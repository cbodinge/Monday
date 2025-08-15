from datetime import datetime, date

class Action:
    analyst: str
    action: str
    date: datetime

    def to_table_row(self):
        return [self.action, 'Marina Avram',
                self.date.strftime("%Y/%m/%d %H:%M:%S") if self.date != datetime.min else '']

class Order:
    accession: str
    first_name: str
    last_name: str
    dob: date
    actions: list[Action]
    other_id: str
    matrix: str
    collection_time: datetime
    collected_by: str
    medications: list[str]
    other_info: list[str]
    order_time: datetime
    client: str

