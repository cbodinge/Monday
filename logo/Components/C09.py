from PSVG import Path
from .points import hex1


class C09(Path):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        h = hex1.pts
        self.points = [
            ('M', h[0][0], h[0][1]),
            ('L', h[1][0], h[1][1]),
            ('L', hex1.cx, hex1.cy),
            ('L', h[5][0], h[5][1]),
            ('L', h[0][0], h[0][1])
        ]

        self.fill = (64, 119, 177)
        self.fill_opacity = 1
