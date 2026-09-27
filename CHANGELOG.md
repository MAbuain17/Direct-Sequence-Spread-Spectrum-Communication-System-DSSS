# Changelog

## CDMA receiver study — 28 September 2026

- Added a four-user direct-sequence CDMA model with Walsh and PN-shift signatures, chip-phase offsets and controlled near–far power.
- Added matched-filter, decorrelating and linear MMSE detection with deterministic receiver tests.
- Published the 45-condition BER sweep, comparison figure and browser-based signal explorer.
- Recast the implementation and historical-report notes around architecture and measurement conventions.

## Rev A hardware design — 27 September 2026

- Added a connected STM32G474 schematic and four-layer PCB for configurable I/Q experiments.
- Added USB-C, dual transmit/receive channels, analogue filtering and protection, SWD, expansion headers and test points.
- Added the BOM, pin map, PCB renders and configurable payload/PN/modulation interface specification.
- Updated the project overview to lead with the Rev A architecture.

## Documentation update — 27 September 2026

- Reworked the README and supporting pages around the circuit, laboratory captures and simulation results.
- Added the December 1986 QEX issue and linked its source article.
- Removed internal CV preparation and source-archive inventory pages.

## 0.1.1 — publication and CI maintenance

- Published the complete project repository with source code, evidence, datasets and generated figures.
- Passed the Python and GNU Octave jobs in GitHub Actions and retained both result artifacts.
- Passed the native MathWorks MATLAB workflow and retained its generated result artifact.
- Updated GitHub-maintained actions to Node.js 24-compatible major versions.
- Scoped automatic native MATLAB runs to relevant implementation, vector and workflow changes.

## 0.1.0 — initial software extension

- Added Python DSSS primitives and MATLAB counterparts with shared deterministic vectors.
- Added AWGN, interference, payload, CRC, acquisition, multipath, fading, near-far, front-end impairment and pulse-shaping studies.
- Added a framed burst receiver that acquires integer delay and grid CFO and corrects phase before decoding.
- Verified the report's inverted-feedback PN recurrence and documented rate/gain corrections.
- Preserved selected individual hardware evidence and source files with QEX attribution.
- Audited historical KiCad files as unrouted; documented the prerequisites for a new board.
- Prepared automated Python/Octave checks and a manual native MATLAB workflow.
