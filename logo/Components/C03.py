from PSVG import Path
from .points import hex3


class C03(Path):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        h = hex3.pts
        self.points = [
            ('M', hex3.cx, hex3.cy),
            ('L', h[4][0], h[4][1]),
            ('L', h[5][0], h[5][1]),
            ('L', h[0][0], h[0][1]),
            ('L', hex3.cx, hex3.cy)
        ]

        self.fill = (182, 182, 182)
        self.fill_opacity = 1
