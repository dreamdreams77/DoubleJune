"""Level fuzzer: plays ~300 generated missions with a scripted bot and reports any it cannot finish.
Usage: pip install playwright && playwright install chromium && python fuzz.py [path/to/index.html]
"""
import sys
from playwright.sync_api import sync_playwright
import os, tempfile, pathlib
ROOT=pathlib.Path(__file__).resolve().parent
SRC=sys.argv[1] if len(sys.argv)>1 else str(ROOT/"index.html")
TMP=tempfile.mkdtemp()
head=''
s=open(SRC).read()
hook='''window.__sim=(hex,cleared,heat,boots)=>{
  run.cleared=cleared;run.heat=heat;run.hearts=9999;run.maxHearts=9999;run.gadgets.boots=boots;run.gadgets.pen=true;
  if(hex===6)run.hexes.forEach(h=>h.claimed=true);
  startLevel(hex);running=true;
  let stuck=0,best=0,frames=0,res="timeout";
  for(;frames<12000;frames++){
    {const p=L.p,ahead=p.x+p.w;
    const zone=L.E.plats.find(m=>p.x+p.w>=m.x0-24&&p.x<=m.x0+m.range+m.w+8);
    let right=true,jump=false;
    if(p.ride){right=solidAt(ahead+6,p.y+p.h+2)||(p.x+p.w+6<p.ride.x+p.ride.w)}
    else if(zone&&p.onGround&&!solidAt(ahead+6,p.y+p.h+2)){const m=zone;right=(m.x<=ahead+2&&m.x+m.w>ahead+8)}
    if(p.onGround&&right){
      const gap=!p.ride&&!solidAt(ahead+8,p.y+p.h+2);
      const wall=solidAt(ahead+6,p.y+2)||solidAt(ahead+6,p.y+p.h-3);
      const foe=L.E.goons.some(g=>g.alive&&g.x>p.x-4&&g.x-p.x<34&&Math.abs(g.y-p.y)<20)||L.E.turrets.some(t=>t.alive&&t.x>p.x&&t.x-p.x<30)||(L.boss&&L.boss.alive&&Math.abs(L.boss.x-p.x)<50);
      const lz=L.E.lasers.find(l=>l.x>p.x-6&&l.x-p.x<44);
      if(lz&&(lz.active||lz.warn))right=false;
      if((gap&&!zone)||wall||foe)jump=true;
    }
    if(jump)L.hold=18;
    press("right",right);press("jump",(L.hold||0)>0);L.hold=(L.hold||0)-1;
    press("fire",frames%20===0);}
    step();
    if(L.p.x>best+1){best=L.p.x;stuck=0}else stuck++;if(frames%15===0){(L.tr=L.tr||[]).push([L.p.x|0,L.p.y|0,+L.p.vx.toFixed(1),+L.p.vy.toFixed(1),L.p.onGround?1:0,L.p.inv]);if(L.tr.length>14)L.tr.shift()}
    if(L.exiting||(!running&&$("#ovl").hidden===false)){res="clear";break}
    if(stuck>1500){res="stuck";break}
  }
  const c0=Math.max(0,Math.floor(L.p.x/16)-6);let map=[];for(let r=0;r<12;r++){let line="";for(let c=c0;c<c0+16&&c<L.W;c++){const pc=Math.floor((L.p.x+5)/16),pr=Math.floor((L.p.y+7)/16);line+=(c===pc&&r===pr)?"@":".#=$o"[L.tiles[r][c]]}map.push(line)}
  const pl=L.E.plats.map(m=>[m.x0/16|0,(m.x0+m.range+40)/16|0,m.y/16]).filter(m=>m[0]>c0-4&&m[0]<c0+16);
  const near=o=>Math.abs(o.x-L.p.x)<120;const ents={goons:L.E.goons.filter(g=>g.alive&&near(g)).map(g=>[g.x|0,g.y|0]),lasers:L.E.lasers.filter(near).map(l=>l.x),turrets:L.E.turrets.filter(t=>t.alive&&near(t)).map(t=>t.x)};running=false;return {tr:L.tr,ents,map:map.join(String.fromCharCode(10)),pl,c0,res,frames,x:L.p.x|0,exit:L.exitX,W:L.W,type:L.type,d:L.d,hearts:run.hearts,alarm:L.alarmEver,kills:L.kills};
};'''
s=s.replace('/* ---------- flow ---------- */',hook)
open(os.path.join(TMP,'fuzz.html'),'w').write(head+s)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path=os.environ.get("CHROMIUM_PATH") or None); pg=b.new_page()
    errs=[]; pg.on("pageerror",lambda e:errs.append(str(e)))
    pg.goto("file://"+os.path.join(TMP,"fuzz.html")); pg.click("#btnStart")
    out={"clear":0,"stuck":0,"timeout":0}; bad=[]; n=0; alarms=0
    for rep in range(6):
      for hex in range(7):
        for cleared in ([0,2,4,6] if hex<6 else [6]):
          for boots in [False,True]:
            pg.evaluate("begin && 0") if False else None
            r=pg.evaluate(f"__sim({hex},{cleared},{rep%6},{str(boots).lower()})")
            n+=1; out[r["res"]]+=1; alarms+=r["alarm"]
            if r["res"]!="clear": bad.append(r)
    print(n,"levels",out,"alarm rate",round(alarms/n,2))
    print("stuck by type:",{t:sum(1 for r in bad if r["type"]==t) for t in ["gold","circ","intel","vault"]})
    for r in bad[:int(os.environ.get("SHOW","3"))]: print(r["type"],r["d"],r["x"],"plats",r["pl"],r["ents"],"hearts lost",9999-r["hearts"]);print(r["tr"]); print(r["map"]); print()
    print("ERR",errs[:5]); b.close()
