# Wiring Diagrams

## Sensor Node (Heltec V3)

### Pinout

| Sensor | Pin | Type | Notes |
|--------|-----|------|-------|
| TL-136 | GPIO34 | ADC1_6 | 160Ω resistor in series |
| DS18B20 | GPIO22 | 1-Wire | + 4.7kΩ pull-up to 3.3V |
| SEN0189 | GPIO35 | ADC1_7 | Analog output |
| Turbidity | GPIO32 | ADC1_4 | Analog output (epoxy-potted) |
| JSN-SR04T | GPIO25 | Trigger | Ultrasonic |
| JSN-SR04T | GPIO26 | Echo | Ultrasonic |
| LoRa CS | GPIO8 | SPI | |
| LoRa RST | GPIO12 | SPI | |
| LoRa DIO0 | GPIO9 | SPI | |
| LoRa BUSY | GPIO14 | SPI | SX1262 only |

### TL-136 Circuit

```
TL-136 (+) ────┬──── 12V (from XL6009 or solar regulator)
                │
TL-136 (-) ────┴──── 160Ω resistor ──── GPIO34 (ADC)
                │
                └──── GND
```

**Important Notes:**
- TL-136 requires 5-30V power supply
- The 160Ω resistor converts current (4-20mA) to voltage (0.64V-3.2V)
- For 160Ω: level_m = (V - 0.64) / 2.56

### DS18B20 Circuit

```
DS18B20 VCC ──── 3.3V
DS18B20 GND ──── GND
DS18B20 DATA ──┬── GPIO22
                └── 4.7kΩ pull-up ──── 3.3V
```

### SEN0189 Circuit

```
SEN0189 VCC ──── 5V (from XL6009)
SEN0189 GND ──── GND
SEN0189 Signal ── GPIO35 (ADC)
```

**Note:** SEN0189 requires 5V power and outputs 0-2.3V analog signal

### Turbidity Sensor Circuit

```
Turbidity VCC ──── 5V (from XL6009)
Turbidity GND ──── GND
Turbidity Signal ── GPIO32 (ADC)
```

**Waterproofing:** Sensor is epoxy-potted to prevent water ingress

### JSN-SR04T Circuit

```
JSN-SR04T VCC ──── 5V (from XL6009)
JSN-SR04T GND ──── GND
JSN-SR04T Trigger ── GPIO25
JSN-SR04T Echo ──── GPIO26
```

**Mounting:** Position sensor facing downward, 0.5m above maximum water level

---

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
| BME280 GND | GND | Ground | |

### Power Circuit

```
2x 18650 (1S2P, 3.7V) ──┬── TP4056 (for charging)
                         │
                         ├── XL6009 IN (3-32V input)
                         │
                         └── XL6009 OUT ── 5V ──── SDS011 VCC
                              (adjustable)
```

**Important:**
- XL6009 boosts 3.7V to 5V for SDS011
- TP4056 handles battery charging from solar (with DW01A protection)
- For solar: Use CN3791 MPPT charger instead of TP4056 for better efficiency

### SDS011 Circuit

```
SDS011 VCC ──── 5V
SDS011 GND ──── GND
SDS011 RX ───── GPIO16 (ESP32 TX)
SDS011 TX ───── GPIO17 (ESP32 RX)
```

**Note:** SDS011 uses UART at 9600 baud

### BME280 Circuit

```
BME280 VCC ──── 3.3V
BME280 GND ──── GND
BME280 SDA ──── GPIO21
BME280 SCL ──── GPIO22
```

**Note:** BME280 uses I²C at address 0x76 or 0x77

---

## Gateway Node (Heltec V3)

### Pinout

| Component | Pin | Type | Notes |
|-----------|-----|------|-------|
| LoRa CS | GPIO8 | SPI | |
| LoRa RST | GPIO12 | SPI | |
| LoRa DIO0 | GPIO9 | SPI | |
| LoRa BUSY | GPIO14 | SPI | SX1262 only |

### Power

Same as Sensor Node:
- 2x 18650 batteries (1S2P)
- 10W solar panel
- CN3791 MPPT charger (recommended) or TP4056 with buck converter

---

## Power System Architecture

### Recommended Setup (with MPPT)

```
10W Solar Panel
   (12V nominal, 19V Voc)
        │
        ▼
   CN3791 MPPT Charger
   (12V input version)
        │
        ▼
   2x 18650 Li-ion (1S2P, 3.7V)
        │
        ├──► Sensor Node (Heltec V3) ──── 3.3V
        │
        └──► XL6009 Boost ──── 5V ──── Air Quality Node (ESP32 + SDS011)
```

### Alternative Setup (without MPPT)

```
10W Solar Panel
   (12V nominal, 19V Voc)
        │
        ▼
   LM2596 Buck Converter
   (19V → 5V)
        │
        ▼
   TP4056 + DW01A Protection
   (5V → 3.7V charging)
        │
        ▼
   2x 18650 Li-ion (1S2P, 3.7V)
        │
        ├──► Sensor Node (Heltec V3) ──── 3.3V
        │
        └──► XL6009 Boost ──── 5V ──── Air Quality Node
```

**Important Notes:**
- CN3791 is preferred for solar charging (MPPT is ~20-30% more efficient)
- XL6009 input range: 3-32V, output adjustable 5-35V
- TP4056 requires input voltage < 6V (use buck converter for 19V solar)
- DW01A + FS8205A provide overcharge/overdischarge protection
