# Double Jump

A spy-platformer roguelite in one HTML file. You play **Agent Jesper**, a pocket-sized tuxedoed operative who runs, jumps and stomps through six enemy fronts, then takes down the Croupier and cracks the Vault. One life per run. A casino on the side bankrolls the gadgets.

No build step, no dependencies. Open `index.html` in a browser and play.

## Daily run

The title screen's **Daily run** gives everyone the same map and the same levels for the day (seeded from the UTC date), with a fixed standard kit and one **mutator** that rotates daily:

| Mutator | Effect |
|---|---|
| Glass cannon | Only 2 hearts, but every chip is worth 50% more |
| Rush hour | Every mission is a Gold Rush |
| Hot pursuit | The rival speeds up from turn 2 and its heist meter is only 12 |
| Lights out | Every mission is a Blackout |
| Silent night | An alarm costs a heart (never your last), but bonus objectives pay double |

Your best result for each day (Vault cracked first, then hexes held, then chips) is remembered and shown on the title screen, and the end screen says when you beat it. Dice rolls and rival moves are still random, so the map is shared but the run is not.

## Agent file: stats and field guide

**Stats & field guide** on the title screen opens your lifetime record: runs, Vaults cracked and win rate, missions and raids won, takedowns, silent takedowns, best chain, chips earned, bonus objectives, briefcases, alarms tripped, dashes, rival agents and Croupiers beaten.

Below it is a field guide that fills in as you play. Enemies and hazards are logged the first time they come near you (a toast says "Field guide updated"), gadgets and dossiers when you own them, complications when you play one, and field events when they happen. Undiscovered entries show as `???`, so the guide doubles as a checklist. Stats are saved as you go and when the tab is hidden.

## Saving and resuming

Your run saves automatically every time you reach the map and right after each dice roll, so a refresh, a crash or a phone reclaiming the tab doesn't lose it. The title screen shows **Continue run** with a summary. A few rules keep the save honest:

- Closing the game **mid-mission** counts as fleeing: you lose a heart and the rival takes a turn when you resume. If that was your last heart, the run ends.
- The dice you rolled are kept, so reloading can't be used to re-roll.
- Closing the game on the dossier screen brings the dossier choice back.
- Starting a new run while a save exists asks you to press **Start a run** twice.
- Dying or finishing a run clears the save. The training mission never touches it.

## Learning the game

- **Training mission**: the title screen has a guided course covering movement, jumping, stomping and chains, the silent sap, laser gates and cameras. It has on-screen prompts, no damage and no alarm, and you can leave from the pause menu. The title screen suggests it until you finish it once.
- **First-time hints**: the first time each gadget, enemy or hazard matters (dash, smoke bomb, dart pen, armored goons, snipers, springs, planks, cameras and lasers, raid agents, blackouts, chains) a short hint appears at the top of the screen. Each one shows once and is remembered.

## How a run works

1. **Pick a hex.** The map is seven hexes: six fronts (Gold, Circuits, Intel) around the Vault. Your first mission can be anywhere; after that you can only move next to hexes you hold.
2. **Roll the dice.** Before every mission two dice roll. Each hex you hold that shows the rolled number pays out one of its resource. Number tokens and odds dots work like a familiar settlers board game: 6 and 8 come up most. Rolling a 7 means a mole in the agency: if you hold more than 7 resources, you lose half.
3. **Run the mission.** A side-scrolling level generated fresh from the run's seed. Reach the exit door.
4. **Choose a dossier.** Clear a hex to own it (+2 of its resource, +1 heart), then pick one of three random perks for the rest of the run.
5. **Spend and upgrade.** Resources go to the Gadget Bench or to **outposts**: tap a held hex and upgrade it (2 Gold, 1 Circuits, 1 Intel) so it pays double on its number. Chips go to the casino.
6. **Hold off the rival.** After every mission the rival agency, the Obsidian Hand, takes a turn (see below).
7. **Crack the Vault.** Hold all six hexes and the centre opens. Beat the Vault's guardian, then reach the vault door to win. Each run's guardian is one of two bosses:
   - **The Croupier**, a card-throwing dealer bot. Stomp him. Once he is hurt, every landing sends a gold shockwave along the floor.
   - **The Warden**, a hovering security mech. It is shielded while it patrols and fires fans of shots, then sends floor waves in both directions (jump them) and slams down. Only while it is slammed down is its core exposed: stomp it (2 damage) or dart it (1). Hit it while it hovers and you just bounce off. Below half health it fires wider fans and sends three waves.

Lose all hearts, or let the rival's heist meter fill, and the run ends. Either way you earn agency XP.

## In a mission

| | Keyboard | Touch |
|---|---|---|
| Move | Arrows or A / D | ◀ ▶ |
| Jump (hold for height) | Space, W, Up or Z | JUMP |
| Fire dart, or sap without the pen | X, J or F | FIRE |
| Dash (needs Phase Dash) | C, Shift or K | DASH |
| Smoke Bomb (needs stock) | B or E | BOMB |
| Pause | P or Esc | Pause button |
| Mute everything | M | SFX / MUSIC buttons |

- **Sap** (no Dart Pen needed): press fire next to a goon. Creep up behind one that hasn't spotted you for a silent takedown (+1 chip, and armored goons lose their plating). From the front it only stuns them for half a second.
- **Goons** (walking bots): stomp them for 2 chips.
- **Armored goons** (steel helmets, from threat 2): the first stomp or dart knocks the armor off and stuns them, the second kills for 4 chips.
- **Chains**: take down enemies one after another without touching the ground and each link pays 1 more chip (up to +5). Landing or getting hit resets the chain.
- **Drones**: stomp or dart them for 3 chips.
- **Turrets**: fire slow shots along the ground. Stomp or dart them for 3 chips.
- **Snipers** (crimson turrets, from threat 3): a red aim line tracks you, locks for the last third of a second, then fires a fast shot along it. Move, jump or dash out of the line. Stomp or dart them for 5 chips.
- **Laser gates**: they flicker before switching on. Time your crossing.
- **Plank bridges**: wooden planks over short gaps drop about a third of a second after you step on them, and grow back after a few seconds. Keep moving, or just jump the gap.
- **Conveyor belts** (from threat 1): metal belts with moving arrows carry you, and the goons standing on them, along at 0.9 pixels per frame. Run with one for a speed boost, run against it to make slow progress, or hold the opposite direction to stand still. Jumping off is unaffected. A belt is never placed right before a moving-platform gap.
- **Spring pads**: step on one to be launched high. Chips are strung along the arc, and the launch always lands inside the same stretch of ground.
- **Moving platforms**: ride them across wide gaps.
- **Briefcase**: one per mission, hidden on a high platform. Worth a free resource.
- **Safe blocks** (grey with a brass dial): hit from below for 5 chips.
- Falling in a pit costs a heart and puts you back on the last solid ground.

- **The Croupier** (vault boss): once he is down to 6 HP, every landing sends a gold shockwave rolling along the floor each way. Jump or dash over them.

- **Reading the action**: your hearts and shields sit under the alert bar on the screen itself (so they show on phones too), the lost heart flickers when you are hit, and at one heart the screen edge pulses red with a heartbeat. A pink arrow at the screen edge warns of a shot or card flying in from off-screen. Hit enemies flash white, kills pop a ring, and long chains get a bigger pop-up. The camera leans a little in the direction you run.

Each hex type flavours its level: Gold fronts drop more chips and safes, Circuits fronts have more lasers, Intel fronts have more goons. Threat rises with every hex you hold.

## The Obsidian Hand (rival agency)

- Every 2 missions it seizes a hex, preferring good numbers next to hexes it already holds.
- When no free hex is left it seizes one of yours. **Outposts can't be seized.**
- Each mission, its heist meter rises by the number of hexes it holds, and by 1 more for each of its hexes that matches the dice roll. At 15 it cracks the Vault and your run is over.
- Raid a rival hex to take it back: +1 threat, +3 resources instead of 2, and the heist meter drops by 3.
- A rival **agent** guards the exit of every raid. They chase you, jump, and fire fast shots along your line. It takes three stomps or darts to put them down, and the exit stays locked until they fall. Beating them pays 10 chips and drops the heist meter by 1 more.
- Every hex the rival seizes gets a **trait**, shown on the map (FORT, NEST or SPY) and in the brief:

| Trait | While the rival holds it | Retaking it pays |
|---|---|---|
| Fortified | Its guards wear armor and the approach is one threat harder | +2 resources |
| Sniper nest | Snipers cover the approach | +15 chips and +1 Intel |
| Spy ring | Adds +1 to the heist meter every turn | Heist meter −2 more |

- **The rival adapts to your kit.** Carry the Dart Pen and raid levels fill with armored guards, carry the Signal Jammer and they add drones, carry Phase Dash and they add snipers. The brief tells you what to expect.
- **Ambushes.** Once the rival holds two or more hexes, an ordinary mission can turn out to be an ambush: a rival agent guards its exit, just like a raid. The brief shows the chance (about 15% with two hexes, rising to about 36% with five, and more at Heat 3 and above).

## Settings, accessibility and installing

The **SETTINGS** button in the header (from the title or map screens) opens:

- **Controls**: every action has three key slots you can rebind (click a slot, press the new key, Esc cancels; assigning a key that is already used moves it). P (pause) and M (mute) are fixed. The key hint under the game updates to match, and bindings are remembered.
- **Colour vision**: Protanopia, Deuteranopia and Tritanopia modes apply a daltonisation filter to the whole game, shifting the colours you can't distinguish into ones you can.
- **Touch controls**: Normal or Large buttons, and an option to always show the on-screen controls (for hybrid devices).
- **Reduce screen shake and flashing**: turns off shake, damage flashes and the alarm pulse.
- **Show tutorial hints again**: resets the one-time hints.

**Installing and offline play**: when served over HTTP(S) (for example from GitHub Pages) the game registers a service worker and a web app manifest, so browsers can install it like an app and it keeps working with no connection after the first visit. The page itself is fetched network-first, so updates arrive as soon as you are back online. Open the file directly from disk and it simply runs as a normal page.

## Sound and music

All audio is synthesized in the browser with the Web Audio API, so there are no sound files to download. The title and menus have a calm track, each mission theme has its own track, and the music speeds up and gets heavier when an alarm trips or the Croupier fight starts.

The **SFX** and **MUSIC** buttons in the header switch each one off separately, and **M** toggles both. Your choice is remembered between visits. Sound starts after your first click or key press, as browsers require, and pauses when the tab is hidden.

## Stealth and alarms

- **Cameras** sweep a cone from the ceiling. **Drones** shine a searchlight down. **Goons** spot you if you're in front of them on the same level.
- Being seen fills the alert meter (top left). It drains slowly when nobody can see you.
- At full alert the **alarm** trips: reinforcements drop in ahead of you, spotted goons move faster, and lasers stay on longer.
- Darts can shoot out cameras. The **Signal Jammer** gadget shuts them all off.

### Field events

After a mission (and its dossier pick), there is a 40% chance of a short event before you return to the map: a defector selling the rival's timetable, a smuggler's cache, a dealer with a tell, a safehouse offer, or a courier you can feed false intel. Each offers a risky choice or a safe one. Choices you can't afford are greyed out.

### Mission types

About half of the unclaimed hexes are a special **mission type**, shown as a tag on the map (▣ SIEGE) and described in the brief. Unlike complications they change the level's structure, and each pays its own bonus when you clear it. They stack with a complication on the same hex.

| Type | What it is | Bonus |
|---|---|---|
| Siege | A short flat arena. Three waves of guards (goons, armored goons, turrets and snipers as threat rises) arrive as you reach each trigger, and the exit stays locked until every guard is down. A raid or ambush makes the waves bigger and more armored | +15 chips |
| Chase | A security shutter starts closing in from behind after a few seconds and speeds up with threat. If it catches you it costs a heart and drops back. The level has no moving platforms, fewer lasers and guards, and extra chips | +1 resource if it never catches you |
| Tunnel | A low-ceiling corridor packed with lasers and turrets. No drones, cameras or springs, and the double-jump boots are switched off | +10 chips and +1 Intel |

### Complications

Many unclaimed hexes carry a complication, shown as a warning tag on the map and spelled out in the brief. Each one changes the level and pays **+1 resource** of the hex's type when you clear it.

| Complication | Effect |
|---|---|
| Blackout (DARK) | Cameras are dead, but the level is nearly pitch black. You only see a small circle around you |
| Gold Rush (RUSH) | About a third more chips and goons |
| Lockdown (LOCK) | More laser gates, and they stay on longer |

Complications are re-rolled after a hex is cleared, so a raid on a rival-held hex may bring a new one.

### Bonus objectives

Every hex shows one optional objective in its brief. Completing it pays 12 chips, 1 resource and agency XP.

| Objective | Goal |
|---|---|
| Ghost | Never trip the alarm |
| Clean hands | No takedowns |
| Fast exit | Beat the par time |
| Bagman | Collect 75% of the chips |
| Courier | Find the hidden briefcase |

## Dossiers (perks)

After each cleared mission, pick one of three:

| Perk | Effect |
|---|---|
| Light Loafers | Run 15% faster |
| Coat-tail Glide | Hold jump while falling to drift |
| Featherweight | Higher jump |
| Safecracker | Safes pay 10 |
| Pickpocket | +2 chips per takedown |
| Chain Reaction | Chain links pay +1 more chip each |
| Quick Draw | Darts fire twice as fast |
| Deep Cover | Free shield at the start of each mission |
| Second Wind | Survive one fatal hit per run |
| Laser Tuned | Lasers stay off longer |
| Piercing Darts | Darts pass through enemies |
| Informant Network | +1 on every dice payout |
| Lucky Seven | A rolled 7 pays 10 chips instead |
| Card Counter | See the dealer's hole card; slot pairs pay 9 |
| Ghost Protocol *(Operative)* | Alert builds half as fast |
| Fence *(Operative)* | Black-market trades are 2 for 1 |
| Double Agent *(Senior Operative)* | The rival moves every 3 missions |
| Inside Man *(Senior Operative)* | The heist meter fills half as fast |

## The Croupier

The Vault boss. Stomps deal 2 damage, darts deal 1. It deals arcs of playing cards and jumps at you; below half health it goes all in with faster, wider volleys. The vault door stays sealed until it folds.

## Gadget Bench

| Gadget | Cost | Effect |
|---|---|---|
| Spring Heels | 1 Gold, 1 Circuits | Double jump |
| Dart Pen | 2 Intel, 1 Gold | Shoot darts |
| Phase Dash | 2 Circuits, 1 Intel | Dash forward; invulnerable mid-dash, even to lasers |
| Smoke Bomb | 1 Intel | Stock up to 3. Wipes your alert and any alarm, blinds cameras and drones for 5 seconds, stuns every goon |
| Magnet Cufflinks | 2 Gold | Pull nearby chips |
| Bowtie Shield | 1 Circuits, 1 Intel | Absorb one hit (stack to 3) |
| Field Medkit | 1 of each | +1 max heart (up to 6) |
| Signal Jammer | 2 Circuits | Cameras go dark, alert builds slower |

Black-market trade: 3 of one resource for 1 of another.

## The Gilded Ace (casino)

- **Roulette**: single-zero wheel. Red, black, odd, even, 1–18, 19–36 pay even money; zero pays 35 to 1.
- **Blackjack**: bets of 5, 10 or 25. Dealer stands on 17. Blackjack pays 3 to 2. Double on your first two cards.
- **Slots**: 5 chips a pull. 7-7-7 pays 80, ★★★ 40, BAR×3 25, ♦ or ♣ ×3 15, any pair 7. About a 95% return.
- **Cashier**: buy a resource for 12 chips, or sell one for 5.

## Agency rank (progress between runs)

Every run earns XP: 10 per mission won, 8 per bonus objective, 5 per raid, 3 per briefcase and 60 for cracking the Vault. Heat multiplies it. XP is saved in the browser.

| Rank | XP | Unlocks |
|---|---|---|
| Recruit | 0 | Standard issue kit |
| Field Agent | 60 | Gambler kit (+40 chips) |
| Operative | 160 | Engineer kit (Spring Heels), Ghost Protocol and Fence dossiers |
| Senior Operative | 320 | Diplomat kit (shield + Informant Network), Double Agent and Inside Man dossiers |
| Section Chief | 550 | Ghost kit (Signal Jammer + Ghost Protocol) |
| Director | 900 | Gold-trimmed tux |

### Heat

Crack the Vault to unlock the next heat level. Each one stacks on those below it and adds 25% XP.

1. Every mission is +1 threat.
2. From turn 4 the rival moves every mission.
3. Start with 2 hearts.
4. Alarms bring double reinforcements and alert builds faster.
5. The Croupier has 12 HP and the heist meter caps at 12.

## Run it

```bash
# any static server works
python3 -m http.server 8000
# then open http://localhost:8000
```

### Publish with GitHub Pages

The included workflow in `.github/workflows/pages.yml` deploys the repo on every push to `main`. In your repo go to **Settings → Pages** and set **Source** to **GitHub Actions**.

## Code map

Everything lives in `index.html`:

- **State and run setup**: seeded RNG (`mulberry32`), hex layout, resources.
- **Map**: SVG hex board, adjacency, dice roll and payouts.
- **Level generation**: `genLevel(type, threat, seed)` builds a column height map, then places platforms, safes, goons, drones, lasers and chips.
- **Sprites**: pixel art defined as strings and pre-rendered to offscreen canvases (`spr`), with squash and stretch at draw time.
- **Runtime**: fixed 60 Hz step, tile collision (`moveBody`), coyote time, jump buffering, hit-stop, moving platforms, boss AI.
- **Rendering**: 320×192 canvas, scaled by CSS to a whole-number multiple of the screen's device pixels (`fitStage`) so every game pixel is the same size on fractional-density phones. The camera and player are interpolated between 60 Hz physics steps for smooth motion on 90/120 Hz screens. Tiles and the skyline are pre-rendered once per level. Layered parallax per theme, weather, additive glows and a vignette sit on top.
- **Rival, stealth and meta**: `rivalTurn`, `tripAlarm`, `objState`, and `meta` / `RANKS` / `KITS` / `HEATS` for the agency layer.
- **Casino and Bench**: plain DOM.

## Testing

`tools/fuzz.py` plays about 300 generated missions (every hex type, threat and heat level) with a scripted bot and reports any level it can't finish, with an ASCII map of where it got stuck. Requires Playwright.

## Ideas for next steps

- Sound effects and music
- More gadgets (grapple, smoke bomb, tux glider)
- Baccarat and poker tables
- Daily seed challenge

## License

MIT. Agent Jesper and every asset in this repo are original.
