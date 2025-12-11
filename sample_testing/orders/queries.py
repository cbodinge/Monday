from . import get_order, Order
from MondayAPI.Query import Query
from API import get_all_items


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
    query.boards.items_page.cursor.activate()

    return query


def all_finalized_orders() -> list[Order]:
    query = standard_query()
    query.boards.arguments = {'ids': '[9365780770]'}
    items = get_all_items(query)

    return [get_order(item) for item in items]


def all_active_orders() -> list[Order]:
    query = standard_query()
    query.boards.arguments = {'ids': '[9365193754]'}
    items = get_all_items(query)

    return [get_order(item) for item in items]


def get_order_by_item_id(item_id: int) -> Order:
    query = standard_query()
    query.boards.items_page.items.arguments['ids'] = f'[{item_id}]'
    item = query.execute()

    try:
        item = item.data.boards.items_page.items[0]
    except (IndexError, AttributeError):
        item = None

    return get_order(item)