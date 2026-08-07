#!/usr/bin/env bash
# selftest.sh — a stranger's proof that both instruments in this directory work.
#
# Exercises tools/prereg.py (freeze / verify / break-seal) and
# tools/record_words.py (the word-ceiling measurement) end to end in a
# throwaway temp directory, and checks the real manifest against the real
# repository. Prints SELFTEST PASSED and exits 0 only if every assertion
# holds; otherwise prints which assertion failed and exits 1.

set -u

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PREREG="$SCRIPT_DIR/prereg.py"
RECORD_WORDS="$SCRIPT_DIR/record_words.py"

TMPDIR="$(mktemp -d)"
cleanup() {
  rm -rf "$TMPDIR"
}
trap cleanup EXIT

fail() {
  echo "SELFTEST FAILED: $1"
  exit 1
}

# --- 1. create a file ---
TARGET="$TMPDIR/panel-memo.md"
printf 'Q1: does it hold? pass mark: yes\nQ2: does it move? pass mark: no\n' > "$TARGET"

# --- 2. freeze it ---
python3 "$PREREG" freeze "$TARGET" > "$TMPDIR/freeze1.out" 2>&1
rc=$?
[ "$rc" -eq 0 ] || fail "freeze on a fresh file did not exit 0 (got $rc); output: $(cat "$TMPDIR/freeze1.out")"
[ -f "$TARGET.frozen" ] || fail "freeze did not create the sidecar $TARGET.frozen"

# --- 3. verify UNMOVED ---
python3 "$PREREG" verify "$TARGET" > "$TMPDIR/verify1.out" 2>&1
rc=$?
[ "$rc" -eq 0 ] || fail "verify on an untouched frozen file did not exit 0 (got $rc); output: $(cat "$TMPDIR/verify1.out")"
grep -q "UNMOVED" "$TMPDIR/verify1.out" || fail "verify on an untouched frozen file did not print UNMOVED"

# --- 4. modify it, verify MOVED, assert exit 1 ---
printf 'Q1: does it hold? pass mark: yes\nQ2: does it move? pass mark: YES, CHANGED\n' > "$TARGET"
python3 "$PREREG" verify "$TARGET" > "$TMPDIR/verify2.out" 2>&1
rc=$?
[ "$rc" -eq 1 ] || fail "verify on a modified frozen file did not exit 1 (got $rc); output: $(cat "$TMPDIR/verify2.out")"
grep -q "MOVED" "$TMPDIR/verify2.out" || fail "verify on a modified frozen file did not print MOVED"

# --- 5. second freeze without --break-seal is refused with exit 3 ---
python3 "$PREREG" freeze "$TARGET" > "$TMPDIR/freeze2.out" 2>&1
rc=$?
[ "$rc" -eq 3 ] || fail "second freeze without --break-seal did not exit 3 (got $rc); output: $(cat "$TMPDIR/freeze2.out")"
grep -q -- "--break-seal" "$TMPDIR/freeze2.out" || fail "refused freeze did not mention --break-seal"

ORIGINAL_STANZA_BEFORE="$(cat "$TARGET.frozen")"

# --- 6. --break-seal appends and leaves the original stanza intact ---
python3 "$PREREG" freeze "$TARGET" --break-seal > "$TMPDIR/freeze3.out" 2>&1
rc=$?
[ "$rc" -eq 0 ] || fail "freeze --break-seal did not exit 0 (got $rc); output: $(cat "$TMPDIR/freeze3.out")"
grep -q "SEAL BROKEN" "$TMPDIR/freeze3.out" || fail "freeze --break-seal did not report SEAL BROKEN"

AFTER_CONTENT="$(cat "$TARGET.frozen")"
case "$AFTER_CONTENT" in
  "$ORIGINAL_STANZA_BEFORE"*) : ;;
  *) fail "the original freeze stanza was not preserved intact as a prefix after --break-seal" ;;
esac
[ "${#AFTER_CONTENT}" -gt "${#ORIGINAL_STANZA_BEFORE}" ] || fail "--break-seal did not append new content to the sidecar"

# verify now shows UNMOVED (current bytes match the newest hash is irrelevant;
# verify checks against the FIRST stanza, and the file is still the changed
# version from step 4, so it must still report MOVED against the first seal)
python3 "$PREREG" verify "$TARGET" > "$TMPDIR/verify3.out" 2>&1
rc=$?
[ "$rc" -eq 1 ] || fail "verify after break-seal did not still report MOVED against the FIRST stanza (got exit $rc)"
grep -q "broken seals:   1" "$TMPDIR/verify3.out" || fail "verify after one break-seal did not report 1 broken seal"

# --- 7. verify on an unfrozen file exits 2 ---
UNFROZEN="$TMPDIR/unfrozen.md"
printf 'never frozen\n' > "$UNFROZEN"
python3 "$PREREG" verify "$UNFROZEN" > "$TMPDIR/verify4.out" 2>&1
rc=$?
[ "$rc" -eq 2 ] || fail "verify on an unfrozen file did not exit 2 (got $rc); output: $(cat "$TMPDIR/verify4.out")"

# --- 8. record_words.py against the real manifest ---
RECORD_OUT="$TMPDIR/record.out"
( cd "$REPO_ROOT" && python3 "$RECORD_WORDS" > "$RECORD_OUT" 2>&1 )
rc=$?
if [ "$rc" -ne 0 ] && [ "$rc" -ne 1 ]; then
  fail "record_words.py against the real manifest exited $rc (expected 0 or 1); output: $(cat "$RECORD_OUT")"
fi
grep -q "STANDING INSTRUMENT" "$RECORD_OUT" || fail "record_words.py output did not label the standing instrument"
grep -q "reference only" "$RECORD_OUT" || fail "record_words.py output did not print the reference-only figure"

echo "SELFTEST PASSED"
exit 0
