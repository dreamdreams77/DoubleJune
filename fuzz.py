"""Level fuzzer: plays ~300 generated missions with a scripted bot and reports any it cannot finish.
Usage: pip install playwright && playwright install chromium && python fuzz.py [path/to/index.html]
  FIGHT=1 python fuzz.py   runs the boss and raid-agent fights instead, with real hearts (3 and 5),
                           and prints win rates and hearts lost (the Croupier by heat, boots and hearts).
  CHROMIUM_PATH=...        use a specific Chromium binary.
  SHOW=n                   print n failing levels (default 3).
"""
import sys
from playwright.sync_api import sync_playwright
import os, tempfile, pathlib
ROOT=pathlib.Path(__file__).resolve().parent
SRC=sys.argv[1] if len(sys.argv)>1 else str(ROOT/"index.html")
TMP=tempfile.mkdtemp()
head=''
s=open(SRC).read()
hook='''window.__sim=(hex,cleared,heat,boots,raid,hearts)=>{
  const H=hearts||9999;run.cleared=cleared;run.heat=heat;run.hearts=H;run.maxHearts=H;run.gadgets.boots=boots;run.gadgets.pen=true;
  if(raid)run.hexes[hex].rival=true;
  if(hex===6)run.hexes.forEach(h=>h.claimed=true);
  startLevel(hex);running=true;
  let stuck=0,best=0,frames=0,res="timeout";
  for(;frames<12000;frames++){
    {const p=L.p,ahead=p.x+p.w;
    const fb=(L.boss&&L.boss.alive?L.boss:(L.agent&&L.agent.alive?L.agent:null));
    if(fb&&p.x>L.arenaX-60){ // fight mode: keep range, face the target, dart it, jump shots
      const dx=fb.x+fb.w/2-(p.x+p.w/2),want=dx>0?1:-1,ad=Math.abs(dx);
      let mv=0;if(ad>110)mv=want;else if(ad<56&&L.boss)mv=-want;
      if(mv===0&&p.face!==want)mv=want;
      press("right",mv>0);press("left",mv<0);
      const threat=L.shots.some(s=>Math.abs(s.x-p.x)<44&&((s.vx>0&&s.x<p.x+4)||(s.vx<0&&s.x>p.x-4))&&Math.abs(s.y-p.y)<22)||L.cards.some(c=>Math.abs(c.x-p.x)<40&&c.y<p.y+30&&c.y>p.y-60)||(L.boss&&Math.abs(dx)<44&&L.boss.onGround===false);
      if(p.onGround&&threat)L.hold=16;
      press("jump",(L.hold||0)>0);L.hold=(L.hold||0)-1;
      press("fire",frames%12===0&&p.face===want&&Math.abs(fb.y+fb.h/2-(p.y+p.h/2))<26);
    }else{
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
    press("fire",frames%20===0);}}
    step();
    if(L.p.x>best+1){best=L.p.x;stuck=0}else stuck++;if(frames%15===0){(L.tr=L.tr||[]).push([L.p.x|0,L.p.y|0,+L.p.vx.toFixed(1),+L.p.vy.toFixed(1),L.p.onGround?1:0,L.p.inv]);if(L.tr.length>14)L.tr.shift()}
    if(L.dying){res="dead";break}
    if(L.exiting||(!running&&$("#ovl").hidden===false)){res="clear";break}
    if(stuck>1500){res="stuck";break}
  }
  const c0=Math.max(0,Math.floor(L.p.x/16)-6);let map=[];for(let r=0;r<12;r++){let line="";for(let c=c0;c<c0+16&&c<L.W;c++){const pc=Math.floor((L.p.x+5)/16),pr=Math.floor((L.p.y+7)/16);line+=(c===pc&&r===pr)?"@":".#=$o"[L.tiles[r][c]]}map.push(line)}
  const pl=L.E.plats.map(m=>[m.x0/16|0,(m.x0+m.range+40)/16|0,m.y/16]).filter(m=>m[0]>c0-4&&m[0]<c0+16);
  const near=o=>Math.abs(o.x-L.p.x)<120;const ents={goons:L.E.goons.filter(g=>g.alive&&near(g)).map(g=>[g.x|0,g.y|0]),lasers:L.E.lasers.filter(near).map(l=>l.x),turrets:L.E.turrets.filter(t=>t.alive&&near(t)).map(t=>t.x)};running=false;return {tr:L.tr,ents,map:map.join(String.fromCharCode(10)),pl,c0,res,frames,x:L.p.x|0,exit:L.exitX,W:L.W,type:L.type,d:L.d,hearts:run.hearts,H:H,alarm:L.alarmEver,kills:L.kills};
};'''
s=s.replace('/* ---------- flow ---------- */',hook)
open(os.path.join(TMP,'fuzz.html'),'w').write(head+s)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path=os.environ.get("CHROMIUM_PATH") or None); pg=b.new_page()
    errs=[]; pg.on("pageerror",lambda e:errs.append(str(e)))
    pg.goto("file://"+os.path.join(TMP,"fuzz.html")); pg.click("#btnStart")
    if os.environ.get("FIGHT"):
        for label,cfgs in [("Croupier",[(6,6,h,b,False,hp) for h in (0,3,5) for b in (False,True) for hp in (3,5)]),("Raid agent",[(hx,c,h,b,True,hp) for hx in range(6) for c in (2,5) for h in (0,3) for b in (False,) for hp in (3,)])]:
            res={"clear":0,"dead":0,"stuck":0,"timeout":0};lost=[];frames=[]
            for cfg in cfgs:
                for _ in range(2):
                    r=pg.evaluate("__sim(%d,%d,%d,%s,%s,%d)"%(cfg[0],cfg[1],cfg[2],str(cfg[3]).lower(),str(cfg[4]).lower(),cfg[5]))
                    res[r["res"]]+=1
                    if r["res"]=="stuck":print("   stuck:",cfg,"x",r["x"],"exit",r["exit"])
                    lost.append(r["H"]-r["hearts"]);frames.append(r["frames"])
                    bd=globals().setdefault("BD",{});k=(label,cfg[2],cfg[5],cfg[3]);bd.setdefault(k,[0,0]);bd[k][1]+=1;bd[k][0]+=(r["res"]=="clear")
            n=sum(res.values());print(label,n,"fights",res,"win rate %.0f%%"%(100*res["clear"]/n),"avg hearts lost %.1f"%(sum(lost)/n),"avg frames %d"%(sum(frames)/n))
        for k,v in sorted(BD.items()):
            if k[0]=="Croupier":print("  Croupier heat",k[1],"hearts",k[2],"boots" if k[3] else "no boots","->",v[0],"/",v[1])
        print("ERR",errs[:5]); b.close(); sys.exit(0)
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
