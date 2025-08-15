from PSVG import Path
from .points import hex3


class C04(Path):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        h = hex3.pts
        self.points = [
            ('M', hex3.cx, hex3.cy),
            ('L', h[0][0], h[0][1]),
            ('L', h[1][0], h[1][1]),
            ('L', h[2][0], h[2][1]),
            ('L', hex3.cx, hex3.cy)
        ]

        self.fill = (158, 158, 158)
        self.fill_opacity = 1
