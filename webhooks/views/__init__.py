import logging
from django.views.decorators.csrf import csrf_exempt

def _get_logger() -> logging.Logger:
    """
    Instantiates and returns a logger instance for the views module.
    """
    log = logging.getLogger('webhooks_logger')
    log.setLevel(logging.DEBUG)

    # Add a file handler
    _file_handler = logging.FileHandler('custom.log')
    _formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    _file_handler.setFormatter(_formatter)
    log.addHandler(_file_handler)

    return log

logger = _get_logger()

# board_ids
pending_orders = 8479058626
lab_tasks = 9923937006
parc_projects = 9593812262
consulting_projects = 6822391121
