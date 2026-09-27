# Implementation overview

This repository follows one signal chain from a laboratory spread-spectrum transceiver through a configurable board design to reproducible receiver experiments.

| Layer | Engineering work | Explore |
|---|---|---|
| Laboratory transceiver | 2 MHz carrier and chip clock, seven-stage PN generation, logic spreading, analogue demodulation, clock alignment and recovered data captures | [Build photographs and waveforms](../hardware/README.md) |
| Configurable Rev A | Four-layer routed PCB with an STM32G474, USB control, dual I/Q DAC outputs, protected I/Q inputs, SWD, expansion and front-panel controls | [Schematic, board renders, BOM and interface](../hardware/configurable/README.md) |
| DSSS modelling | Exact PN recurrence, energy-normalized BPSK, packet framing, acquisition, pulse shaping, interference, fading and front-end impairments | [Methods](methodology.md) · [Results](results.md) |
| CDMA extension | Code families, four-user composite waveform, chip-phase and near–far sweeps, matched/decorrelating/MMSE receivers and desired-user BER | [Architecture and results](cdma.md) |
| Interactive study | Browser-based exploration of code correlation, near–far loading and multiuser receiver decisions | [CDMA explorer](../visualizer/index.html) |

The MATLAB and Python implementations share deterministic test vectors. Their random streams are independent; numerical sweeps are compared by conditions and statistics rather than sample identity. The [validation workflow](../.github/workflows/validate.yml) runs the Python suite and Octave experiments; the separate [MATLAB workflow](../.github/workflows/matlab.yml) validates the native MATLAB path.

The original bench circuit, Rev A PCB and simulation models are different engineering stages. The [hardware page](../hardware/README.md) contains the bench record, while the [Rev A page](../hardware/configurable/README.md) contains its circuit and layout package.
