# References and source check

> This brook lite version was derived from the groundwater lite version; [R4] and [R18] (ADS1115) are kept for reference only, the ADS1115 is not used here. The node uses 869.525 MHz, in the 869.40-869.65 MHz sub-band, which has a 10 % duty-cycle limit (the same band as the full brook station on `main`); [R25] covers the 868.0-868.6 MHz sub-band, so check the 869.4 MHz row of ERC Rec. 70-03 for your country.

Every technical claim in this repository that comes from outside the project is listed here with the source it
was checked against. In the YAML files and docs, `[R#]` points to the entries below.

*Checked on 17 November 2026.* "Read" means the page or document was opened and the quoted facts were found in it;
"Seen in search" means only a search snippet was available. ESPHome behaviour was also tested by running
`esphome config` (ESPHome 2026.10.2) on every YAML file in this repository. **Nothing here replaces a bench test:**
the firmware has not been run on hardware.

## 1. ESPHome (firmware behaviour)

| ID | Source | Used for | Checked |
| :-- | :-- | :-- | :-- |
| R1 | [`sx126x` component](https://esphome.io/components/sx126x/) | Required options (`hw_version`, `modulation`, `rf_switch`), `pa_power` (-3 to 22 dBm on SX1262), `coding_rate: CR_4_5`, `tcxo_voltage` / `tcxo_delay`, `crc_enable`, `sync_value` | Read |
| R2 | [`packet_transport`](https://esphome.io/components/packet_transport/) | `update_interval` (default 15 s), `encryption` (any string, hashed; per provider), `providers`, `broadcast_id`, `rolling_code_enable` | Read. The page does not define `remote_id` or `internal`; those were verified with R9 |
| R3 | [`adc` sensor](https://esphome.io/components/sensor/adc/) | `attenuation`, `samples`, `sampling_mode`; usable range about 0.075 to 3.12 V (clamped outside); no accuracy figure given for the S3 | Read |
| R4 | [`ads1115`](https://esphome.io/components/sensor/ads1115/) | Address 0x48 (ADDR to GND), `multiplexer: A0_A1`, `gain` values, `sample_rate` values (8 to 860, default 860) | Read |
| R5 | [`bme280`](https://esphome.io/components/sensor/bme280/) | Platform `bme280_i2c`; address 0x77 default or 0x76; oversampling options | Read |
| R6 | [`http_request`](https://esphome.io/components/http_request/) | The option is `request_headers` (not `headers`); `on_error` runs only when the request cannot complete, **not** for non-200 responses; `timeout`, `watchdog_timeout` | Read |
| R7 | [`deep_sleep`](https://esphome.io/components/deep_sleep/) | `sleep_duration` is templatable in ms; the device does not respond to the network while asleep (so no OTA); the page does **not** say what GPIO levels do during sleep | Read |
| R8 | [`dallas_temp`](https://esphome.io/components/sensor/dallas_temp/) | Resolution 9 to 12 bit (default 12), `update_interval`; the page says nothing about conversion time or read failures | Read |
| R9 | ESPHome 2026.10.2 `esphome config` | Everything the pages above do not cover: `internal: false` is required on named `packet_transport` sensors; the gateway key goes under each provider; `sample_duration` is not an `adc` option; `headers` was renamed | Run on all configs |

## 2. Heltec WiFi LoRa 32 V3 (board)

| ID | Source | Used for | Checked |
| :-- | :-- | :-- | :-- |
| R10 | [ESPHome device page: Heltec WiFi LoRa 32 V3](https://devices.esphome.io/devices/heltec-wifi-lora-32-v3/) | SX1262 pins (SPI 9/10/11, CS 8, DIO1 14, BUSY 13, RST 12), `rf_switch: true`, `tcxo_voltage: 1_8V`, `tcxo_delay: 5ms`, ESP-IDF framework, LED GPIO35, battery ADC GPIO1, Vext on GPIO36 (set LOW to enable, `inverted: true`). Its battery example uses `multiply: 2.0` | Read (via search) |
| R11 | [Heltec hardware update log](https://wiki.heltec.org/docs/devices/open-source-hardware/esp32-series/lora-32/wifi-lora-32-v3/hardware-update-log) | V3.2: "Modified voltage detection circuit, now need to pull up the ADC_Ctrl (GPIO 37)", "Vext changed to LDO", new charger chip. V3 and V3.1: no voltage-detection entries | Read |
| R12 | [ESPBoards: Heltec Wireless Stick Lite V3 pinout](https://www.espboards.dev/esp32/heltec-wireless-stick-lite-v3/) | GPIO1 reads the battery through a 390 k / 100 k divider (factor 4.9) while GPIO37 is LOW (same V3 family; a community pinout, not Heltec) | Seen in search |
| R13 | [RNode firmware commit "Fixed reading of battery voltage for Heltec V3.2"](https://git.hackliberty.org/Git-Mirrors/RNode_Firmware/commit/828623c70c21be0deedc7428e655c5ca37e7f814) | "V3 and V3.1 have a pull up on pin_ctrl and are active low; V3.2 has a transistor and active high", and a software test to tell them apart | Read |
| R14 | [Heltec V3.2 schematic](https://resource.heltec.cn/download/WiFi_LoRa_32_V3/WiFi_LoRa_32_V3.2_Schematic_Diagram.pdf) | The authoritative place to confirm `ADC_Ctrl` and `Vext_Ctrl` polarity for your board | **Not read in detail**: check it for your revision |
| R15 | [Heltec WiFi Kit 32 V3 datasheet](https://resource.heltec.cn/download/WiFi_Kit_32_V3/HTIT-WiFi%20kit32_V3(Rev1.1).pdf) | Heltec quotes deep-sleep current below 10 µA for that board (a different board). Real LoRa 32 V3 units are usually higher, so measure yours | Seen in search |

## 3. Microcontroller ADC

| ID | Source | Used for | Checked |
| :-- | :-- | :-- | :-- |
| R16 | [ESP-IDF: ESP32-S3 ADC](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-reference/peripherals/adc/index.html) | 12-bit raw results; reference voltage is designed as 1100 mV but is 1000 to 1200 mV between chips (so calibration matters) | Seen in search |
| R17 | [Espressif ESP-FAQ: ADC](https://docs.espressif.com/projects/esp-faq/en/latest/software-framework/peripherals/adc.html) | With 12 dB attenuation the measurable range is 0 to 3100 mV on the ESP32-S3 | Seen in search |

## 4. Components

| ID | Source | Used for | Checked |
| :-- | :-- | :-- | :-- |
| R18 | [TI ADS1115 datasheet (SBAS444E)](https://www.ti.com/lit/gpn/ads1115) | Analog inputs must stay within GND - 0.3 V to VDD + 0.3 V (ESD diodes turn on otherwise); VDD 2.0 to 5.5 V; 16-bit, programmable gain | Seen in search |
| R19 | [DFRobot SEN0244 wiki](https://wiki.dfrobot.com/sen0244/) | Range 0 to 1000 ppm TDS, accuracy ±10 % of full scale at 25 °C, output 0 to 2.3 V, probe with 2 needles; the sample code uses 1 + 0.02 × (T - 25) for temperature compensation | Read |
| R20 | [MT3608 datasheet (Aerosemi)](https://www.radiolocman.com/datasheet/pdf.html?di=177837) | 2 to 24 V input, output up to 28 V, 4 A switch current limit, internal soft start | Seen in search |
| R21 | TL-136 seller manuals: [Vikye TL-136](https://manuals.plus/asin/B088NKRLP3), [VBESTLIFE TL-136](https://manuals.plus/ae/1005001447225174) | Supply listed as **12 to 32 VDC**, output 4 to 20 mA, 0 to 5 m variant; sellers list accuracy as 0.2 to 0.5 % of full scale. **TL-136 is a generic part with no authoritative datasheet**; check the label or manual of your unit | Seen in search |
| R22 | [Semtech AN1200.13 LoRa Modem Designer's Guide](https://www.mouser.com/pdfdocs/semtech-lora-modem-design.pdf) | Time-on-air formula. Calculated here for SF9, 125 kHz, CR 4/5, 8 preamble symbols, CRC on: 30 B = 226 ms, 50 B = 329 ms, 70 B = 411 ms, 90 B = 513 ms, 110 B = 595 ms | Formula applied by script |
| R23 | [Analog Devices (Maxim) DS18B20](https://www.analog.com/en/products/ds18b20.html) | 12-bit conversion takes up to 750 ms; ±0.5 °C accuracy; 4.7 kΩ pull-up on the data line | Figures confirmed in datasheet copies found by search |
| R24 | [Adafruit BME280 guide](https://learn.adafruit.com/adafruit-bme280-humidity-barometric-pressure-temperature-sensor-breakout) | ±3 % RH, ±1 hPa, ±1 °C; address 0x77 by default, 0x76 with SDO to GND (many cheap modules ship at 0x76) | Seen in search |

## 5. Regulation and cloud service

| ID | Source | Used for | Checked |
| :-- | :-- | :-- | :-- |
| R25 | [rfessentials: EU duty-cycle limits](https://rfessentials.com/rf-knowledge-base/how-does-the-duty-cycle-limitation-in-european-ism-bands-affect-iot-device-desig/), [Saelens et al. 2019, EURASIP JWCN](https://jwcn-eurasipjournals.springeropen.com/track/pdf/10.1186/s13638-019-1502-5) | 868.0 to 868.6 MHz: 1 % duty cycle, 25 mW ERP (14 dBm), under ETSI EN 300 220 and CEPT ERC Rec. 70-03. Duty cycle is band-specific, not a single global 1 % | Secondary sources. **The primary text (ERC Rec. 70-03) was not read**; check your national rules |
| R26 | [openSenseMap security docs](https://en.docs.sensebox.de/opensensemap/opensensemap-security/) | With authentication enabled, every POST must carry the box access token, e.g. `'Authorization' : 'YOUR_BOX_ACCESS_TOKEN'` (no `Bearer` prefix) | Seen in search |
| R27 | [openSenseMap API: post multiple measurements](https://docs.opensensemap.org/#api-Measurements-postNewMeasurements) | `POST /boxes/:boxId/data` with a JSON list of `{sensor, value}` | **Could not be opened here** (blocked); confirmed through a client library and R28 |
| R28 | [senseBox forum: uploading multiple sensors](https://forum.sensebox.de/t/help-uploading-multiple-sensors-data/1654) | Working example of the list format and token header; a wrong URL returns `MethodNotAllowed` | Seen in search |

## 6. Corrections found during this source check

These replace earlier statements in the review report and in earlier versions of this repository.

1. **Battery divider enable polarity depends on the board revision (R11, R13).** V3 and V3.1: GPIO37 LOW connects the divider.
   V3.2: GPIO37 **HIGH**. Earlier versions of this repo always drove it LOW. It is now the substitution `vbat_ctrl_active_low`
   (default `"false"` = V3.2). Set `"true"` for a V3 or V3.1 board.
2. **Wrong polarity must not strand a node.** With the wrong setting the battery reads near 0 V, which used to count as an
   empty battery and put the node into 6-hour low-battery sleep. Readings below 2 V are now ignored.
3. **Vext polarity on V3.2 is unconfirmed (R10, R11, R14).** ESPHome documents LOW = ON (V3 era). V3.2 changed Vext to an LDO,
   and I could not confirm the polarity. It is the substitution `vext_active_low` (default `"true"`); verify with a multimeter
   before the first run (see `docs/wiring.md`).
4. **TL-136 supply is 12 to 32 V (R21),** not 9 to 12 V as written before. 18 V from the MT3608 minus a 3.2 V shunt drop
   (160 Ω at 20 mA) still leaves about 14.8 V.
5. **TCXO voltage:** 1.8 V comes from ESPHome's device page for this board (R10). Other projects use different values for other
   Heltec boards, so if the radio never starts, this is the first setting to question.
6. **Battery divider factor:** ESPHome's page uses 2.0 (R10); other sources give 390 k / 100 k = 4.9 (R12). Calibrate with a
   multimeter; do not trust either number blindly.
7. **EC accuracy is ±10 % of full scale (R19),** about ±100 ppm TDS, so a few hundred µS/cm of uncertainty even when calibrated
   at 25 °C. The sensor is rated for 0 to 1000 ppm only.
8. **MT3608 has internal soft start (R20).** The 220 to 470 µF input capacitor is kept as a cheap precaution for a 3.3 V rail
   feeding an 18 V boost, not as a fix for a known fault.

## 7. Still unverified

* Hardware behaviour of everything: the firmware has only been validated, not run.
* Exact LoRa frame size from `packet_transport` (estimated at 50 to 110 bytes; airtime figures above bracket it).
* Home Assistant entity IDs generated from ESPHome names (check them in your installation).
* openSenseMap API behaviour today (R27 could not be opened; the platform is being rewritten and the API may change).
* Real deep-sleep current and battery life of your board and cell (R15 is a different board).
