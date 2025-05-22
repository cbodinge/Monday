import json

from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect

from API import Query, POST
# from .tests import test as t
from .tools.sample_testing_rename_new_item import rename_new_item
from .tools.create_request_link import request_link
from .tools.set_reference import set_reference


# Create your views here.

def _payload(request):
    payload = None
    try:
        payload = json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        return payload, HttpResponseBadRequest("Invalid JSON")

    # Handle the handshake
    if "challenge" in payload:
        return payload, JsonResponse({"challenge": payload["challenge"]})

    return payload, JsonResponse(payload, status=200)



@csrf_exempt
def hook(request):
    payload, response = _payload(request)
    if request.method == 'POST':
        item_id = payload['event']['pulseId']
        rename_new_item(item_id)

    print(json.dumps(payload, indent=2))

    return response


@csrf_exempt
def update_reference(request):
    payload, response = _payload(request)
    print(json.dumps(payload, indent=2))

    if request.method == 'POST':
        item_id = payload['event']['pulseId']
        set_reference(item_id, 9169256232)

    return response


@csrf_exempt
def create_request_link(request):
    print(request)
    payload, response = _payload(request)

    if request.method == 'POST':
        item_id = payload['event']['pulseId']
        request_link(item_id, '6822391121')

    return response


def test(request: HttpRequest) -> HttpResponse:
    q = Query()
    q.boards.items_page.items.id.activate()
    q.boards.arguments = {'ids': 6822391121}
    q.boards.items_page.arguments = {'limit': 100}
    a=POST().execute(q)

    items = [i['id'] for i in a['data']['boards'][0]['items_page']['items']]



    return JsonResponse({'i': items}, status=200)

