# Engineering notes on the original report

The [original laboratory report](original-report.pdf) records the circuit, test setup and observed waveforms. The following conventions make its measurements easier to interpret alongside the newer models.

## Clock, data and spreading

The circuit uses seven active stages of an eight-stage 74164 register. Its XNOR feedback has a 127-chip period; the all-zero start state is valid and the all-one state is fixed. At a 2 Mchip/s clock, a 1,000-chip data-clock interval lasts 500 µs. The direct 2 kHz square-wave input has 500 chips in each high or low interval. These are two distinct test configurations, so code period, data interval and square-wave fundamental are kept separate in the model.

The ratios of 1,000 and 500 chips per interval correspond to 30.0 and 27.0 dB, respectively, when expressed as `10 log10(chips/interval)`. They describe nominal spreading ratios. The [simulation study](results.md) evaluates error rates under stated interference conditions; it does not use those ratios as measured receiver gain.

## Signal path and synchronization

The recorded bench connection carries the transmitter output to the receiver through a wired path with a shared reference. The logic trace reproduces PN generation, spreading and carrier XOR operations. The communications receiver adds preamble correlation and a finite delay/CFO search; its acquisition results are recorded separately from the bench observations.

The synchronization indicator reflects the clock-switch logic state. Timing quality in the newer model is evaluated from correlation peaks and decoded-frame checks. A PN sequence also provides code separation, while payload confidentiality requires a separate cryptographic layer.

## Design lineage

The underlying 1986 circuit is credited in [design references](attribution.md). The [Rev A board](../hardware/configurable/README.md) develops a different, programmable baseband architecture, with its own routed PCB, bill of materials and design checks. The original source files remain available with the report as the laboratory record.
