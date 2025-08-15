from PSVG import Document, Text, Rect

from ..structures import Accession
from .qr import qr
from fonts import f600

def _text(string: str) -> Text:
    return Text(f600, text=string, size=18, baseline='hanging', anchor='start',
                fill=(0, 0, 0), fill_opacity=1, x=250)

class Label(Document):
    def __init__(self, accession: Accession):
        super().__init__(w=500, h=250)
        self.accession = accession
        self._background()
        self._fields()
        self._code()

    def _background(self):
        background = Rect(fill=(255, 255, 255), fill_opacity=1)
        self.addChild(background)

    def _code(self):
        _qr = qr(self.accession)
        _qr.x=25
        _qr.y=25
        self.addChild(_qr.root)

    def _fields(self):
        self._set_fields(_text(f'id: {self.accession.id}'), 25)
        self._set_fields(_text(f'first: {self.accession.first_name}'), 55)
        self._set_fields(_text(f'last: {self.accession.last_name}'), 85)

        if self.accession.dob is not None:
            _id2 = _text(self.accession.dob.strftime("%d/%m/%Y"))


    def _set_fields(self, field: Text, y: float):
        field.x = 250
        field.y = y

        self.addChild(field)
