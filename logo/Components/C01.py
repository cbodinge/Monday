from PSVG import Path
from .points import hex2


class C01(Path):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        h = hex2.pts
        self.points = [
            ('M', h[4][0], h[4][1]),
            ('L', h[5][0], h[5][1]),
            ('L', hex2.cx, hex2.cy),
            ('L', h[3][0], h[3][1]),
            ('L', h[4][0], h[4][1])
        ]

        self.fill = (216, 216, 216)
        self.fill_opacity = 1
