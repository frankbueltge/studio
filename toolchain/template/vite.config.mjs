// House build contract (SITE-API.md "Built works"): deterministic, self-contained,
// relative paths, everything not .html/.js/.css/.json/.svg inlined as data: URIs,
// never wipe the project top level. See toolchain/README.md for the rationale per line.
import { defineConfig } from 'vite'

export default defineConfig({
  base: './',
  build: {
    outDir: '..',
    emptyOutDir: false,
    assetsInlineLimit: Number.MAX_SAFE_INTEGER,
    cssCodeSplit: false,
    rollupOptions: {
      output: {
        entryFileNames: 'bundle.js',
        chunkFileNames: '[name].js',
        assetFileNames: '[name][extname]',
      },
    },
  },
})
