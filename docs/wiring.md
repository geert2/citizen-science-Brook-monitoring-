{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\froman\fcharset0 Times-Bold;\f2\froman\fcharset0 Times-Roman;
}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # \uc0\u55357 \u56588  Wiring Diagrams\
\
## Sensor Node (Heltec V3)\
### Pinout\
| Sensor | Pin | Type | Notes |\
|--------|-----|------|-------|\
| TL-136 | GPIO34 | ADC1_6 | 4\'9620mA \uc0\u8594  **160\u937  resistor** \u8594  GPIO34 |\
| DS18B20 | GPIO22 | 1-Wire | + **4.7k\uc0\u937  pull-up** to 3.3V |\
| SEN0189 | GPIO35 | ADC1_7 | Analog output |\
| Turbidity | GPIO32 | ADC1_4 | Analog output (epoxy-potted) |\
| JSN-SR04T | GPIO25 | Trigger | Ultrasonic |\
| JSN-SR04T | GPIO26 | Echo | Ultrasonic |\
| LoRa CS | GPIO8 | SPI | |\
| LoRa RST | GPIO12 | SPI | |\
| LoRa DIO0 | GPIO9 | SPI | |\
| LoRa BUSY | GPIO14 | SPI | SX1262 only |\
\
### TL-136 Circuit\
\
\pard\pardeftab720\sa280\partightenfactor0

\f1\b\fs28 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 \
\pard\pardeftab720\sa240\partightenfactor0

\f2\b0\fs24 \cf0 TL-136 (+) \uc0\u9472 \u9472 \u9658  12V (from XL6009) TL-136 (-) \u9472 \u9472 \u9658  160\u937  resistor \u9472 \u9472 \u9658  GND \
\uc0\u9474  \
\uc0\u9492 \u9472 \u9472 \u9658  GPIO34 (ADC)\
\
## Air Quality Node (ESP32)\
### Pinout\
| Sensor | Pin | Type | Notes |\
|--------|-----|------|-------|\
| SDS011 RX | GPIO16 | UART | |\
| SDS011 TX | GPIO17 | UART | |\
| SDS011 VCC | 5V | Power | From XL6009 |\
| SDS011 GND | GND | Ground | |\
| BME280 SDA | GPIO21 | I\'b2C | |\
| BME280 SCL | GPIO22 | I\'b2C | |\
| BME280 VCC | 3.3V | Power | |\
| XL6009 IN | VIN | Power | From 2\'d718650 (7.4V) |\
| XL6009 OUT | 5V | Power | To SDS011 |\
}