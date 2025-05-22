from datetime import datetime

from API import POST, Query, Mutation


def rename_new_item(item_id):
    now = datetime.now()
    name = now.strftime("%y-%m-%d-%H-%M-%S")

    m = Mutation()
    s = '''mutation {
      change_multiple_column_values(item_id:%s, board_id:8479058626, column_values: "{\\"name\\" : \\"%s\\"}") {
        id
      }
    }''' % (item_id, name)

    m.execute(s)
