from API import Mutation
from datetime import datetime

def set_accession(item_id: int, created_at: datetime) -> None:
    s = '''mutation {
      change_multiple_column_values(item_id: %s, board_id:8479058626, column_values: "{\\"name\\" : \\"%s\\"}") {
        id
      }
    }''' % (item_id, created_at.strftime("%y-%m-%d-%H-%M-%S"))

    return Mutation().execute(s)