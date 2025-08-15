from datetime import date

class Accession:
    id: str
    first_name: str
    last_name: str
    dob: date
    other_id: str

    tests = list[str]

    def __init__(self, _id: str, first_name: str='', last_name: str='', dob: date=None, other_id: str=''):
        self.id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.other_id = other_id



