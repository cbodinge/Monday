from datetime import datetime

from API import POST, Query, Mutation


def rename_new_item(item_id, accession):
    m = Mutation()
    s = '''mutation {
      change_multiple_column_values(item_id:%s, board_id:8479058626, column_values: "{\\"name\\" : \\"%s\\"}") {
        id
      }
    }''' % (item_id, accession.id)

    m.execute(s)
