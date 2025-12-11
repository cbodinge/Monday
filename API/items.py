from MondayAPI.Query import Query


def get_all_items(q: Query):
    data = q.execute()
    items = data.data.boards[0].items_page.items
    cursor = data.data.boards[0].items_page.cursor

    while True:
        data, cursor = _next_page(q, cursor)
        items.extend(data.data.next_items_page.items)
        if cursor is None:
            break

    return items


def _next_page(query: Query, cursor):
    q = Query()
    q.next_items_page.items.copy_active(query.boards.items_page.items)
    q.next_items_page.cursor.activate()
    q.next_items_page.arguments = {'cursor': f'"{cursor}"'}

    data = q.execute()
    cursor = data.data.next_items_page.cursor

    return data, cursor


def get_some_items(board_id: int, query_params: str):
    q = Query()
    q.boards.items_page.items.name.activate()
    q.boards.items_page.items.id.activate()
    q.boards.items_page.cursor.activate()
    q.boards.arguments = {'ids': [board_id]}
    q.boards.items_page.arguments = {'limit': 50,
                                     'query_params': query_params}

    data = q.execute()
    items = data.data.boards[0].items_page.items
    cursor = data.data.boards[0].items_page.cursor

    while True:
        data, cursor = _next_page(cursor)
        items.extend(data.data.next_items_page.items)
        if cursor is None:
            break

    return {i.id: i.name for i in items}
