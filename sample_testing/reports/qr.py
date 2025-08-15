from PSVG import Path, Section
from ..structures import Accession
from qrcode.image.svg import SvgPathImage
from qrcode.main import QRCode

def qr(accession: Accession, size=200):
    """
    Creates an SVG section with the qr code representing the accession id.
    """
    _qr = QRCode(
        version=1,
        box_size=10,
        border=0,
        image_factory=SvgPathImage
    )
    _qr.add_data(accession.id)
    _qr.make(fit=True)
    svg = _qr.make_image()
    points = svg.path.attrib['d']

    _qr = Section(100, 100, svg.width, svg.width)
    path = Path(fill_opacity=1, fill=(0, 0, 0))
    path.points = points
    _qr.addChild(path)
    _qr.root.xscale = size / svg.width
    _qr.root.yscale = size / svg.width

    _qr.construct()

    return _qr


def qr2(string: str, size=200):
    """
    Creates an SVG section with the qr code representing the accession id.
    """
    _qr = QRCode(
        version=1,
        box_size=10,
        border=0,
        image_factory=SvgPathImage
    )
    _qr.add_data(string)
    _qr.make(fit=True)
    svg = _qr.make_image()
    points = svg.path.attrib['d']

    _qr = Section(100, 100, svg.width, svg.width)
    path = Path(fill_opacity=1, fill=(0, 0, 0))
    path.points = points
    _qr.addChild(path)
    _qr.root.xscale = size / svg.width
    _qr.root.yscale = size / svg.width

    _qr.construct()

    return _qr