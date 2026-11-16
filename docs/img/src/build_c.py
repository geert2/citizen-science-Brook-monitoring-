from _lib import D, C

# ------------------------------------------------------------------ 6 GATEWAY
d = D(420, 580, '6 · Gateway (mains USB)')
d.box(30, 60, 150, 56, '#fff8e6', '#555555'); d.text(105, 85, 'Water node', 14, weight='bold'); d.text(105, 103, 'at the brook', 12)
d.wire([(105, 116), (105, 205), (230, 205), (230, 250)], 'teal', 3.5, '9 7')
d.text(192, 196, 'LoRa radio 869.5 MHz', 12, 'middle', 'bold', C['teal'])
d.wire([(330, 250), (330, 150)], 'black', 5); d.dot(330, 146, 'black', 7)
d.text(330, 112, '868 MHz antenna', 13, weight='bold'); d.text(330, 128, 'attach BEFORE power!', 11, fill=C['red'])
d.box(180, 250, 200, 90, '#e6f7ea', '#2a9d3f')
d.text(280, 284, 'Heltec V3', 14, weight='bold'); d.text(280, 302, 'gateway · always listening', 12); d.text(280, 322, 'antenna on the SMA socket', 11, fill='#555555')
d.pin(330, 250, 'black')
d.box(30, 430, 140, 50, '#eef3f8', '#555555'); d.text(100, 451, '5 V USB charger', 12, weight='bold'); d.text(100, 468, 'mains', 11)
d.wire([(100, 430), (100, 385), (230, 385), (230, 340)], 'red', 5); d.pin(230, 340, 'red')
d.text(165, 377, 'USB-C cable', 11, fill='#555555')
d.wire([(340, 340), (340, 430)], 'blue', 3.5, '9 7'); d.pin(340, 340, 'blue')
d.text(352, 392, 'Wi-Fi', 12, 'start', 'bold', C['blue'])
d.box(270, 430, 130, 50, '#e8f1ff', '#1d6fdc'); d.text(335, 451, 'Router', 12, weight='bold'); d.text(335, 468, '→ Home Assistant', 11)
d.notes(515, ['Dashed lines = wireless. Never power the Heltec', 'without its antenna attached.'])
d.legend([('power', 'red'), ('radio', 'teal'), ('Wi-Fi', 'blue')])
d.save('06-gateway.svg')

# ------------------------------------------------------------------ 7 OPTIONAL SWITCH
d = D(420, 830, '7 · Optional: separate power switch')
d.text(210, 52, 'Only if Vext is not enough (see wiring.md)', 12, fill='#555555')

def schematic(oy, title, q1, q2, rg, rb_name, r2_label, r3_label, notes):
    # q1/q2 = (name, part, type, pin letters top/left/bottom)
    d.text(18, oy, title, 13, 'start', 'bold')
    d.wire([(40, oy + 28), (360, oy + 28)], 'red', 5); d.text(40, oy + 20, 'BAT +', 11, 'start', fill=C['red'])
    # Q1 (high-side)
    d.box(230, oy + 70, 100, 70, '#eef3f8', '#555555')
    d.text(280, oy + 95, q1[0], 13, weight='bold'); d.text(280, oy + 112, q1[1], 11); d.text(280, oy + 127, q1[2], 10)
    d.text(294, oy + 63, q1[3][0], 11, 'start', 'bold'); d.text(238, oy + 109, q1[3][1], 11, 'start', 'bold'); d.text(294, oy + 156, q1[3][2], 11, 'start', 'bold')
    d.pin(280, oy + 70, 'red'); d.pin(230, oy + 105, 'grey'); d.pin(280, oy + 140, 'red')
    d.wire([(280, oy + 28), (280, oy + 70)], 'red'); d.dot(280, oy + 28, 'red')
    # R1 from rail to gate node
    d.wire([(150, oy + 28), (150, oy + 48)], 'red'); d.resv(150, oy + 48, oy + 70); d.dot(150, oy + 28, 'red')
    d.wire([(150, oy + 70), (150, oy + 105), (230, oy + 105)], 'grey'); d.dot(150, oy + 105, 'grey')
    d.text(141, oy + 64, 'R1 100 kΩ', 11, 'end')
    # path to Q2 top (with R2 for the BJT version)
    if r2_label:
        d.wire([(150, oy + 105), (150, oy + 118)], 'grey'); d.resv(150, oy + 118, oy + 140); d.wire([(150, oy + 140), (150, oy + 165)], 'grey')
        d.text(141, oy + 134, r2_label, 11, 'end')
    else:
        d.wire([(150, oy + 105), (150, oy + 165)], 'grey')
    # Q2 (driver)
    d.box(100, oy + 165, 100, 70, '#eef3f8', '#555555')
    d.text(150, oy + 190, q2[0], 13, weight='bold'); d.text(150, oy + 207, q2[1], 11); d.text(150, oy + 222, q2[2], 10)
    d.text(164, oy + 158, q2[3][0], 11, 'start', 'bold'); d.text(108, oy + 204, q2[3][1], 11, 'start', 'bold'); d.text(164, oy + 252, q2[3][2], 11, 'start', 'bold')
    d.pin(150, oy + 165, 'grey'); d.pin(100, oy + 200, 'pink'); d.pin(150, oy + 235, 'black')
    d.wire([(150, oy + 235), (150, oy + 262)], 'black'); d.gnd(150, oy + 262)
    # GPIO33 -> series resistor -> gate node -> pulldown
    d.text(18, oy + 168, 'GPIO33', 11, 'start', 'bold', C['pink'])
    d.wire([(20, oy + 200), (34, oy + 200)], 'pink'); d.resh(34, 58, oy + 200); d.wire([(58, oy + 200), (100, oy + 200)], 'pink')
    d.text(46, oy + 190, rg, 10)
    d.dot(78, oy + 200, 'pink'); d.wire([(78, oy + 200), (78, oy + 222)], 'pink'); d.resv(78, oy + 222, oy + 246)
    d.wire([(78, oy + 246), (78, oy + 262)], 'black'); d.gnd(78, oy + 262)
    d.text(70, oy + 238, r3_label, 11, 'end')
    # output
    d.wire([(280, oy + 140), (280, oy + 205)], 'red')
    d.text(280, oy + 226, 'to MT3608 IN +', 12, weight='bold'); d.text(280, oy + 242, '(both modules)', 11)
    for i, t in enumerate(notes):
        d.text(18, oy + 300 + i * 15, t, 11, 'start', fill='#555555')

schematic(82, 'Option B · AO3401 (P-MOSFET) + 2N7002',
          ('Q1', 'AO3401', 'P-MOSFET', ('S', 'G', 'D')), ('Q2', '2N7002', 'N-MOSFET', ('D', 'G', 'S')),
          '100 Ω', 'R3', None, 'R3 100 kΩ',
          ['R2 = 100 Ω at the Q2 gate, R3 keeps Q2 off in sleep.', 'GPIO33 HIGH = boosters ON.'])
schematic(440, 'Option C · BC327 (PNP) + BC337 (NPN)',
          ('Q3', 'BC327-40', 'PNP', ('E', 'B', 'C')), ('Q4', 'BC337-40', 'NPN', ('C', 'B', 'E')),
          '4.7 kΩ', 'R4', 'R2 330 Ω', 'R4 100 kΩ',
          ['R3 = 4.7 kΩ at the Q4 base, R4 keeps Q4 off in sleep.', 'Drops about 0.3 V: fine for the MT3608.'])
d.legend([('+ battery', 'red'), ('GND', 'black'), ('GPIO33', 'pink'), ('internal', 'grey')])
d.save('07-optional-switch.svg')
