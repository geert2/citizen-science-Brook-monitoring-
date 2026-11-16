"""Tiny SVG drawing helpers used to generate the wiring diagrams (portrait, phone friendly)."""
FONT = "Helvetica, Arial, sans-serif"
C = dict(red='#d62828', black='#1f1f1f', blue='#1d6fdc', green='#2a9d3f', orange='#f08a00',
         purple='#8a3ffc', teal='#0a9396', pink='#d6336c', grey='#777777')


def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


class D:
    def __init__(self, w, h, title, desc=''):
        self.w, self.h, self.p, self.title, self.desc = w, h, [], title, desc
        self.text(w / 2, 28, title, 17, 'middle', 'bold')

    def text(self, x, y, t, size=13, anchor='middle', weight='normal', fill='#1f1f1f'):
        self.p.append(f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" '
                      f'font-weight="{weight}" fill="{fill}">{esc(t)}</text>')

    def box(self, x, y, w, h, fill='#f4f4f4', stroke='#555555', rx=8, sw=2):
        self.p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
                      f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

    def wire(self, pts, color='black', w=3.5, dash=None):
        d = ' '.join(f'{x},{y}' for x, y in pts)
        da = f' stroke-dasharray="{dash}"' if dash else ''
        self.p.append(f'<polyline points="{d}" fill="none" stroke="{C[color]}" stroke-width="{w}" '
                      f'stroke-linecap="round" stroke-linejoin="round"{da}/>')

    def dot(self, x, y, color='black', r=4.5):
        self.p.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{C[color]}"/>')

    def pin(self, x, y, color='black'):
        self.p.append(f'<circle cx="{x}" cy="{y}" r="4.5" fill="#ffffff" stroke="{C[color]}" stroke-width="2.5"/>')

    def gnd(self, x, y):
        """Ground symbol hanging below (x, y). All ground symbols are the same wire."""
        for i, half in enumerate((10, 6.5, 3)):
            yy = y + 4 + i * 5
            self.p.append(f'<line x1="{x-half}" y1="{yy}" x2="{x+half}" y2="{yy}" stroke="{C["black"]}" '
                          f'stroke-width="2.5" stroke-linecap="round"/>')

    def resv(self, x, y1, y2):
        """Vertical resistor body between y1 and y2 (leads are drawn by the caller)."""
        self.box(x - 6, y1, 12, y2 - y1, '#ffffff', '#1f1f1f', 2, 2)

    def resh(self, x1, x2, y):
        self.box(x1, y - 6, x2 - x1, 12, '#ffffff', '#1f1f1f', 2, 2)

    def legend(self, items):
        y = self.h - 22
        x = 18
        for label, col in items:
            self.p.append(f'<line x1="{x}" y1="{y-4}" x2="{x+16}" y2="{y-4}" stroke="{C[col]}" '
                          f'stroke-width="4" stroke-linecap="round"/>')
            self.text(x + 21, y, label, 11, 'start', fill='#444444')
            x += 21 + 6.4 * len(label) + 14

    def notes(self, y, lines, size=12):
        for i, t in enumerate(lines):
            self.text(18, y + i * (size + 6), t, size, 'start', fill='#333333')

    def save(self, path):
        import os
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', path)
        head = ('<?xml version="1.0" encoding="UTF-8"?>\n'
                f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
                f'width="{self.w}" height="{self.h}" font-family="{FONT}">\n'
                f'<title>{esc(self.title)}</title>\n'
                f'<rect width="100%" height="100%" fill="#ffffff"/>\n'
                f'<rect x="1.5" y="1.5" width="{self.w-3}" height="{self.h-3}" rx="10" fill="none" '
                f'stroke="#d0d0d0" stroke-width="2"/>\n')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(head + '\n'.join(self.p) + '\n</svg>\n')
