from PSVG import Path
from .points import hex2

class C02(Path):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        h = hex2.pts
        self.points = [
            ('M', h[5][0], h[5][1]),
            ('L', h[0][0], h[0][1]),
            ('L', hex2.cx, hex2.cy),
            ('L', h[5][0], h[5][1]),
        ]

        self.fill = (188, 188, 188)
        self.fill_opacity = 1
