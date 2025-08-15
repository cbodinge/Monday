from sample_testing.orders.queries import all_finalized_orders
from sample_testing.reports.chain_of_custody import ChainOfCustody
from sample_testing.reports.requisition import Requisition

orders = all_finalized_orders()
for order in orders:
    ChainOfCustody(order).pdf()
    Requisition(order).pdf()
