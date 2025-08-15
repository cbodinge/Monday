from PSVG import Path
from .points import hex1


class C10(Path):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        h = hex1.pts
        self.points = [
            ('M', h[3][0], h[3][1]),
            ('L', hex1.cx, hex1.cy),
            ('L', h[1][0], h[1][1]),
            ('L', h[2][0], h[2][1]),
            ('L', h[3][0], h[3][1])
        ]

        self.fill = (35, 93, 135)
        self.fill_opacity = 1
