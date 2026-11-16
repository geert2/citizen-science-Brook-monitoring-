from _lib import D, C

# ------------------------------------------------------------------ 4 WATER NODE ANALOG
d = D(420, 650, '4 · Water node: analog sensors')
d.box(15, 50, 100, 400, '#eef3f8', '#555555')
d.text(65, 76, 'ADS1115', 14, weight='bold')
for i, t in enumerate(['powered by', '3V3 + GND,', 'SDA + SCL', '(diagram 3)']):
    d.text(65, 98 + i * 15, t, 11, fill='#555555')
for y, t in ((150, 'A0'), (240, 'A1'), (350, 'A2')):
    d.text(105, y + 4, t, 12, 'end', 'bold'); d.pin(115, y, 'blue')
d.text(65, 436, 'A3 unused', 11, fill='#777777')

# --- A0: TL-136 loop
d.box(150, 60, 110, 44, '#fff8e6', '#555555')
d.text(205, 80, 'TL-136', 13, weight='bold'); d.text(205, 96, 'level sensor', 11)
d.text(138, 70, '15 V', 12, 'middle', 'bold', C['purple'])
d.wire([(130, 82), (150, 82)], 'purple'); d.pin(130, 82, 'purple')
d.text(158, 76, '+', 12, 'start', 'bold'); d.text(252, 76, '−', 12, 'end', 'bold')
d.wire([(260, 82), (310, 82)], 'black'); d.dot(310, 82)
d.wire([(310, 82), (365, 82), (365, 112)], 'black'); d.resv(365, 112, 140)
d.wire([(365, 140), (365, 166)], 'black'); d.gnd(365, 166)
d.text(378, 130, '160 Ω', 11, 'start'); d.text(378, 144, 'shunt', 11, 'start', fill='#555555')
d.wire([(310, 82), (310, 150), (225, 150)], 'black'); d.wire([(225, 150), (214, 150)], 'black')
d.resh(190, 214, 150); d.wire([(190, 150), (115, 150)], 'blue')
d.wire([(310, 150), (225, 150)], 'blue')
d.text(202, 138, '1 kΩ', 11)
d.text(130, 190, 'A0 reads the voltage across 160 Ω:', 11, 'start', fill='#555555')
d.text(130, 205, '0.64 V (4 mA) … 3.2 V (20 mA)', 11, 'start', fill='#555555')

# --- A1: SEN0244
d.box(250, 222, 150, 78, '#fff8e6', '#555555')
d.text(335, 252, 'SEN0244', 13, weight='bold'); d.text(335, 269, 'TDS / EC', 11); d.text(335, 285, 'out: 0–2.3 V', 11)
d.text(258, 244, 'A', 11, 'start'); d.text(258, 264, '+', 12, 'start', 'bold'); d.text(258, 284, '−', 12, 'start', 'bold')
d.wire([(115, 240), (250, 240)], 'blue'); d.pin(250, 240, 'blue')
d.wire([(250, 262), (222, 262)], 'red'); d.pin(250, 262, 'red'); d.text(216, 266, '5 V', 12, 'end', 'bold', C['red'])
d.wire([(250, 282), (222, 282)], 'black'); d.pin(250, 282, 'black'); d.gnd(222, 282)

# --- A2: SEN0189 with divider
d.box(250, 332, 150, 78, '#fff8e6', '#555555')
d.text(335, 362, 'SEN0189', 13, weight='bold'); d.text(335, 379, 'turbidity', 11); d.text(335, 395, 'out: up to 4.5 V', 11)
d.text(258, 354, 'OUT', 11, 'start'); d.text(258, 374, '+', 12, 'start', 'bold'); d.text(258, 394, '−', 12, 'start', 'bold')
d.pin(250, 350, 'blue'); d.wire([(250, 350), (214, 350)], 'blue'); d.resh(190, 214, 350)
d.wire([(190, 350), (115, 350)], 'blue'); d.dot(150, 350, 'blue')
d.wire([(150, 350), (150, 374)], 'blue'); d.resv(150, 374, 398); d.wire([(150, 398), (150, 412)], 'black'); d.gnd(150, 412)
d.text(202, 340, '10 kΩ', 11); d.text(160, 392, '10 kΩ', 11, 'start')
d.wire([(250, 372), (222, 372)], 'red'); d.pin(250, 372, 'red'); d.text(216, 376, '5 V', 12, 'end', 'bold', C['red'])
d.wire([(250, 392), (222, 392)], 'black'); d.pin(250, 392, 'black'); d.gnd(222, 392)

d.notes(480, ['• 15 V = MT3608 #2, 5 V = MT3608 #1 (diagram 2).',
              '• The 10 kΩ / 10 kΩ divider halves the 4.5 V output so',
              '  the ADS1115 (3.3 V supply) is never overloaded.',
              '• The ADS reads A2 = half the sensor voltage;',
              '  the gateway multiplies it by 2 again.',
              '• SEN0189: set the small slide switch to ANALOG.',
              '• Check the silkscreen on your boards for pin order.',
              '• Ground symbols are all the same GND wire.'])
d.legend([('15 V', 'purple'), ('5 V', 'red'), ('GND', 'black'), ('analog signal', 'blue')])
d.save('04-water-node-analog.svg')

# ------------------------------------------------------------------ 5 AIR QUALITY NODE
d = D(420, 690, '5 · Air quality node (mains USB)')
d.box(15, 55, 110, 345, '#e6f7ea', '#2a9d3f')
d.text(70, 80, 'ESP32', 14, weight='bold'); d.text(70, 97, 'DevKit', 12)
esp = [(125, 'GPIO16', 'RX2', 'blue'), (155, 'GPIO17', 'TX2', 'green'), (185, 'VIN', '5 V', 'red'), (215, 'GND', '', 'black'),
       (275, '3V3', '', 'orange'), (305, 'GND', '', 'black'), (335, 'GPIO22', 'SCL', 'green'), (365, 'GPIO21', 'SDA', 'blue')]
for y, n, a, col in esp:
    d.text(116, y + 4, n, 11, 'end', 'bold'); d.pin(125, y, col)
d.text(66, 126, '', 11)

# SDS011
d.box(250, 55, 155, 190, '#fff8e6', '#555555')
d.text(327, 78, 'SDS011', 14, weight='bold'); d.text(327, 95, 'dust sensor', 12)
sds = [(125, 'TXD', 'blue'), (155, 'RXD', 'green'), (185, '5V', 'red'), (215, 'GND', 'black')]
for y, n, col in sds:
    d.pin(250, y, col); d.text(258, y + 4, n, 11, 'start', 'bold')
d.wire([(125, 125), (250, 125)], 'blue'); d.wire([(125, 155), (250, 155)], 'green')
d.wire([(125, 185), (250, 185)], 'red'); d.wire([(125, 215), (250, 215)], 'black')
d.text(188, 118, 'SDS TX → ESP RX', 10, 'middle', fill=C['blue'])
d.text(188, 148, 'ESP TX → SDS RX', 10, 'middle', fill=C['green'])
d.text(188, 178, '5 V', 10, 'middle', fill=C['red'])

# BME280
d.box(250, 255, 155, 140, '#fff8e6', '#555555')
d.text(350, 278, 'BME280', 14, weight='bold'); d.text(350, 296, 'temp · RH', 11); d.text(350, 311, 'pressure', 11)
bme = [(275, 'VIN', 'orange'), (305, 'GND', 'black'), (335, 'SCL', 'green'), (365, 'SDA', 'blue')]
for y, n, col in bme:
    d.pin(250, y, col); d.text(258, y + 4, n, 11, 'start', 'bold')
d.wire([(125, 275), (250, 275)], 'orange'); d.wire([(125, 305), (250, 305)], 'black')
d.wire([(125, 335), (250, 335)], 'green'); d.wire([(125, 365), (250, 365)], 'blue')

# USB supply
d.box(15, 470, 110, 44, '#eef3f8', '#555555'); d.text(70, 489, '5 V USB', 12, weight='bold'); d.text(70, 505, 'phone charger', 11)
d.wire([(70, 470), (70, 400)], 'red', 5); d.text(82, 440, 'USB cable', 11, 'start', fill='#555555')
d.text(70, 392, 'USB', 11, fill='#555555')

d.notes(540, ['• SDS011: use the 4 wires 5V, GND, TXD, RXD of its cable.',
              '• Crossed on purpose: TX of one side goes to RX of the other.',
              '• BME280: SDO to GND gives address 0x76 (try 0x77 if not',
              '  found in the I2C scan).',
              '• Inlet of the SDS011 pointing down, away from the box.'])
d.legend([('3.3 V', 'orange'), ('5 V', 'red'), ('GND', 'black'), ('signal', 'blue')])
d.save('05-air-quality-node.svg')

