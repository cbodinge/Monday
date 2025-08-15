from .page import Page, font600
from PSVG import Text
from ..orders import Order
from .svg2pdf import process


class Requisition(Page):
    def __init__(self, order: Order):
        super().__init__('Requisition')
        self.order = order
        self._y = 200
        self._dy = 45
        self.info()

    def add_text(self, label: str, text: str):
        if text != '':
            new_text = Text(font600, f'{label}: {text}', 20, x=50, y=self._y)
            self._y += self._dy
            self.addChild(new_text)

    def add_testing_menu(self):
        testing_menu = ['Fentanyl', 'MDEA', 'MDPV', 'Sufentanil', 'Xylazine']
        for drug in testing_menu:
            new_text = Text(font600, f'     - {drug}', 20, x=50, y=self._y)
            self._y += .75*self._dy
            self.addChild(new_text)

    def info(self):
        self.add_text('ID', self.order.accession)
        self.add_text('Other ID', self.order.other_id)
        self.add_text('Patient', f'{self.order.last_name}, {self.order.first_name}')
        self.add_text('DOB', self.order.dob.strftime('%m/%d/%Y'))
        self.add_text('Matrix', self.order.matrix)
        self.add_text('Collection Time', self.order.collection_time.strftime('%m/%d/%Y %H:%M'))
        self.add_text('Collected By', self.order.collected_by)
        self.add_text('Client', self.order.client)

        self._y += self._dy
        self.add_text('Ordered Tests', ' ')
        self.add_testing_menu()

    def pdf(self):
        svg = self.construct()
        pdf = process(svg)

        with open(f'exports/({self.order.accession}) requisition.pdf', 'wb') as file:
            file.write(pdf)
