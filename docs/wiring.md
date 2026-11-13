# 🔌 Wiring Diagrams

## Sensor Node (Heltec V3)
### Pinout
| Sensor | Pin | Type | Notes |
|--------|-----|------|-------|
| TL-136 | GPIO34 | ADC1_6 | 4–20mA → **160Ω resistor** → GPIO34 |
| DS18B20 | GPIO22 | 1-Wire | + **4.7kΩ pull-up** to 3.3V |
| SEN0189 | GPIO35 | ADC1_7 | Analog output |
| Turbidity | GPIO32 | ADC1_4 | Analog output (epoxy-potted) |
| JSN-SR04T | GPIO25 | Trigger | Ultrasonic |
| JSN-SR04T | GPIO26 | Echo | Ultrasonic |
| LoRa CS | GPIO8 | SPI | |
| LoRa RST | GPIO12 | SPI | |
| LoRa DIO0 | GPIO9 | SPI | |
| LoRa BUSY | GPIO14 | SPI | SX1262 only |

### TL-136 Circuit


TL-136 (+) ──► 12V (from XL6009) TL-136 (-) ──► 160Ω resistor ──► GND 
│ 
└──► GPIO34 (ADC)

## Air Quality Node (ESP32)
### Pinout
| Sensor | Pin | Type | Notes |
|--------|-----|------|-------|
| SDS011 RX | GPIO16 | UART | |
| SDS011 TX | GPIO17 | UART | |
| SDS011 VCC | 5V | Power | From XL6009 |
| SDS011 GND | GND | Ground | |
| BME280 SDA | GPIO21 | I²C | |
| BME280 SCL | GPIO22 | I²C | |
| BME280 VCC | 3.3V | Power | |
| XL6009 IN | VIN | Power | From 2×18650 (7.4V) |
| XL6009 OUT | 5V | Power | To SDS011 |
