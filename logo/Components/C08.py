from PSVG import Path
from .points import hex1


class C08(Path):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        h = hex1.pts
        self.points = [
            ('M', h[4][0], h[4][1]),
            ('L', h[5][0], h[5][1]),
            ('L', hex1.cx, hex1.cy),
            ('L', h[3][0], h[3][1]),
            ('L', h[4][0], h[4][1])
        ]

        self.fill = (91, 147, 197)
        self.fill_opacity = 1
