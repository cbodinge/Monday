from PSVG import Section
from .Components import *

def main(size=1000):

    logo = Section(x=0, y=0, w=1000, h=1000)

    logo.root.xscale = size/1000
    logo.root.yscale = size/1000

    components = [
        C01(),
        C02(),
        C03(),
        C04(),
        C05(),
        C06(),
        C07(),
        C08(),
        C09(),
        C10()
    ]

    for component in components:
        logo.addChild(component)

    return logo
