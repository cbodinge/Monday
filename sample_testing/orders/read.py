from . import Order, Action
from API import get_date, get_time


def get_action(subitem):
    action = Action()
    action.action = subitem['name']
    action.analyst = subitem['column_values'][0]['text']
    action.date = get_time(subitem['column_values'][1]['value'])

    return action


def dummy(column: dict, order: Order):
    pass

def first_name(column: dict, order: Order):
    order.first_name = column['text']

def last_name(column: dict, order: Order):
    order.last_name = column['text']

def dob(column: dict, order: Order):
    order.dob = get_date(column['value'])

def other_id(column: dict, order: Order):
    order.other_id = column['text']

def client(column: dict, order: Order):
    order.client = column['text']

def matrix(column: dict, order: Order):
    order.matrix = column['text']

def collection_time(column: dict, order: Order):
    order.collection_time = get_time(column['value'])

def collected_by(column: dict, order: Order):
    order.collected_by = column['text']

def medications(column: dict, order: Order):
    order.medications = column['text'].split('\n')

def other_info(column: dict, order: Order):
    order.other_info = column['text']

columns = {
    'First Name': first_name,
    'Last Name': last_name,
    'DOB': dob,
    'Other ID': other_id,
    'Client': client,
    'Matrix': matrix,
    'Collection Time': collection_time,
    'Collected By': collected_by,
    'Medications': medications,
    'Other Info': other_info
}

def get_order(item):
    order = Order()
    order.accession = item['name']

    for column in item['column_values']:
        columns.get(column['column']['title'], dummy)(column, order)

    order.actions = [get_action(i) for i in item['subitems']]

    return order