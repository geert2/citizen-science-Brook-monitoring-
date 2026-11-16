from _lib import D, C

# ------------------------------------------------------------------ 1 POWER / BATTERY
d = D(420, 750, '1 · Solar charging and battery')
d.box(110, 50, 200, 64, '#e8f1ff', '#1d6fdc')
d.text(210, 76, '12 V solar panel', 14, weight='bold')
d.text(210, 94, 'about 10 W', 12)
d.wire([(160, 114), (160, 160)], 'red'); d.wire([(260, 114), (260, 160)], 'black')
d.text(172, 142, '+', 14, 'start', 'bold'); d.text(272, 142, '−', 14, 'start', 'bold')
d.box(110, 160, 200, 70, '#fff4e0', '#f08a00')
d.text(210, 192, 'CN3791 MPPT charger', 14, weight='bold')
d.text(210, 209, '1 cell · 4.2 V', 12)
for x, t in ((160, 'IN +'), (260, 'IN −')): d.text(x, 175, t, 11)
d.text(210, 224, 'BAT +', 11); d.text(270, 224, 'BAT −', 11)
d.pin(160, 160, 'red'); d.pin(260, 160, 'black'); d.pin(210, 230, 'red'); d.pin(270, 230, 'black')

# battery pack (2 cells in parallel)
d.box(110, 290, 200, 110, '#f3f3f3', '#555555')
d.wire([(125, 305), (295, 305)], 'red', 5); d.wire([(125, 385), (295, 385)], 'black', 5)
for cx, n in ((135, '#1'), (225, '#2')):
    d.box(cx, 315, 60, 60, '#ffffff', '#555555', 6)
    d.text(cx + 30, 341, '18650', 13, weight='bold'); d.text(cx + 30, 359, n, 12)
    d.wire([(cx + 30, 305), (cx + 30, 315)], 'red', 3); d.wire([(cx + 30, 375), (cx + 30, 385)], 'black', 3)
d.text(210, 418, '2 × 18650 cells in PARALLEL', 13, weight='bold')
d.text(210, 435, 'protected cells · never in series', 12)

# charger -> battery
d.wire([(210, 230), (210, 305)], 'red'); d.dot(210, 305, 'red')
d.wire([(270, 230), (270, 248), (350, 248), (350, 470), (270, 470), (270, 500)], 'black')
d.wire([(350, 385), (295, 385)], 'black'); d.dot(350, 385)
# battery -> Heltec with fuse
d.wire([(125, 305), (96, 305), (96, 470), (150, 470), (150, 500)], 'red')
d.box(88, 372, 16, 34, '#fff3cd', '#b58900', 3, 2)
d.text(82, 394, '2 A fuse', 12, 'end')

d.box(90, 500, 240, 86, '#e6f7ea', '#2a9d3f')
d.text(150, 515, 'BAT +', 11); d.text(270, 515, 'BAT −', 11)
d.text(210, 540, 'Heltec WiFi LoRa 32 V3', 14, weight='bold')
d.text(210, 558, 'battery connector (JST 1.25)', 12)
d.text(210, 576, 'check the polarity first!', 12, fill=C['red'])
d.pin(150, 500, 'red'); d.pin(270, 500, 'black')

d.notes(620, ['• Cells in parallel: + to +, − to −.  CN3791 = 1 cell.',
              '• Set the CN3791 MPPT voltage to about 80 % of the',
              '  panel open-circuit voltage.',
              '• Do not charge Li-ion below 0 °C.',
              '• Attach the antenna BEFORE powering the Heltec.'])
d.legend([('+ battery', 'red'), ('GND / −', 'black')])
d.save('01-power-battery.svg')

# ------------------------------------------------------------------ 2 BOOSTERS
d = D(420, 660, '2 · Switched sensor power')
d.box(110, 50, 200, 64, '#e6f7ea', '#2a9d3f')
d.text(210, 76, 'Heltec V3', 14, weight='bold'); d.text(210, 93, 'Vext = switched 3.3 V', 12)
d.text(160, 108, 'Vext', 11); d.text(260, 108, 'GND', 11)
d.pin(160, 114, 'orange'); d.pin(260, 114, 'black')
d.wire([(260, 114), (260, 134)], 'black'); d.gnd(260, 134)
d.text(300, 128, 'to GND', 11, 'start', fill='#555555')
d.wire([(160, 114), (160, 160)], 'orange')
d.wire([(95, 200), (95, 160), (285, 160), (285, 200)], 'orange'); d.dot(160, 160, 'orange')
d.text(170, 142, '3.3 V · on when GPIO36 = LOW', 11, 'start', fill=C['orange'])

for x0, name, setv, col in ((40, 'MT3608 #1', 'set to 5.0 V', 'red'), (230, 'MT3608 #2', 'set to about 15 V', 'purple')):
    d.box(x0, 200, 150, 80, '#eef3f8', '#555555')
    d.text(x0 + 75, 236, name, 14, weight='bold')
    d.text(x0 + 75, 254, setv, 12, fill=C[col])
    inx, outx, gx = x0 + 55, x0 + 55, x0 + 110
    d.text(inx, 216, 'IN +', 11); d.text(outx, 273, 'OUT +', 11); d.text(gx, 273, 'GND', 11)
    d.pin(inx, 200, 'orange'); d.pin(outx, 280, col); d.pin(gx, 280, 'black')
    d.wire([(gx, 280), (gx, 300)], 'black'); d.gnd(gx, 300)
d.wire([(95, 280), (95, 340)], 'red'); d.wire([(285, 280), (285, 340)], 'purple')

d.box(20, 340, 180, 122, '#fdecec', '#d62828')
d.text(110, 364, '5 V rail', 14, weight='bold')
for i, t in enumerate(['→ SEN0189 turbidity (+)', '→ SEN0244 TDS / EC (+)', '→ JSN-SR04T (5V)']):
    d.text(110, 389 + i * 20, t, 12)
d.text(110, 452, 'sensor GND: any GND point', 11, fill='#555555')
d.box(220, 340, 180, 122, '#f3ebff', '#8a3ffc')
d.text(310, 364, '~15 V rail', 14, weight='bold')
d.text(310, 389, '→ TL-136 (+) only', 12)
d.text(310, 409, '(4–20 mA loop supply)', 12)
d.text(310, 435, 'NEVER to ADS1115', 12, fill=C['red'], weight='bold')
d.text(310, 452, 'or the Heltec!', 12, fill=C['red'], weight='bold')

d.notes(495, ['1. Set each module with NOTHING on OUT +.',
              '2. Meter on OUT + and GND: 5.0 V / about 15 V.',
              '3. Turn the trimmer slowly (it may start at 28 V).',
              '4. IN − and OUT − are the same wire on the module.',
              '5. Expect 135–235 mA from Vext while measuring.',
              '6. XL6009 cannot be used: it needs 5 V or more in.'])
d.text(18, 660 - 38, 'All ground symbols are the same GND wire.', 12, 'start', fill='#333333')
d.legend([('3.3 V', 'orange'), ('5 V', 'red'), ('~15 V', 'purple'), ('GND', 'black')])
d.save('02-boosters.svg')

# ------------------------------------------------------------------ 3 WATER NODE DIGITAL
d = D(420, 690, '3 · Water node: digital connections')
# ADS1115
d.box(90, 40, 240, 90, '#eef3f8', '#555555')
d.text(210, 62, 'ADS1115', 14, weight='bold')
d.text(210, 80, '16-bit ADC · I2C address 0x48', 11)
d.text(210, 96, 'inputs A0–A3: see diagram 4', 11)
for x, t, col in ((110, 'ADDR', 'black'), (140, 'VDD', 'orange'), (190, 'GND', 'black'), (240, 'SDA', 'blue'), (290, 'SCL', 'green')):
    d.text(x, 121, t, 10); d.pin(x, 130, col)
d.wire([(110, 130), (110, 150)], 'black'); d.gnd(110, 150)
d.text(98, 157, 'ADDR to GND', 11, 'end', fill='#555555')

# Heltec (middle)
d.box(40, 230, 340, 100, '#e6f7ea', '#2a9d3f')
d.text(210, 272, 'Heltec WiFi LoRa 32 V3', 14, weight='bold')
d.text(210, 291, 'header pin names', 11, fill='#555555')
for x, t, col in ((140, '3V3', 'orange'), (190, 'GND', 'black'), (240, 'GPIO41', 'blue'), (290, 'GPIO42', 'green')):
    d.text(x, 248, t, 10); d.pin(x, 230, col)
d.wire([(140, 130), (140, 230)], 'orange'); d.wire([(190, 130), (190, 230)], 'black')
d.wire([(240, 130), (240, 230)], 'blue'); d.wire([(290, 130), (290, 230)], 'green')
d.text(248, 185, 'SDA', 11, 'start', fill=C['blue']); d.text(298, 185, 'SCL', 11, 'start', fill=C['green'])

# bottom pins of Heltec
for x, t, col in ((70, '3V3', 'orange'), (110, 'GPIO5', 'blue'), (150, 'GND', 'black'), (265, 'GPIO6', 'teal'), (305, 'GPIO7', 'pink')):
    d.text(x, 316, t, 10); d.pin(x, 330, col)

# DS18B20
d.box(40, 470, 140, 72, '#fff8e6', '#555555')
for x, t, col in ((70, 'VCC', 'orange'), (110, 'DATA', 'blue'), (150, 'GND', 'black')):
    d.text(x, 487, t, 10); d.pin(x, 470, col)
d.text(110, 517, 'DS18B20', 14, weight='bold'); d.text(110, 534, 'water temperature', 11)
d.wire([(70, 330), (70, 470)], 'orange'); d.wire([(110, 330), (110, 470)], 'blue'); d.wire([(150, 330), (150, 470)], 'black')
d.dot(70, 400, 'orange'); d.dot(110, 400, 'blue')
d.wire([(70, 400), (82, 400)], 'black', 2.5); d.resh(82, 98, 400); d.wire([(98, 400), (110, 400)], 'black', 2.5)
d.text(62, 404, '4.7 kΩ', 11, 'end'); d.text(90, 425, 'pull-up', 11, fill='#555555')

# JSN-SR04T
d.box(210, 490, 190, 62, '#fff8e6', '#555555')
for x, t, col in ((230, '5V', 'red'), (265, 'TRIG', 'teal'), (305, 'ECHO', 'pink'), (345, 'GND', 'black')):
    d.text(x, 507, t, 10); d.pin(x, 490, col)
d.text(305, 538, 'JSN-SR04T ultrasonic', 13, weight='bold')
d.wire([(230, 490), (230, 440)], 'red'); d.text(230, 432, '5 V', 12, fill=C['red'], weight='bold')
d.wire([(265, 330), (265, 490)], 'teal')
# echo divider 1k / 2k
d.wire([(305, 330), (305, 435)], 'pink'); d.dot(305, 410, 'pink')
d.wire([(305, 435), (305, 436)], 'pink'); d.resv(305, 436, 458)
d.wire([(305, 458), (305, 490)], 'pink')
d.text(296, 452, '1 kΩ', 11, 'end')
d.wire([(305, 410), (345, 410)], 'pink'); d.wire([(345, 410), (345, 420)], 'pink')
d.resv(345, 420, 442); d.wire([(345, 442), (345, 468)], 'black')
d.wire([(345, 490), (345, 468), (382, 468)], 'black'); d.dot(345, 468); d.gnd(382, 468)
d.text(357, 436, '2 kΩ', 11, 'start')

d.notes(580, ['ECHO is a 5 V signal: the 1 kΩ / 2 kΩ divider brings',
              'it to 3.3 V before it reaches GPIO7.',
              'DS18B20 wires: red = VCC, yellow = DATA, black = GND.',
              'All ground symbols are the same GND wire.',
              '5 V = output of MT3608 #1 (diagram 2).'])
d.legend([('3.3 V', 'orange'), ('5 V', 'red'), ('GND', 'black'), ('signal', 'blue')])
d.save('03-water-node-digital.svg')
