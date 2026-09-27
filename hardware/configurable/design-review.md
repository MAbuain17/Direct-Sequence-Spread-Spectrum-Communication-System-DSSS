# Rev A design review

## CAD checks

KiCad 10.0.6 checks on 27 September 2026:

| Check | Result |
|---|---|
| Schematic ERC | 0 violations |
| PCB DRC | 0 violations |
| Unconnected PCB items | 0 |
| Layout | Four copper layers; 110 × 80 mm |
| Circuit components / nets | 70 / 48 |

The schematic and PCB use the same component pin map. The USB connector shell is grounded, unused MCU pins are marked unconnected, and the inner ground plane connects the analogue and digital return paths. Local ground pours also cover the outer copper layers.

Default signal clearance is 0.15 mm. Escape vias use 0.45 mm pads and 0.20 mm drills. The USB-C footprint has a specific 0.18 mm pad-to-locating-hole clearance rule to accommodate its standard library geometry; confirm that geometry and tolerances with the board supplier.

Machine-readable counts are recorded in [design-checks.json](design-checks.json).

## Engineering review before a prototype

- Confirm the ordered MCU, regulator, USB connector, crystal and SMA part numbers against their footprints and data sheets.
- Review USB D+/D− routing, return continuity and signal integrity at full-speed USB; the existing traces are connected but do not constitute an impedance-controlled transmission-line specification.
- Check USB current budget, AP2112 thermal dissipation, PTC hold current, ferrite current rating and analogue-rail noise.
- Confirm the crystal load and drive settings. The 15 pF capacitor choice assumes approximately 2.5 pF total stray capacitance for a 10 pF load target; adjust for the selected crystal and board.
- Check DAC output headroom, buffer stability, input clamp leakage and the RC response at each intended sample/chip rate.
- Verify boot/reset options, USB clock recovery, timer trigger selection, dual-ADC sampling and DMA buffer timing in firmware.
- Review layer stack-up, minimum drill capability, annular rings, assembly access and connector mechanical fit with the manufacturer.

## Development stage

Rev A is a connected schematic and routed PCB design. Firmware implementation, fabrication and physical measurements are subsequent milestones. The existing laboratory photographs document the earlier bench implementation.
