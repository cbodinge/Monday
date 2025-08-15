from . import get_order, Order
from API import POST, Query


def standard_query() -> Query:
    query = Query()

    query.boards.items_page.items.name.activate()
    query.boards.items_page.items.column_values.column.title.activate()
    query.boards.items_page.items.column_values.value.activate()
    query.boards.items_page.items.column_values.text.activate()

    query.boards.items_page.items.subitems.column_values.column.title.activate()
    query.boards.items_page.items.subitems.column_values.value.activate()
    query.boards.items_page.items.subitems.column_values.text.activate()
    query.boards.items_page.items.subitems.name.activate()

    return query


def all_finalized_orders() -> list[Order]:
    post = POST()
    query = standard_query()

    query.boards.arguments = {'ids': '[9365780770]'}

    try:
        items = post.execute(query)['data']['boards'][0]['items_page']['items']
    except IndexError:
        items = []

    return [get_order(item) for item in items]


def get_order_by_item_id(item_id: int) -> Order:
    post = POST()
    query = standard_query()

    query.boards.items_page.items.arguments['ids'] = f'[{item_id}]'

    try:
        items = post.execute(query)['data']['boards'][0]['items_page']['items']
    except IndexError:
        items = []

    return get_order(items[0])