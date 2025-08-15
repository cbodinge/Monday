from PSVG import Path
from .points import hex4


class C06(Path):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        h = hex4.pts
        self.points = [
            ('M', hex4.cx, hex4.cy),
            ('L', h[2][0], h[2][1]),
            ('L', h[3][0], h[3][1]),
            ('L', h[4][0], h[4][1]),
            ('L', hex4.cx, hex4.cy)
        ]

        self.fill = (182, 182, 182)
        self.fill_opacity = 1
