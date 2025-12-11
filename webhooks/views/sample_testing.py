from . import pending_orders, csrf_exempt, logger
from .tools import payload
from API import Mutation, POST, Query
from datetime import datetime
from django.http import HttpResponse, HttpRequest
from requests.exceptions import HTTPError, RequestException
from requests import Response


def set_order_id(item_id: int, created_at: datetime) -> None:
    response = Response()

    try:
        s = '''mutation {
          change_multiple_column_values(item_id: %s, board_id:%s, column_values: "{\\"name\\" : \\"%s\\"}") {
            id
          }
        }''' % (item_id, pending_orders, created_at.strftime("%y-%m-%d-%H-%M-%S"))

        response = Mutation().execute(s)
        response.raise_for_status()

    except HTTPError:
        logger.error(f'item_id: {item_id} - set_order_id failed with code {response.status_code}.')

    except RequestException as err:
        logger.error(f"item_id: {item_id} - set_order_id failed: {err}")


def get_all_pending_orders() -> list:
    response = HttpResponse(status=200)

    try:
        q = Query()
        q.boards.items_page.items.created_at.activate()
        q.boards.items_page.items.id.activate()
        q.boards.items_page.items.name.activate()

        q.boards.arguments = {'ids': pending_orders}

        response = POST().execute(q)
        response.raise_for_status()
        return response.json()['data']['boards'][0]['items_page']['items']

    except HTTPError:
        logger.error(f'get_all_pending_orders failed with code {response.status_code}.')
        return []

    except (RequestException, KeyError) as err:
        logger.error(f"get_all_pending_orders failed: {err}")
        return []


@csrf_exempt
def rename_new_order(request: HttpRequest) -> HttpResponse:
    data, response = payload(request)
    if request.method == 'POST':
        item_id = data['event']['pulseId']
        dt = datetime.fromisoformat(data['event']['triggerTime'])
        set_order_id(int(item_id), dt)
    return response


@csrf_exempt
def rename_all_pending_orders(request: HttpRequest) -> HttpResponse:
    """
    Convenience Function to rename all currently active pending orders by their original created time.
    """

    items = get_all_pending_orders()
    for item in items:
        set_order_id(int(item['id']), datetime.fromisoformat(item['created_at']))

    return HttpResponse(str(items))
