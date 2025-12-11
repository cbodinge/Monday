from sample_testing.orders.queries import all_finalized_orders
from sample_testing.reports.chain_of_custody import ChainOfCustody
from sample_testing.reports.requisition import Requisition


def finals():
    orders = all_finalized_orders()
    for order in orders:
        if order.accession > '25-10-25-12-58-52':
            print(order.accession)
            ChainOfCustody(order).pdf()
            Requisition(order).pdf()


finals()
