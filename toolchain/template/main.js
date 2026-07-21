import './style.css'

// The island is the single source of runtime data — byte-identical to ../data.json.
// The works CSP forbids fetch; everything ships in the files.
const data = JSON.parse(document.getElementById('data-island').textContent)

// House RNG — mulberry32. Same seed, same work (print the seed on the work's face).
export function mulberry32(seed) {
  return function () {
    seed |= 0
    seed = (seed + 0x6d2b79f5) | 0
    let t = Math.imul(seed ^ (seed >>> 15), 1 | seed)
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296
  }
}

const root = document.querySelector('.work-root')
root.textContent = `template running — ${Object.keys(data).length} data key(s) loaded`
