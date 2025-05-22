from API import POST, Query, Mutation

def rename_new_item(current_item):
    q = Query()
    q.boards.items_page.items.column_values.activate()

    print(POST().execute(q))

    m = Mutation()
    s = '''mutation {
      change_column_values(item_id:%s, board_id:9169256232, column_values: "{\\"Reference\\" : \\"%s\\"}") {
        id
      }
    }''' % (item_id, name)

    m.execute(s)