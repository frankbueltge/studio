# VERIFIER-92 — the premiere gate, third convening

## FAIL — 4 blocking items

`projects/season1/still-dark/index.html`, opening hash
`a7912784ae540e2e11ba6fcb2227af8510eb6632004b03bd6a0823f59dec7aee`. HEAD `b619af4`, twelve paths
dirty, unmoved through the pass.

The numbers are right. Every figure on the face reproduces from the captures, all ten printed
commands return their own stop, all thirteen cited URLs answer 200 and every quotation I could
extract is verbatim. What fails is four sentences of prose written **about** those numbers, three of
them written tonight, one of them a stale count this session walked past while repairing its twin
four hundred lines away.

---

## BLOCKING

### 1. A run that has not been twenty-four seconds long since session 85

**String:** `**Three spoken announcements across a twenty-four-second run in which the figure takes
seven states**, measured in a browser by `announce.mjs`, committed beside this file`
**File/line:** `projects/season1/still-dark/README.md:385`

**Why it is false.** The run has ten states and lasts about twenty-nine seconds. The paragraph opens
`**Since session 83 the run says what it is doing…**` — a continuing present — and the figures are
attributed to an instrument in the present tense. The claim is contradicted by *this same file*, 587
lines below, in the SESSION 92 guard table: `**11 figure rewrites** (the empty first paint and the
run's ten states)`. It is the identical defect this session repaired twice elsewhere tonight —
README:782 `Across the nine stops **the run then had**`, and data.py:594 — and missed here. Line 385
sits in the file's only unheaded region: `grep -nE "^#{1,6} "` returns headings at 1, 774, 808, 853,
972 and nothing between 1 and 774, which is the exact ground `../VERIFIER-91.md` §6 blocked on.

**Evidence.**

```
$ cd projects/season1/still-dark && NODE_PATH=… node announce.mjs
FIGURE REWRITES ...... 11
       6 ms  
      67 ms  100 %–100 %
   14173 ms  79 %–100 %
   …
   26974 ms  26 %–100 %
  SPOKEN ............. 3
```

Stops per committed face, at 1,600 ms a step over the page's own `first_dwell_ms: 14118`:

```
1c481c2 (83) stops=7 run≈23.7s   b416e4e (86) stops=8 run≈25.3s
a20d9ae (89) stops=9 run≈26.9s   b619af4 (91) stops=9 run≈26.9s   worktree stops=10 run≈28.5s
```

**Smallest repair:** `across a twenty-four-second run in which the figure takes seven states` →
`across the twenty-four-second run of seven states it then had`. **I checked my own repair:**
`git show 1c481c2:…/index.html | grep -c '"share_falling":'` returns 7, and 14118 + 6×1600 = 23,718
ms — the sentence is exactly true of session 83's face and of no face since session 85. "Three
spoken announcements" is left untouched because `announce.mjs` still returns `SPOKEN ... 3` tonight.

---

### 2. A law dated one session earlier than the face that first carried it

**Strings:**
- `which is the exact threshold the face has published beside the figure since session 83: *"The
  upper end holds at 100 % until more of these ships are certainly dark on this day than the eleven
  the day itself named."*` — `README.md:822–824`
- `Since session 83 the face has printed *"the upper end holds at 100 % until more of these ships
  are certainly dark on this day than the eleven the day itself named."*` — `PROJECT.md:155–157`

**Why it is false.** Session 83's face published a *different threshold*. `1c481c2` is session 83's
own commit (`Ensemble session 2026-08-10 (session 83)`), and its `"constant"` reads:

> Neither end of this figure can rise. The upper end has not moved at all: it holds at 100 % **while
> no ship here is CERTAINLY dark on this day** — a list gives a return only to the nearest week, so
> every one of them is merely possible — **and it falls the moment one of them becomes certain.**

The threshold there is **one** certain ship, not eleven. The eleven-name threshold first stands on
the face at `11bb78f` — session 84 — and the *verbatim* sentence both files quote first stands at
`964b831`, session 87. This is the load-bearing sentence of tonight's headline claim: the whole
"countdown" argument is that certain has reached the published threshold, and the published
threshold is misdated by a session and the quotation attributed to a face that did not carry it.

**Evidence.**

```
$ for h in 1c481c2 11bb78f 964b831; do git show $h:projects/season1/still-dark/index.html \
    | grep -oE '"constant": "[^"]*"' | head -1; done
1c481c2 …it holds at 100 % while no ship here is CERTAINLY dark on this day…
11bb78f …while no more of these ships are CERTAINLY dark on this day than the eleven the day itself named…
964b831 …The upper end holds at 100 % until more of these ships are certainly dark on this day than
        the eleven the day itself named; only the lower end has moved so far…
```

**Smallest repair:** in both files, `since session 83` → `since session 84 (`11bb78f`), in tonight's
wording since session 87`. **I checked my own repair:** `git show 11bb78f:` carries `than the eleven
the day itself named` and `git show 1c481c2:` does not; every face from `11bb78f` to `b619af4`
carries the threshold, and `964b831` onward carries the quoted string byte-for-byte. Both hashes
open locally.

---

### 3. A universal over every face ever printed, unenumerated — banked rule 52

**String:** `**one more certain name and the end this work has marked CANNOT MOVE on every face it
has ever printed comes off 100 %.**`
**File/line:** `projects/season1/still-dark/README.md:825–826`

**Why it is false.** The mark arrives in session 83; the work's own comment says so twice, in the
object under test — `index.html:120` and `index.html:148`, both reading *the mark this face has
meant by CANNOT MOVE **since session 83***. Eight reachable committed faces before that carry no
such mark at all: no `"constant"` key, no `sd-arrive-standing-fig`, no `holds at 100`. The clone is
shallow and grafted, so still-earlier faces exist on the public repository and cannot have carried
it either. This is rule 52's own species, printed four lines above a paragraph that correctly
refuses a *first* on exactly that ground.

**Evidence.**

```
$ for h in 231f550 fb56615 8b8e777 7fdf259 e1d6851 e4cb780 2c42458 f6ca3b0; do \
    git show $h:…/index.html | grep -oE '"constant": "[^"]*"'; done      # ← eight faces, no output
$ for h in f6ca3b0 2c42458 e4cb780; do git show $h:…/index.html | grep -c 'sd-arrive-standing-fig'; done
0 0 0
```

Enumeration, printed as rule 52 requires — the mark on every committed face reachable here:

`231f550` no · `fb56615` no · `8b8e777` no · `dfe8d78` no · `e1d6851` no · `e4cb780` no · `2c42458`
no · `f6ca3b0` no · **`1c481c2` yes** · `c28f01b` yes · `11bb78f` yes · `994f214` yes · `b416e4e`
yes · `abecba4` yes · `964b831` yes · `1003f95` yes · `43f900e` yes · `a20d9ae` yes · `babd179` yes
· `b619af4` yes. **Twelve of twenty, none before session 83.**

**Smallest repair:** `on every face it has ever printed` → `on every face since session 83`. **I
checked my own repair:** the enumeration above is the check — twelve consecutive faces from
`1c481c2` to `b619af4`, with no gap — and it is the wording the work's own two comments already use.

---

### 4. "Every figure here is printed by a command a stranger runs" — three of them are not

**String:** `*No gate had ruled on this state when it was built; it is the object the gate of this
session was given. Every figure here is printed by a command a stranger runs.*`
**File/line:** `projects/season1/still-dark/README.md:810–811`

**Why it is false.** Three figures in the section it governs are measurements of an object held in
no commit, and no command printed anywhere in the work returns them: **266 px** (line 844), the
**15 px** push (line 844), and **one character longer** (line 843). The page they were taken on —
built, then cut before any voice was convened — exists nowhere. The parenthetical offered as the
warrant, `` `git show HEAD:projects/season1/still-dark/index.html` reproduces the 273 px it read at
session 91 ``, does not: that command prints a file. This is the species this file itself struck 90
lines earlier — *"no run of today's instrument returns them. A stale number with a date on it is
still a number nobody can reproduce."*

**Evidence.** The pre-cut object *is* reconstructible, and I reconstructed it, which is what makes
the repair small rather than a deletion:

```
$ python3 -c "p=open('projects/season1/still-dark/index.html').read(); \
  open('/tmp/pc/index.html','w').write(p.replace(\
  'have been dark on the day and that nobody could have had on it',\
  'have been dark on that same day and that nobody could have had on it'))"
replacements: 9
$ NODE_PATH=… node tools/frame.mjs --dir=/tmp/pc
  the hole sharing a frame with the whole figure: 266 px, 22 of 31 chips — floor 268 px / 22 chips — UNDER
     74 px  the hole's heading
$ NODE_PATH=… node tools/frame.mjs                       # the worktree
  the hole sharing a frame with the whole figure: 281 px, 24 of 31 chips — HOLDS
     59 px  the hole's heading
```

74 − 59 = **15 px** ✓. Heading lengths, measured: HEAD 188 chars, pre-cut 189 — **one character
longer** ✓. Line boxes at 390 px: HEAD 4, pre-cut 5, worktree 4 — a *fourth wrapped line* ✓.

**Smallest repair:** print the recipe beside 266, e.g. `— a state held in no commit and rebuilt from
the one that is: replace "dark on the day and that nobody" with "dark on that same day and that
nobody" in the committed page and run `frame.mjs --dir` on the copy; it returns 266 px, 22 of 31
chips, UNDER.` **I checked my own repair:** the commands above are the ones I ran, and they return
exactly 266 px / 22 of 31 chips / UNDER. Note the chip count is **22**, not the 24 the guard table
carries for the repaired page — if the recipe is printed, that figure should be printed with it.

---

## NOTED, not blocking

1. **`273 px and 24 of 24 chips` at README:1019 and 1023** sits *under* the `SESSION 92` guard
   heading (line 972) while tonight's reading, 281 px / 24 of 31, stands 200 lines above. The
   sentences are about sessions 89 and 90 and a careful reader gets it; the first instance carries
   no session stamp of its own. Stamping it `(sessions 89–91)` closes it. I reproduced 273 px / 24
   of 24 on the HEAD page.
2. **README:756 now types `130`** into the same unheaded stretch from which `../VERIFIER-91.md` §6
   struck two figures. It is true tonight (`fold.mjs` returns 130) and it names the guard table
   rather than a line offset, which was the point of the repair — but it is a hand-typed count of a
   list-dependent quantity, which is banked 17's own species, and it will be false on the next list.
3. **`day.py --as-of` accepts malformed instants silently.** `--as-of 2026-08-13T170256Z` (the form
   of the capture filenames) returns `28 capture(s) … 4–35`; `--as-of garbage` returns the full
   answer. Both exit 0. Every instant the face prints is well-formed and all ten check out, but a
   stranger who retypes a capture filename gets a confident wrong number with no error.
4. **`https://www.fidh.org/IMG/pdf/fo-report.pdf`** fetches 200, 7,241,916 bytes, but its text is
   behind a subset-font encoding and neither `pdftotext` nor `pypdf` exists here, so I could **not**
   verify *72 aboard, 63 dead, 14 days adrift* first-hand. Not new tonight; recorded as unverified
   rather than verified. **`forensic-architecture.org/investigation/the-left-to-die-boat`** returns
   200 but 931 bytes of JavaScript shell; it is cited as an address with no quotation on it, so
   nothing is misquoted.
5. **Word ceiling, as instructed, reported not ruled.** `python3 tools/record_words.py --worktree`:
   `TOTAL 3204` — **BREACH by 204** (PROJECT.md 2894 + WORKBOARD section 310). The committed figure,
   which the instrument names as the standing one: `2998 — UNDER by 2`. No asset claims compliance,
   so no printed sentence is false; the object the gate was given is 204 words over.
6. **README:57–59** says *thirty-one* and *nine* are printed by `day.py 2026-08-04`. The command
   prints 11–42 and every name's window; both counts are one step away. Loose in "prints them".

---

## WHAT HOLDS — reproduced first-hand

- **The island belongs to the captures.** `python3 data.py --check` → `island matches the captures`,
  exit 0. `python3 tools/renders.py` → `RENDERS MATCH THE PAGE`, index.html `a7912784ae54…`.
- **The face's figure.** `day.py 2026-08-04` → `26%–100% (11 of 11–42)`, `29 capture(s) read, 10
  distinct edition(s), 11 distinct content(s), 18 distinct bod(y/ies)` — byte-identical to the
  island's `"output"` string and to PROJECT.md's session-92 line.
- **All ten printed per-stop commands return their own stop:** 100/79/69/65/55/44/35/33/31/**26**,
  each from the `--as-of` instant the face prints. `edition.py` lists the 29 captures; the 29th is
  `2026-08-13T17:02:56Z`, edition `2026-08-13`, eleven vessels, seven new to the day, all seven
  certain.
- **The ninth movement of degree** — nine falls, on 5–13 August; and `--as-of` reproduces every one
  of the ten prior values, **including 37 %** (at `2026-08-10T22:04:56Z`).
- **The certain end 4 → 11, whole set of movements 2, 2, 7** — `certain_of` across the stops is
  0,0,0,0,0,0,0,**2**,**4**,**11**. Three movements, enumerated on the face at every stop.
- **The law tested seven times and holding** — the lists of 7, 8, 9, 10, 11, 12 and 13 August have
  arrived since the threshold was printed; certain is 11, not more than 11, and `share_fixed` is
  `–100 %` at every stop.
- **The fold breakdown, exactly.** `fold.mjs` → 130, exit 1. Per element at ≤480 px: controls **70**,
  run's line **60** (= 130); figure **70**, hole's heading **50** — total **250** if they counted.
  On the HEAD page: 108 = 54 + 54, six and six on nine stops, as the README says.
- **The frame span.** 281 px / 24 of 31 chips now; **273 px / 24 of 24** on the HEAD page; **266 px /
  22 of 31 — UNDER** on the reconstructed pre-cut page. 328 of 844 and 591 of 900.
- **`gaps.mjs`** — 0 of 42 rows failing, own 1.42 px / next 9.59 px, axis 0 collisions at all seven
  widths, 4 labels below 700 px and 10 at and above, tightest 12.57 px. `tiers.mjs` passes.
  `announce.mjs` — 1 live region, 4 writes in 30 s, 3 spoken, 11 figure rewrites.
- **Every URL, fetched tonight: 13 of 13 return 200.** Verbatim present: the seven-day window quote,
  *"The index counts all examined; the case and list show named vessels."*, *"case of the day by
  region brisance, then duration"*, *"each individual has an equal probability of being captured"*,
  the `>=3 datasets` sentence, Brysbaert's **238 wpm for non-fiction** (56 words → 14,118 ms ✓), both
  bitforms quotations, and Cennetoğlu's 34,361-death caption in full.
- **The atlas.** `count: 505` ✓. Ọnụọha at entries 197, 201, 202 and *Sobrevivientes* at 199 — all
  0-based, all correct; entry 202 carries *"People excluded from housing due to criminal records"*
  verbatim; entry 199 carries the title, the year and *survivor testimony*, none of which are on the
  page that section says lacks them. Cennetoğlu, Hoover Green, HRDAG, multiple systems, Forensic
  Oceanography, left-to-die: **0 hits each.**
- **`189 to 265` examined and `six to eleven` names** across the ten lists ✓; `230 / 82 / 5,641` on
  the 4 August list ✓; `thirty-one later, twenty-two reaching back, nine ruled out` ✓;
  `twenty-six after this page printed its figure` ✓ (1+3+5+6+2+2+7).
- **Banked 17 correctly named** — `e4cb780` entry 17 ends *"A constant advanced by hand is a number
  typed by hand wearing a variable's name"*; it stands twice already in `data.py` (lines 75, 1294),
  so "a third place" holds.

---

**Opening hash:** `a7912784ae540e2e11ba6fcb2227af8510eb6632004b03bd6a0823f59dec7aee`
**Closing hash:** `a7912784ae540e2e11ba6fcb2227af8510eb6632004b03bd6a0823f59dec7aee`
Unmoved. HEAD `b619af4`, unmoved. No file was written by this pass except this memo.
