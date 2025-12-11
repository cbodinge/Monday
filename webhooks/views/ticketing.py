from . import csrf_exempt, logger, consulting_projects, parc_projects
from .tools import payload
from API import Mutation, POST, Query
from requests import Response
from requests.exceptions import HTTPError, RequestException
from django.http import HttpResponse


def request_link(item_id: int, board_id: int) -> None:
    response = Response()

    column_ids = {consulting_projects: 'link_mkr0zde1',
                  parc_projects: 'link_mkr0zde1'}

    column_id = column_ids.get(board_id)

    try:
        url = f'https://forms.monday.com/forms/68d7bca8cc1a1af90e6e948a7eb7d5cf?r=use1&ref={item_id}'

        s = '''mutation {
          change_simple_column_value(item_id: %s, board_id: %s, column_id: "%s" value: "%s") {
            id
          }
        }''' % (item_id, board_id, column_id, f'{url} Request')

        response = Mutation().execute(s)
        response.raise_for_status()

        logger.info(f'Request Link created for item {item_id} and board {board_id}')

    except HTTPError:
        logger.error(f'item_id: {item_id} - request_link failed with code {response.status_code}.')

    except RequestException as err:
        logger.error(f"item_id: {item_id} - request_link failed: {err}")


@csrf_exempt
def create_request_link(request):
    data, response = payload(request)

    if request.method == 'POST':
        item_id = int(data['event']['pulseId'])
        board_id = int(data['event']['boardId'])
        request_link(item_id, board_id)

    return response


@csrf_exempt
def update_all_request_links(request):
    boards = [parc_projects, consulting_projects]
    q = Query()
    q.boards.id.activate()
    q.boards.items_page.items.name.activate()
    q.boards.items_page.items.id.activate()
    q.boards.arguments = {'ids': boards}

    post = POST()
    data = post.execute(q).json()['data']

    for board in data['boards']:
        for item in board['items_page']['items']:
            request_link(item['id'], int(board['id']))

    return HttpResponse()
