# USB control and firmware plan

This document specifies the Rev A firmware interface. It is a design specification; no flashed-board execution is recorded.

## Commands

USB CDC carries one JSON command per line. Replies include the command name, success/error status and the active configuration. The board starts idle after reset and applies configuration changes between bursts.

| Command | Purpose |
|---|---|
| `configure` | Set modulation, chip rate, samples/chip, spreading length and amplitude |
| `pn` | Set LFSR order, taps, nonzero seed and phase, or upload a custom binary chip sequence |
| `payload` | Upload a bit string, hexadecimal bytes or UTF-8 text; select a repeating test pattern |
| `frame` | Set preamble, CRC, repeat count and inter-frame gap |
| `tx` | Start or stop transmission; report samples and frames sent |
| `capture` | Return a bounded dual-ADC capture with sample rate and channel metadata |
| `status` | Return configuration, DMA underruns/overruns and frame counters |
| `loopback` | Compare a known transmitted pattern with captured I/Q after host synchronization |

Example configuration:

```json
{"command":"configure","modulation":"qpsk","chip_rate_hz":25000,"samples_per_chip":4,"spreading_length":127,"amplitude":0.6}
{"command":"pn","order":7,"taps":[7,6],"seed":1,"phase":0}
{"command":"payload","encoding":"bits","data":"1011001010110001"}
{"command":"tx","action":"start","frames":100}
```

The taps use polynomial exponents: `[7,6]` represents x⁷ + x⁶ + 1. Firmware must define the shift direction and output stage, and publish sequence vectors before comparing this mode with the existing inverted-feedback model. Arbitrary taps can produce short cycles; only verified maximal polynomials should be labelled PRBS.

## Modes

| Mode | Mapping | I/Q outputs |
|---|---|---|
| BPSK | Chip 0 → +1; chip 1 → −1 | I carries the bipolar chip waveform; Q stays at the bias level |
| QPSK | Gray mapping: 00 → (+,+), 01 → (+,−), 11 → (−,−), 10 → (−,+), normalized by √2 | Consecutive spread-chip pairs drive I and Q |
| OOK | Chip 0 → off; chip 1 → on | I carries the unipolar waveform; Q stays at bias |
| 2-FSK | Chip chooses f₀ or f₁; phase accumulator continues across chip boundaries | I/Q carry the complex baseband oscillator |

Digital symbols are converted to unsigned DAC samples around a mid-supply bias. Requested amplitude must leave buffer and DAC headroom. Chip rate counts spread chips before QPSK pairing; QPSK symbol rate is half the chip rate. An odd chip count is padded explicitly and its original length retained.

## Frame format

`preamble | payload length | payload | CRC32`

The preamble, length endianness and CRC polynomial/initialization belong in shared golden vectors. Raw mode bypasses framing for continuous code and logic measurements. A repeating payload is useful for eye diagrams; a PRBS payload is useful for error-rate tests.

## Firmware structure

1. Configure clocks, USB CDC, SWD, GPIO and the analogue peripherals. Use HSI48 with USB SOF clock recovery for USB; configure the HSE/PLL separately for processing and timers.
2. Generate payload bits, PN chips and mapped symbols into bounded ping-pong buffers. Use DMA to stream packed dual-DAC samples under a shared timer trigger.
3. Configure ADC1/ADC2 with simultaneous sampling, timer triggering and DMA. Confirm trigger routing and sampling-time settings against the STM32G4 reference manual.
4. Use the digital header for chip/data/PN/frame observations. Keep the GPIO waveform schedule synchronized with the sample timer.
5. Detect underruns and overruns, stop cleanly on error, and apply configuration changes at buffer or frame boundaries.
6. Implement a host receiver for correlation, code-phase search, symbol decisions and CRC/BER comparison. Later move selected receiver stages onto the MCU after profiling.

Initial analogue target: 25 kchip/s, four samples/chip, 100 ksample/s per DAC channel. Buffer memory, USB throughput, ADC capture bandwidth and interrupt load determine higher-rate operation.

## Useful extensions

- Uploaded PN sequences and Gold-code pairs for code-division experiments.
- Adjustable gain/phase mismatch in the transmitted I/Q waveform.
- Repeated frames with controlled code phase for acquisition sweeps.
- SPI-connected display, RF conversion module or programmable attenuator.
- Code and modulation profiles stored in flash with a configuration checksum.
