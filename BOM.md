# Bill of Materials (BOM) & Sourcing Guide - BROOK LITE

> `lite` branch: water level (TL-136 0-2 m), water temperature (DS18B20), electrical conductivity (DFRobot SEN0244), air temperature, humidity and pressure (BME280). No ADS1115, turbidity, ultrasonic sensor or air-quality node (those are on `main`).

This checklist covers all hardware, waterproofing consumables, and gateway parts needed to build and deploy a brook lite station. Prices are approximate (including VAT) based on Benelux/EU electronics suppliers.

---

## 1. Field Node at the Brook (~€135 - €195)
One per measuring point.

| Status | Component | Exact Specification | Qty | Approx. Cost | Suggested Suppliers (BE / NL / EU) |
| :--- | :--- | :--- | :---: | :---: | :--- |
| [ ] | **Microcontroller** | Heltec WiFi LoRa 32 V3 (**868 MHz** EU version, ESP32-S3 + SX1262). Note the revision on the silkscreen (V3.0, V3.1 or V3.2): it decides the battery-divider polarity, see `docs/wiring.md` | 1 | €21 - €25 | TinyTronics, Otronic |
| [ ] | **Level Sensor** | TL-136 Submersible Level Transmitter (**0-2 m**, **4-20 mA**, **vented** cable long enough to reach the box, typically 5-10 m) | 1 | €25 - €35 | Amazon.com.be, AliExpress |
| [ ] | **Temperature Probe** | Waterproof DS18B20 Digital Probe (1 m cable) | 1 | €3 | Gotron, Otronic |
| [ ] | **Step-Up Boost Module** | MT3608 DC-DC Adjustable Step-Up Converter (set to **18.0 V**) | 1 | €2 | TinyTronics, Otronic |
| [ ] | **EC / Water Quality Sensor** | DFRobot **SEN0244** Gravity Analog TDS/EC Sensor Module + Probe (probe has **two** electrode wires) | 1 | €12 - €14 | TinyTronics, BerryBase |
| [ ] | **BME280 module** | BME280 breakout, 3.3 V, I²C (4 pins). Check it is a real BME280 (with humidity) and not a BMP280. | 1 | €4 - €6 | TinyTronics, Otronic, AliExpress |
| [ ] | **Radiation shield** | Small louvred (Stevenson-type) sensor shield, or a DIY stack of white plant saucers; plus 4-core cable (≤ 1 m) and one extra cable gland | 1 | €8 - €15 | AliExpress, Amazon.com.be, DIY |
| [ ] | **Shunt Resistor** | **100 Ω** metal film, **0.1 %** (25 ppm), 0.25 W | 1 | €0.50 | Gotron, Mouser, Farnell |
| [ ] | **Input Protection** | 1 kΩ resistor, **3.6 V zener** (e.g. BZX84C3V6 or 1N5227B), 100 nF ceramic capacitor | 1 set | €0.50 | Gotron, Otronic |
| [ ] | **Boost Input Capacitor** | 220 - 470 µF low-ESR electrolytic, ≥ 10 V | 1 | €0.50 | Gotron, Otronic |
| [ ] | **Pull-Up Resistor** | 4.7 kΩ resistor (0.25 W, for DS18B20 data line) | 1 | €0.10 | Gotron *(often included with DS18B20)* |
| [ ] | **Batteries & Holder** | 2 × **protected** 18650 Li-Ion cells (3000 mAh+, e.g. Samsung 35E with protection), **in parallel**, + 2-cell holder wired in parallel (1S2P) | 2 | €16 - €24 | TinyTronics, NKON |
| [ ] | **Waterproof Enclosure** | IP65 Outdoor Junction Box (approx. 150 x 110 x 70 mm) | 1 | €7 - €9 | Hubo, Brico |
| [ ] | **Enclosure Breather Vent** | M12 or PG7 membrane vent plug (IP67/IP68, e.g. Gore-type) for the TL-136 vent | 1 | €2 - €4 | Amazon.com.be, RS, Farnell |
| [ ] | **Cable Glands** | PG9 or PG11 Waterproof Nylon Cable Glands (with rubber seals): TL-136, DS18B20, EC probe, BME280 | 4 | €2 | Hubo, Brico |
| [ ] | **Desiccant** | Silica Gel Packets (10 g-20 g) | 2 | €1 | Amazon.com.be |
| [ ] | **Assembly parts** | Perfboard or small PCB, screw terminals, hook-up wire, standoffs, cable ties | 1 set | €4 - €6 | Gotron, Hubo |
| [ ] | **Stilling pipe** | 40-50 mm PVC pipe (1.5-3 m, depending on the bank) with 8-10 mm holes every 5-10 cm, perforated end cap, 2-3 stainless pipe clamps + stakes | 1 | €10 - €20 | Hubo, Brico |
| [ ] | **Conduit** | Flexible corrugated conduit (20-25 mm) from the pipe to the box | 3-5 m | €4 - €8 | Hubo, Brico |
| [ ] | **Post** | Wooden or steel post for the box and radiation shield, standing above flood level | 1 | €8 - €15 | Hubo, Brico |
| [ ] | **Pull line** | 2-3 mm stainless wire or Kevlar line + clamp, to position the probe bundle in the pipe without pulling on the cables | 1 | €3 - €5 | Hubo, Brico |
| [ ] | **Staff gauge** *(if none exists)* | Enamelled water-level staff (peilschaal), 1-2 m, fixed to a post in the brook | 1 | €30 - €60 | hydro suppliers; or a DIY ruler on a post |

*Optional range:* external 868 MHz antenna with bulkhead SMA pigtail (€6 - €9).

---

## 2. Submersible Cable Waterproofing (~€10, Shared Across Multiple Nodes)
Needed to extend the short factory cables on the EC and DS18B20 probes to the box on the bank (typically 3-5 m).

| Status | Item | Specification | Qty | Approx. Cost | Suggested Suppliers |
| :--- | :--- | :--- | :---: | :---: | :--- |
| [ ] | **Extension Cable** | Flexible waterproof rubber cable (H05RN-F, 3 x 0.5 mm²). The DS18B20 uses all three cores; the EC probe uses **two** (twisted pair or screened is better). | 8 m | €6 - €8 | Hubo, Brico |
| [ ] | **Adhesive Heat-Shrink** | **3:1 Dual-Wall Marine Adhesive-Lined** Heat-Shrink Tubing (3 mm & 10 mm) | 1 pack | €5 | Amazon.com.be, Gotron |
| [ ] | **Rubber Sealing Tape** | Self-Amalgamating Silicone/Rubber Tape | 1 roll | €5 | Hubo, Brico |
| [ ] | **Cable Ties** | UV-Resistant Black Nylon Zip Ties | 1 pack | €2 | Hubo, Brico |

---

## 3. Gateway at Home (~€21 - €30, One-Time Purchase)
The gateway receives the LoRa packets and uploads them to Home Assistant and openSenseMap. It is separate from the gateway of the full station on `main` (different firmware).

| Status | Component | Exact Specification | Qty | Approx. Cost | Suggested Suppliers |
| :--- | :--- | :--- | :---: | :---: | :--- |
| [ ] | **Gateway Board** | Heltec WiFi LoRa 32 V3 (**868 MHz** EU version) | 1 | €21 - €25 | TinyTronics, Otronic |
| [ ] | **Power Supply** | Plain 5 V USB-C charger + USB-C data cable (avoid USB-PD-only chargers) | 1 | €0 - €5 | Reuse existing charger |
| [ ] | **External Antenna** *(Optional)* | 868 MHz High-Gain SMA Antenna + U.FL-to-SMA Pigtail (for > 2 km range) | 1 | €6 - €9 | TinyTronics |

---

## 4. Calibration & Maintenance Supplies (Shared by Community Group)

| Status | Item | Specification | Approx. Cost | Suggested Suppliers |
| :--- | :--- | :--- | :---: | :--- |
| [ ] | **Multimeter** | To check boost voltage and battery voltage | €10+ | any |
| [ ] | **Handheld EC meter** *(optional)* | To check the EC sensor in the brook every few months | €15 - €40 | aquarium/hydroponics shop |
| [ ] | **Waders or boots, gloves** | Safe work at the bank | - | - |
| [ ] | **Reference thermometer / hygrometer** *(optional)* | To sanity-check the BME280 and DS18B20 | €10 - €20 | any |
| [ ] | **EC Calibration Fluid, high point** | Standard **1413 µS/cm** solution (250 ml) | €8 - €10 | Amazon.com.be or aquarium/hydroponics shop |
| [ ] | **EC Calibration Fluid, low point** | Standard **84 µS/cm** solution (250 ml), for a true two-point calibration | €8 - €10 | same |

---

## Buying Notes & Pitfalls to Avoid
* **Check LoRa frequency:** verify the Heltec V3 board is labelled **868 MHz** (Europe), not 915 MHz or 433 MHz.
* **Check TL-136 range & output:** choose **0-2 m**, **4-20 mA** and a **vented** cable. A 0-2 m sensor resolves the level much better than a 0-5 m one; floods above 2 m are flagged but not measured. Do not buy the 0-10 V or RS485 versions; the firmware assumes a 4-20 mA loop. Check the supply range on the label (listed as 12-32 V [R21]; the 18 V boost covers this).
* **BME280 vs BMP280:** the BMP280 has no humidity sensor. Look for "BME280" on the chip (square metal can with a hole) and in the listing; many cheap listings mix them up.
* **EC sensor range:** the cheap analog EC/TDS sensor is meant for fresh water up to about 2000 µS/cm. It is fine for seeing storm dilution, discharges or fertilizer run-off as trends, not for lab-grade numbers.
* **Use a protected 18650:** the Heltec board charges the cell but has no deep-discharge cut-off.
* **Heat-shrink type matters:** ordinary thin-wall heat-shrink does not seal against water pressure. Look for **adhesive-lined** / **dual-wall** (*lijmgevuld* / *met lijmlaag*).
* **Shunt value:** use **100 Ω**. The 160 Ω of the full station only works with its ADS1115 (see `docs/wiring.md`).
* **Permission:** ask the waterway manager before fixing a pipe, post or staff gauge in or on the bank.
