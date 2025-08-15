from datetime import datetime
import json

from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect

from API import Query, POST
# from .tests import test as t
from .tools.sample_testing_rename_new_item import rename_new_item
from .tools.create_request_link import request_link
from .tools.set_reference import set_reference
from .tools.update_accession import set_accession


from sample_testing.reports.label import Label
from sample_testing import Accession

class Test:
    def __init__(self):
        self.last_used=None
        self.accession=None

    def get_accession(self, data):
        now = datetime.now()
        _id = now.strftime("%y-%m-%d-%H-%M-%S")
        cv = data['event']['columnValues']

        date = datetime.strptime(cv['date_mkn4k66s']['date'], '%Y-%m-%d')
        accession = Accession(_id=_id,
                              first_name=cv['short_text_mkn4grfw']['value'],
                              last_name=cv['short_text_mkn4nm6j']['value'],
                              dob=date)
        self.accession = accession

t = Test()

with open('./webhooks/templates/display.html', 'r') as file:
    wrapper = file.read()

with open('./webhooks/templates/Label.html', 'r') as file:
    label_wrapper = file.read()

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
        t.get_accession(payload)
        rename_new_item(item_id, t.accession)

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


@csrf_exempt
def report_forwarding(request):
    svg = Label(t.accession).construct()

    page = str(label_wrapper) % (svg,)
    page.encode('utf8')

    return HttpResponse(page)


def update_accessions(request: HttpRequest) -> HttpResponse:
    q = Query()
    q.boards.items_page.items.created_at.activate()
    q.boards.items_page.items.id.activate()
    q.boards.items_page.items.name.activate()

    pending_orders=8479058626

    q.boards.arguments = {'ids': pending_orders}

    post = POST()
    items = post.execute(q)['data']['boards'][0]['items_page']['items']

    for item in items:
        set_accession(int(item['id']), datetime.fromisoformat(item['created_at']))

    return HttpResponse(str(items))

def test(request: HttpRequest) -> HttpResponse:
    return HttpResponse('')

