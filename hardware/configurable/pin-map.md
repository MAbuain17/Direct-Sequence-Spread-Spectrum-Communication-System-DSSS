# Pin map

## STM32G474RET6 — LQFP64

| Function | Pin / port | Board net |
|---|---|---|
| TX I | 18 / PA4, DAC1_OUT1 | DAC_I |
| TX Q | 19 / PA5, DAC1_OUT2 | DAC_Q |
| RX I | 8 / PC0, ADC1_IN6 | ADC_I |
| RX Q | 9 / PC1, ADC2_IN7 | ADC_Q |
| USB D− / D+ | 45 / PA11, 46 / PA12 | USB_DM_MCU / USB_DP_MCU |
| HSE crystal | 5 / PF0, 6 / PF1 | HSE_IN / HSE_OUT |
| Reset | 7 / PG10-NRST | NRST |
| Debug | 49 / PA13, 50 / PA14, 56 / PB3 | SWDIO / SWCLK / SWO |
| Chip clock | 42 / PA8 | CHIP_CLK |
| Data / PN | 59 / PB6, 60 / PB7 | DATA_OUT / PN_OUT |
| Frame marker | 38 / PC6 | FRAME |
| SPI2 | 34 / PB12, 35 / PB13, 36 / PB14, 37 / PB15 | SPI_CS / SPI_SCK / SPI_MISO / SPI_MOSI |
| USART2 | 14 / PA2, 17 / PA3 | UART_TX / UART_RX |
| Buttons | 2 / PC13, 3 / PC14 | BTN_MODE / BTN_USER |
| Indicators | 24 / PB0, 25 / PB1 | LED_TX / LED_RX |
| Boot selection | 61 / PB8-BOOT0 | BOOT0 |

The pin assignments are based on the [ST datasheet](https://www.st.com/resource/en/datasheet/stm32g474re.pdf). Firmware must configure alternate functions and the boot option bytes for the selected usage.

## Connectors

| Connector | Odd pins | Even pins |
|---|---|---|
| J6 SWD, 2 × 5 at 1.27 mm | 1: 3.3 V; 3: GND; 5: GND; 7: unused; 9: GND | 2: SWDIO; 4: SWCLK; 6: SWO; 8: unused; 10: NRST |
| J7 digital, 2 × 5 at 2.54 mm | 1: 3.3 V; 3: chip clock; 5: data; 7: PN; 9: frame | Ground on all even pins |
| J8 expansion, 2 × 4 at 2.54 mm | 1: 3.3 V; 3: SPI CS; 5: MOSI; 7: UART TX | 2: GND; 4: SPI SCK; 6: MISO; 8: UART RX |

J2/J3 are TX I/Q; J4/J5 are RX I/Q. All SMA shells connect to ground. JP1 connects BOOT0 to 3.3 V; R6 holds it low with the jumper removed.

All digital expansion signals use 3.3 V logic. The USB port is the board's power input.
