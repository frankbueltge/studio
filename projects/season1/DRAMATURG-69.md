# DRAMATURG-69 — STILL DARK, increment 1, rebuild of state 1

*The staging memo as delivered to the conductor, before the rebuild was built and before any
reader saw anything. §D is the pre-registration the panel is scored against. One deviation from
§A was made by the conductor at build time and is recorded at the foot of this file.*

---

## §A. The rebuilt state 1

**DOM / screen-reader order:** heading → tier column-header → scale → eleven rows → counter block → control → footer. One screen, no scroll at t=0.

1. `4 AUGUST 2026` — unchanged. Q1 passed 3 of 3; do not touch what passed.
2. **New single line above the rows, row face, dim:**
   `SOURCED  name · flag · days dark · waters        DERIVED  both ends of every date`
3. Eleven rows, bars, hatched ends, labelled `4 AUG` rule — unchanged.
4. **Counter block, three lines.**
   Heading face, large:
   `knowable on 4 Aug — 11 of ____ · ____%`
   Small, tagged:
   `OBSERVED — this house counted 11 vessels in the edition of 4 August, in its own capture: 2026-08-05T04:39:32Z · HTTP 200 · 35,473 bytes · sha256 ed3e54ec…`
   Small, dim:
   `read so far: 1 edition, captured by this house. what fills the blanks is the next capture.`
5. **The control.** Label **before** the input in the DOM (Reader A could not tell what it was; in the old build the label trailed the slider).
   Label: `drag — this adds the next edition this house captured; the day itself does not move.`
   Tick left: `4 Aug edition` · Tick right: `+ 5 Aug edition`
   `aria-valuetext`: `4 Aug edition` / `4 Aug edition + 5 Aug edition`
6. Footer: source link + method quote + the "intentional/no illegality" sentence + full sha256 of each capture. The SOURCED/DERIVED/OBSERVED *definitions* leave the footer (they now sit where they bite).

**Removed from state 1, and why each is staging:**

- **The ceiling sentence.** It is the work's finding and it told the ending (Reader C stopped because of it). It appears verbatim, unedited, at the turn. Not concealment: nothing at state 1 asserts completeness — `1 edition` and two blanks assert the opposite.
- **`0–11` and `100%`.** Replaced by blanks. `100%` is an artifact of a single capture (denominator = numerator), read by 3 of 3 as arithmetic, and it is the misleading assertion constraint 2 forbids: bare, it says *the day is known*. A blank says *not yet*, which is true.
- **`$ python3 …day.py 2026-08-04`** at state 1 — economy; it reappears at the turn with unedited output.
- **The standalone `OBSERVED 11 · first seen …` line** — folded into the evidence line, not deleted.

**Does state 1 show a share? No.** In its place stands the measured numerator with its evidence, and two blanks. The reader loses the headline figure — and with it the false impression of a finished measurement. The crux, stated plainly: *withholding a conclusion is staging; printing a provisional number as if settled is a lie.* We print incompleteness and withhold direction. Nothing on state 1 becomes misleading by the omission of "can only fall"; `100%` becomes misleading without it.

## §B. The turn — one notch

`11` does not move. The blanks fill: `knowable on 4 Aug — 11 of 0–14 · 79%–100%`. Three rows slide in below a dashed rule — SOUTHERN SEAS NO.302, RICKY, ALTAR 10 — each stamped `first seen in the edition of 5 August`, crossing the same 4 AUG rule. The evidence line gains both later captures, including `2026-08-05T19:17:55Z · 200 · 35,485 bytes · sha256 17c07fc3… (byte-identical to 12:54)` — a night that added nothing, printed. Then, first time on the face: `a ceiling from 3 captures: further nights can only add vessels to this day, so this share can only fall.` Then the command and its verbatim output.

**Builder, determinism:** the embedded output is stale ("2 capture(s)"). Regenerate: stop 2 = `python3 projects/season1/capture/day.py 2026-08-04` (prints 3 captures, 11 of 0–14, 79%–100%); stop 1's state = the same script with `--captures` over the 4 August capture alone. Print both commands at the turn.

**What the reader holds:** their count survived; the thing it was a share *of* grew underneath it. One more look made the number worse, and the last line says it can only go that way.

## §C. Making OBSERVED read

Two placements, no paragraph. (1) The tag and the count share one string with the timestamp, status, bytes and hash — readers already called that evidence measured; the number now travels inside it instead of above it. (2) The column-header line binds `days dark` to SOURCED and the dates to DERIVED at the columns themselves, one line, where the eye is.

## §D. Re-registered thresholds

Questions verbatim from DRAMATURG-68 §B; dispatch verbatim; three new severed readers, `STATE-1.txt` alone.

- **Q1** *In one sentence: what does this page show?* — **2 of 3**.
- **Q2** *There is one control. Would you move it, or is this where you stop? Answer "move" or "stop", then one sentence.* — **3 of 3 "move"**. Unchanged. A threshold loosened after a failure is worth less than the failure it hides.
- **Q3** *What do you expect would change if you moved it?* — **2 of 3** say what is *known* / the record changes.
- **Q4** *Which numbers here were measured by whoever made this, and which worked out from other numbers?* — **2 of 3** place the count 11 as measured and the date bands as worked out, **and do not call `56 d dark` derived**. Tightened, not loosened: the column header now names it.
- **Void clause:** if the mechanical extraction of state 1 needs one bracketed or editorial word of ours, or any reader receives anything but `STATE-1.txt`, Q1–Q4 report VOID and no threshold is claimed.
- **Pre-registered escalation:** Q2 at ≤1 a second time retires the two-stop slider as a mechanism, as the return was retired. It is not restaged a third time.

## §E. Cuts

Cut: the ceiling sentence from state 1; `0–11 · 100%`; the state-1 command line; the duplicate OBSERVED line; the tier definitions from the footer. **If forced to cut more: the verbatim `day.py` block at the turn.** Checkability survives in the printed command and the hashed captures; the block is the most page-space per unit of experience on the screen.

---

## Deviation from §A, made at build time by the conductor, and why

**§A.4's third line was specified as** `read so far: 1 edition, captured by this house. what fills
the blanks is the next capture.` **Built as** `on this screen: 1 edition — the first this house
captured. what fills the blanks is the next one.` Reason: the footer at state 1 lists **three**
captures by name, so *"read so far: 1 edition"* would have read as a contradiction of the house's
own evidence line. *"On this screen"* says what is true of the screen without denying what is on
disk. The change was made before any reader saw the page, and the panel measured the built string.

**§B was built with one addition:** the stop-2 command block prints **two** commands — the first
screen's (`--as-of 2026-08-05T05:00:00Z`) and this screen's — because the first screen's state
would otherwise be one only this house could reproduce. `day.py` gained the `--as-of` flag for
exactly that, and its ceiling line now counts **distinct editions** beside captures, since three
captures held two editions tonight.
