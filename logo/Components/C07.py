from PSVG import Path
from .points import hex2


class C07(Path):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        h = hex2.pts
        self.points = [
            ('M', h[3][0], h[3][1]),
            ('L', h[2][0], h[2][1]),
            ('L', hex2.cx, hex2.cy),
            ('L', h[3][0], h[3][1]),
        ]

        self.fill = (188, 188, 188)
        self.fill_opacity = 1