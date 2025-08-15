from math import cos, sin, pi
from PSVG import Path


class Hexagon:
    def __init__(self, cx, cy, r):
        self.cx = cx
        self.cy = cy
        self.r = r
        self._rotation = 30

        self.x = []
        self.y = []
        self.pts = []

        self.set()


    def set(self):
        self.x = [self._x(i*60) for i in range(6)]
        self.y = [self._y(i*60) for i in range(6)]
        self.pts = list(zip(self.x, self.y))

    def _x(self, degrees):
        theta = (degrees + self._rotation) * pi / 180
        return self.cx + self.r * cos(theta)

    def _y(self, degrees):
        theta = (degrees + self._rotation) * pi / 180
        return self.cy + self.r * sin(theta)

    @property
    def rotation(self):
        return self._rotation

    @rotation.setter
    def rotation(self, value):
        self._rotation = value
        self.set()

    def translate(self, dx, dy):
        self.cx += dx
        self.cy += dy
        self.set()

    def path(self):
        p = Path(stroke_width=3)

        p.points = [
            ('M', self.x[0], self.y[0]),
            ('L', self.x[1], self.y[1]),
            ('L', self.x[2], self.y[2]),
            ('L', self.x[3], self.y[3]),
            ('L', self.x[4], self.y[4]),
            ('L', self.x[5], self.y[5]),
            ('L', self.x[0], self.y[0]),
        ]

        return p

cx = 500
cy = 500
r = 250     # hexagon side length
s = 50      # space between inner hexagon and outer components

hex0 = Hexagon(cx, cy, r + s)
hex1 = Hexagon(cx, cy, r)
hex2 = Hexagon(cx, cy-(r + s), r)
hex3 = Hexagon(hex0.x[0], hex0.y[0], r)
hex4 = Hexagon(hex0.x[2], hex0.y[2], r)

hexes = [hex0, hex1, hex2, hex3, hex4]

top = hex1.y[4]
bot = hex3.y[1]
dy = ((top + bot) / 2 - cy)

for h in hexes:
    h.translate(0, dy)
