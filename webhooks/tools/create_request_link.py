from API import Mutation


def request_link(item_id, board_id):
    url = f'https://forms.monday.com/forms/68d7bca8cc1a1af90e6e948a7eb7d5cf?r=use1&ref={item_id}'

    s = '''mutation {
      change_simple_column_value(item_id: %s, board_id: %s, column_id: "link_mkr0zde1" value: "%s") {
        id
      }
    }''' % (item_id, board_id, f'{url} Request')

    Mutation().execute(s)

