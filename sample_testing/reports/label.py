from PSVG import Document, Text, Path, Section, Rect
from ..structures import Accession
import qrcode
from qrcode.image.svg import SvgPathImage
from fonts import f600

class Label(Document):
    def __init__(self, accession: Accession):
        super().__init__(w=500, h=250)
        self.accession = accession
        self._fields()

    def _code(self):
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=0,
            image_factory=SvgPathImage
        )
        qr.add_data(self.accession.id)
        qr.make(fit=True)
        svg = qr.make_image()
        points = svg.path.attrib['d']

        qr = Section(25, 25, svg.width, svg.width)
        path = Path(fill_opacity=1, fill=(0, 0, 0))
        path.points = points
        qr.addChild(path)
        qr.root.xscale=200/svg.width
        qr.root.yscale=200/svg.width

        self.addChild(qr.root)

    def _text(self, string: str):
        return Text(f600, text=string, size=18, baseline='hanging' ,anchor='start',
                    fill=(0, 0, 0), fill_opacity=1, x=250)

    def _fields(self):
        self._set_fields(self._text(f'id: {self.accession.id}'), 25)
        self._set_fields(self._text(f'first: {self.accession.first_name}'), 55)     # First Name
        self._set_fields(self._text(f'last: {self.accession.last_name}'), 85)      # Last Name

        if self.accession.dob is not None:
            _id2 = self._text(self.accession.dob.strftime("%d/%m/%Y"))


    def _set_fields(self, field: Text, y: float):
        field.x = 250
        field.y = y

        self.addChild(field)




    def code(self):
        self._code()



