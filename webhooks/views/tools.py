from typing import Any

from . import logger
from json import loads, JSONDecodeError
from django.http import HttpRequest, HttpResponseBadRequest, JsonResponse, HttpResponse


def payload(request: HttpRequest) -> tuple[Any | None, HttpResponseBadRequest] | tuple[Any, JsonResponse]:
    """
    Returns the payload of a Monday webhook request where appropriate.
    Has internal logic to determine if this is a challenge request or not.
    Args:
        request: HTTP Request object.

    Returns:
        tuple with the decoded JSON (or raw if decoding failed) and the appropriate HttpResponse object.

    """
    _payload = None
    try:
        _payload = loads(request.body.decode('utf-8'))
        logger.info(f'Payload decoded: {_payload}')
    except JSONDecodeError:
        logger.info(f'Payload could not be decoded: {request.body}')
        return _payload, HttpResponseBadRequest("Invalid JSON")

    # Handle the handshake
    if "challenge" in _payload:
        logger.info('challenge detected, handshake sent.')
        return _payload, JsonResponse({"challenge": _payload["challenge"]})

    return _payload, JsonResponse(_payload, status=200)
