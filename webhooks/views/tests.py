from django.http import HttpRequest, HttpResponse, JsonResponse
from API import Query, POST
from . import pending_orders, parc_projects, consulting_projects



def get_board_list(request: HttpRequest) -> HttpResponse:
    q = Query()
    q.boards.id.activate()
    q.boards.name.activate()

    post = POST()
    items = post.execute(q).json()['data']

    return JsonResponse(items)


def test(request: HttpRequest) -> HttpResponse:
    q = Query()
    q.boards.id.activate()
    q.boards.items_page.items.name.activate()
    q.boards.items_page.items.id.activate()
    q.boards.arguments = {'ids': [parc_projects, consulting_projects]}
    post = POST()
    items = post.execute(q).json()['data']

    # items = [(int(i['id']), i['name']) for i in items]

    return JsonResponse(items)