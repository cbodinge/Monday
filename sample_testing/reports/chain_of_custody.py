from .page import Page, font600
from PSVG import Text, Table
from ..orders import Order
from .svg2pdf import process


class ChainOfCustody(Page):
    def __init__(self, order: Order):
        super().__init__('Chain of Custody')
        self.order = order
        self.patient_info()
        self.actions()

    def patient_info(self):
        accession = Text(font600, f'ID: {self.order.accession}', 16, x=50, y=200)
        other_id = Text(font600, f'Other ID: {self.order.other_id}', 16, x=50, y=220)
        patient_name = Text(font600, f'Patient: {self.order.last_name}, {self.order.first_name}', 16, x=50, y=240)
        patient_dob = Text(font600, f'DOB: {self.order.dob.strftime('%Y-%m-%d')}', 16, x=50, y=260)

        self.addChild(accession)
        self.addChild(other_id)
        self.addChild(patient_name)
        self.addChild(patient_dob)

    def actions(self):
        text = Text(font600, f'', 12)
        data = [action.to_table_row() for action in self.order.actions]
        data.insert(0, ['', '', ''])
        data.insert(0, ['Action', 'Analyst', 'Date/Time'])
        table = Table(text, data, w=750)

        table.set_row_height(20)
        table.weighted_col_width(750, [.5, .2, .3])

        for box in table.boxes.values():
            box.alignment = box.left

        for i in table.r_rng:
            box = table.boxes[(i, 0)]
            box.alignment = box.left

            box = table.boxes[(i, 1)]
            box.alignment = box.center

            box = table.boxes[(i, 2)]
            box.alignment = box.right

        table.w = 750
        table.x = 50
        table.y = 300
        table.set()

        self.addChild(table.root)

    def pdf(self):
        svg = self.construct()
        pdf = process(svg)

        with open(f'exports/({self.order.accession}) chain of custody.pdf', 'wb') as file:
            file.write(pdf)
