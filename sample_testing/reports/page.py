from PSVG import Document, Font, Rect, Text, Table
from logo import logo

font500 = Font('JetBrains Mono', '500')
font600 = Font('JetBrains Mono', '600')
font700 = Font('JetBrains Mono', '700')
font800 = Font('JetBrains Mono', '800')


class Header:
    address: str = "13 Children's Way R2109"
    city: str = "Little Rock"
    state: str = "AR"
    zipcode: str = "72202"
    director: str = "Chales P. Kokes, MD"
    phone: str = "800.647.1043"
    fax: str = "888.977.1335"
    clia: str = "04D2132412"
    iso: str = "ALI-419-T"

    def get_header(self):
        text = Text(font500, "", 9)
        data = [[self.address],
                [f'{self.city}, {self.state} {self.zipcode}'],
                [f'Lab Director: {self.director}'],
                [f'Lab Phone: {self.phone}'],
                [f'Lab Fax: {self.fax}'],
                [f'CLIA: {self.clia}'],
                [f'ISO/IEC 17025: {self.iso}'], ]
        table = Table(text, data, w=200, h=250)
        for box in table.boxes.values():
            box.alignment = box.left
        table.set_row_height(100/7)
        table.even_col_width(200)
        table.set()

        return table


class Page(Document):
    def __init__(self, title: str):
        super().__init__()

        self._title = title

        self.root.w = 850
        self.root.h = 1100
        self.background()
        self.logo()
        self.title()
        self.header()

    def background(self):
        background = Rect(0, 0, self.root.w, self.root.h,
                          fill=(255, 255, 255), fill_opacity=1)
        self.addChild(background)

    def logo(self):
        svg = logo(100)
        svg.x=700
        svg.y=50
        self.addChild(svg.root)

    def title(self):
        title = Text(font700, self._title, 30, 50, 100, baseline='central')
        self.addChild(title)

    def header(self):
        header = Header()
        svg = header.get_header()
        svg.x = 500
        svg.y = 50
        self.addChild(svg.root)

p = Page("Page Title")

with open('test.svg', 'w') as file:
    file.write(p.construct())