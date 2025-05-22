from API import Mutation, POST, Query


def set_reference(item_id, board_id):
    try:
        ref = get_reference(item_id)
        if reference_exists(ref):
            ref = 'column_values: "{\\"board_relation_mkr3qxev\\" : {\\"item_ids\\" : [\\"%s\\"]}}"' % ref
        else:
            ref = 'column_values: "{\\"board_relation_mkr3qxev\\" : null}"'
    except KeyError:
        return

    s = '''mutation {
      change_multiple_column_values(
      item_id: %s, 
      board_id: %s, 
      %s
      ) {
        id
      }
    }''' % (item_id, board_id, ref)

    return Mutation().execute(s)


def get_reference(item_id):
    q = Query()
    q.items.column_values.column.title.activate()
    q.items.column_values.text.activate()
    q.items.column_values.id.activate()
    q.items.column_values.arguments = {'ids': '"short_textly7br80r"'}
    q.items.arguments = {'ids': item_id}

    data = POST().execute(q)
    return data['data']['items'][0]['column_values'][0]['text']


def reference_exists(item_id):
    q = Query()
    q.items.id.activate()
    q.items.arguments = {'ids': item_id}

    data = POST().execute(q)
    return len(data['data']['items']) > 0