# De Meetbeek – Water & Air Quality Monitoring Station
*Citizen science project for monitoring De Grote Beek (Hansbeke, Belgium)*

[![ESPHome](https://img.shields.io/badge/ESPHome-1.0-blue)](https://esphome.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Sensor.Community](https://img.shields.io/badge/Sensor.Community-Data-green)](https://sensor.community/)

## 🌊 Project Overview
This project monitors **water quality** (level, temperature, EC, turbidity) and **air quality** (PM2.5/PM10) in **De Grote Beek**, a small stream in the sandy-loam region of East Flanders, Belgium. Data is shared openly with [sensor.community](https://sensor.community/) and local stakeholders.

### 📡 Features
- **LoRa long-range** communication (868 MHz EU) between sensor nodes and gateway.
- **Solar-powered** with Li-ion battery backup.
- **Open data** via MQTT and sensor.community API.
- **Low-cost** (~€150–200) and **DIY-friendly**.

### 🌍 Location
- **Stream**: De Grote Beek (Hansbeke, Deinze)
- **Watertype**: Zandleembeek (sandy-loam)
- **Coordinates**: [Add your GPS coordinates here]
- **VMM Reference**: [VMM Databank](https://geo.vmm.be/geoloket/)

---

## 🛠️ Hardware
### Sensor Nodes
| Node | Board | Sensors | Power | Communication |
|------|-------|---------|-------|---------------|
| **Water Sensor Node** | Heltec V3 (ESP32 + SX1262) | TL-136, DS18B20, SEN0189, Turbidity, JSN-SR04T | 3.3V (2×18650 + Solar) | LoRa (868 MHz) |
| **Air Quality Node** | ESP32 | SDS011, BME280 | 5V (XL6009 Boost) | Wi-Fi |
| **Gateway Node** | Heltec V3 (ESP32 + SX1262) | - | 3.3V (2×18650 + Solar) | LoRa + Wi-Fi + MQTT |

### Shopping List
| Item | Supplier | Cost | Status |
|------|----------|------|--------|
| TL-136 (Level) | [AliExpress](https://www.aliexpress.com/wholesale?SearchText=TL-136) | €19.49 | ✅ |
| DS18B20 (Water Temp) | [Botland](https://botland.store/ds18b20-waterproof/10315) | €3.50 | ✅ |
| SEN0189 (EC) | [Farnell NL](https://nl.farnell.com/dfrobot/sen0189/ec-sensor/dp/3352312) | €15.90 | ✅ |
| Turbidity (DFRobot) | [Botland](https://botland.store/turbidity-sensor/6540) | €18.90 | ✅ |
| JSN-SR04T (Ultrasonic) | [Botland](https://botland.store/ultrasonic-sensor-jsn-sr04t/10210) | €8.90 | ✅ |
| SDS011 (PM2.5/PM10) | [Sensor.Community Shop](https://shop.sensor.community/) | €24.90 | ✅ |
| BME280 (Air T/H/P) | [Opencircuit](https://www.opencircuit.nl/product/bme280/) | €5.95 | ✅ |
| Heltec V3 (×2) | [Hexaspot](https://hexaspot.com/) | €XX | ✅ |
| 10W Solar Panel | [AliExpress](https://www.aliexpress.com/wholesale?SearchText=10W+solar+panel) | €15 | ✅ |
| 2× 18650 Battery | Local | €10 | ✅ |
| XL6009 + TP4056 | [AliExpress](https://www.aliexpress.com/wholesale?SearchText=XL6009+TP4056) | €3 | ✅ |
| IP66 Box | [Amazon NL](https://www.amazon.nl/s?k=IP66+junction+box) | €15 | ✅ |
| PVC Pipe (110mm) | Local Hardware | €7 | ✅ |
| **Total** | | **~€150–200** | |

---

## 📡 System Architecture