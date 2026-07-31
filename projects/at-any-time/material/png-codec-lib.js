// Minimal, from-scratch PNG decoder/encoder using ONLY Node's built-in
// `zlib` module — no external image library of any kind (this environment
// was checked and has none: no PIL/Pillow, no cwebp/pngquant/optipng/
// ImageMagick/graphicsmagick, no sharp/jimp/pngjs under NODE_PATH — see
// MEASUREMENTS-A4-AND-PAGECOUNTS.md for the full inventory). Every byte of
// every encoded file this library produces is accounted for: IHDR + (PLTE
// for indexed images) + IDAT (raw scanlines, PNG filtering, then
// zlib.deflateSync) + IEND, per the PNG spec (ISO/IEC 15948).
//
// Supports exactly the color types this measurement needs:
//   decode: color type 6 (RGBA8), no interlace — what Chromium's own
//           canvas.toDataURL('image/png') produces (verified empirically).
//   encode: color type 0 (grayscale, bit depth 1/2/4/8),
//           color type 2 (RGB, bit depth 8),
//           color type 3 (indexed/palette, bit depth 1/2/4/8),
//           color type 6 (RGBA, bit depth 8) — for round-trip verification.
//
// Filtering: 8-bit-per-channel images use PNG's standard adaptive
// per-scanline filter selection (try all five filter types, keep whichever
// minimises the sum of absolute byte values — the same "minimum sum of
// absolute differences" heuristic libpng documents as its default).
// Sub-byte bit depths (1/2/4, used only for color types 0 and 3) use filter
// type 0 (None) throughout, per the PNG spec's own recommendation that
// filtering rarely helps below 8 bits/sample and Paeth/Sub/Up are defined
// in terms of whole bytes-per-pixel that don't exist at these depths.
// zlib.deflateSync is always called at level 9 (max compression).

const zlib = require('zlib');

const CRC_TABLE = (() => {
  const table = new Uint32Array(256);
  for (let n = 0; n < 256; n++) {
    let c = n;
    for (let k = 0; k < 8; k++) c = c & 1 ? 0xedb88320 ^ (c >>> 1) : c >>> 1;
    table[n] = c >>> 0;
  }
  return table;
})();

function crc32(buf) {
  let c = 0xffffffff;
  for (let i = 0; i < buf.length; i++) c = CRC_TABLE[(c ^ buf[i]) & 0xff] ^ (c >>> 8);
  return (c ^ 0xffffffff) >>> 0;
}

function chunk(type, data) {
  const len = Buffer.alloc(4);
  len.writeUInt32BE(data.length, 0);
  const typeBuf = Buffer.from(type, 'ascii');
  const crcBuf = Buffer.alloc(4);
  crcBuf.writeUInt32BE(crc32(Buffer.concat([typeBuf, data])), 0);
  return Buffer.concat([len, typeBuf, data, crcBuf]);
}

const PNG_SIG = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);

function decodePng(buf) {
  if (!buf.slice(0, 8).equals(PNG_SIG)) throw new Error('not a PNG (bad signature)');
  let off = 8;
  let width, height, bitDepth, colorType, interlace;
  const idatChunks = [];
  while (off < buf.length) {
    const len = buf.readUInt32BE(off);
    const type = buf.toString('ascii', off + 4, off + 8);
    const data = buf.slice(off + 8, off + 8 + len);
    if (type === 'IHDR') {
      width = data.readUInt32BE(0);
      height = data.readUInt32BE(4);
      bitDepth = data.readUInt8(8);
      colorType = data.readUInt8(9);
      interlace = data.readUInt8(12);
    } else if (type === 'IDAT') {
      idatChunks.push(data);
    }
    off += 8 + len + 4;
  }
  if (interlace !== 0) throw new Error('interlaced PNG not supported (not needed by this pipeline)');
  if (!(colorType === 6 && bitDepth === 8)) {
    throw new Error(`decodePng only supports colorType 6 / bitDepth 8 (got colorType=${colorType} bitDepth=${bitDepth})`);
  }
  const raw = zlib.inflateSync(Buffer.concat(idatChunks));
  const channels = 4;
  const bpp = channels; // 1 byte/channel * 4 channels
  const rowBytes = width * channels;
  const out = Buffer.alloc(rowBytes * height);
  let inOff = 0;
  for (let y = 0; y < height; y++) {
    const filterType = raw[inOff]; inOff += 1;
    const rowStart = y * rowBytes;
    const prevStart = (y - 1) * rowBytes;
    for (let x = 0; x < rowBytes; x++) {
      const rawByte = raw[inOff + x];
      const a = x >= bpp ? out[rowStart + x - bpp] : 0;
      const b = y > 0 ? out[prevStart + x] : 0;
      const c = (y > 0 && x >= bpp) ? out[prevStart + x - bpp] : 0;
      let val;
      switch (filterType) {
        case 0: val = rawByte; break;
        case 1: val = (rawByte + a) & 0xff; break;
        case 2: val = (rawByte + b) & 0xff; break;
        case 3: val = (rawByte + ((a + b) >> 1)) & 0xff; break;
        case 4: {
          const p = a + b - c;
          const pa = Math.abs(p - a), pb = Math.abs(p - b), pc = Math.abs(p - c);
          const pr = (pa <= pb && pa <= pc) ? a : (pb <= pc ? b : c);
          val = (rawByte + pr) & 0xff;
          break;
        }
        default: throw new Error('bad filter type ' + filterType);
      }
      out[rowStart + x] = val;
    }
    inOff += rowBytes;
  }
  return { width, height, bitDepth, colorType, channels, pixels: out };
}

// Apply PNG's per-scanline filtering (adaptive, min-sum-of-abs heuristic)
// to 8-bit-per-sample data with `bpp` bytes per pixel, then deflate.
function filterAndCompress8bit(pixels, width, height, bpp) {
  const rowBytes = width * bpp;
  const filtered = Buffer.alloc((rowBytes + 1) * height);
  let outOff = 0;
  const tmp = [Buffer.alloc(rowBytes), Buffer.alloc(rowBytes), Buffer.alloc(rowBytes), Buffer.alloc(rowBytes), Buffer.alloc(rowBytes)];
  for (let y = 0; y < height; y++) {
    const rowStart = y * rowBytes;
    const prevStart = (y - 1) * rowBytes;
    for (let ftype = 0; ftype < 5; ftype++) {
      const rowBuf = tmp[ftype];
      for (let x = 0; x < rowBytes; x++) {
        const raw = pixels[rowStart + x];
        const a = x >= bpp ? pixels[rowStart + x - bpp] : 0;
        const b = y > 0 ? pixels[prevStart + x] : 0;
        const c = (y > 0 && x >= bpp) ? pixels[prevStart + x - bpp] : 0;
        let v;
        switch (ftype) {
          case 0: v = raw; break;
          case 1: v = (raw - a) & 0xff; break;
          case 2: v = (raw - b) & 0xff; break;
          case 3: v = (raw - ((a + b) >> 1)) & 0xff; break;
          case 4: {
            const p = a + b - c;
            const pa = Math.abs(p - a), pb = Math.abs(p - b), pc = Math.abs(p - c);
            const pr = (pa <= pb && pa <= pc) ? a : (pb <= pc ? b : c);
            v = (raw - pr) & 0xff;
            break;
          }
        }
        rowBuf[x] = v;
      }
    }
    // pick filter with minimum sum of absolute (signed-byte) values
    let bestFtype = 0, bestSum = Infinity;
    for (let ftype = 0; ftype < 5; ftype++) {
      let sum = 0;
      const rowBuf = tmp[ftype];
      for (let x = 0; x < rowBytes; x++) {
        const v = rowBuf[x];
        sum += v < 128 ? v : 256 - v;
      }
      if (sum < bestSum) { bestSum = sum; bestFtype = ftype; }
    }
    filtered[outOff] = bestFtype; outOff += 1;
    tmp[bestFtype].copy(filtered, outOff);
    outOff += rowBytes;
  }
  return zlib.deflateSync(filtered, { level: 9 });
}

// Sub-8-bit depths: filter type None throughout (per spec guidance), rows
// are pre-packed into their final bit-packed byte layout by the caller.
function noneFilterAndCompress(packedRows, rowBytes, height) {
  const filtered = Buffer.alloc((rowBytes + 1) * height);
  let outOff = 0;
  for (let y = 0; y < height; y++) {
    filtered[outOff] = 0; outOff += 1;
    packedRows.copy(filtered, outOff, y * rowBytes, (y + 1) * rowBytes);
    outOff += rowBytes;
  }
  return zlib.deflateSync(filtered, { level: 9 });
}

function makeIHDR(width, height, bitDepth, colorType) {
  const d = Buffer.alloc(13);
  d.writeUInt32BE(width, 0);
  d.writeUInt32BE(height, 4);
  d.writeUInt8(bitDepth, 8);
  d.writeUInt8(colorType, 9);
  d.writeUInt8(0, 10); // compression method
  d.writeUInt8(0, 11); // filter method
  d.writeUInt8(0, 12); // interlace method
  return chunk('IHDR', d);
}

function assemble(chunks) {
  return Buffer.concat([PNG_SIG, ...chunks, chunk('IEND', Buffer.alloc(0))]);
}

// Encode 8-bit grayscale (color type 0) from a Uint8/Buffer array of one
// luminance byte per pixel (caller has already computed luminance).
function encodeGray8(width, height, grayBytes) {
  const idat = filterAndCompress8bit(grayBytes, width, height, 1);
  return assemble([makeIHDR(width, height, 8, 0), chunk('IDAT', idat)]);
}

// Encode RGB8 (color type 2) from interleaved R,G,B bytes (alpha dropped).
function encodeRGB8(width, height, rgbBytes) {
  const idat = filterAndCompress8bit(rgbBytes, width, height, 3);
  return assemble([makeIHDR(width, height, 8, 2), chunk('IDAT', idat)]);
}

// Encode RGBA8 (color type 6), for round-trip self-verification.
function encodeRGBA8(width, height, rgbaBytes) {
  const idat = filterAndCompress8bit(rgbaBytes, width, height, 4);
  return assemble([makeIHDR(width, height, 8, 6), chunk('IDAT', idat)]);
}

// Encode indexed/palette (color type 3). `indices` is one palette-index
// byte per pixel (0..palette.length-1); `palette` is an array of [r,g,b].
// bitDepth is chosen by the caller (1/2/4/8) based on palette.length.
function encodeIndexed(width, height, indices, palette, bitDepth) {
  const plte = Buffer.alloc(palette.length * 3);
  palette.forEach(([r, g, b], i) => { plte[i * 3] = r; plte[i * 3 + 1] = g; plte[i * 3 + 2] = b; });

  let idat;
  if (bitDepth === 8) {
    idat = filterAndCompress8bit(indices, width, height, 1);
  } else {
    const perByte = 8 / bitDepth;
    const rowBytes = Math.ceil(width / perByte);
    const packed = Buffer.alloc(rowBytes * height);
    for (let y = 0; y < height; y++) {
      for (let x = 0; x < width; x++) {
        const v = indices[y * width + x];
        const bitOff = (x % perByte) * bitDepth;
        const shift = 8 - bitDepth - bitOff;
        packed[y * rowBytes + Math.floor(x / perByte)] |= (v << shift);
      }
    }
    idat = noneFilterAndCompress(packed, rowBytes, height);
  }
  return assemble([
    makeIHDR(width, height, bitDepth, 3),
    chunk('PLTE', plte),
    chunk('IDAT', idat),
  ]);
}

// Encode 1-bit grayscale (color type 0, bit depth 1) from a 0/1-per-pixel
// array (caller has already thresholded).
function encodeBilevel1(width, height, bits) {
  const rowBytes = Math.ceil(width / 8);
  const packed = Buffer.alloc(rowBytes * height);
  for (let y = 0; y < height; y++) {
    for (let x = 0; x < width; x++) {
      const v = bits[y * width + x];
      if (v) packed[y * rowBytes + (x >> 3)] |= (0x80 >> (x & 7));
    }
  }
  const idat = noneFilterAndCompress(packed, rowBytes, height);
  return assemble([makeIHDR(width, height, 1, 0), chunk('IDAT', idat)]);
}

module.exports = {
  decodePng, encodeGray8, encodeRGB8, encodeRGBA8, encodeIndexed, encodeBilevel1,
};
