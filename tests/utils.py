from collections.abc import Sequence

from requests import Response


def get_payload(payload: dict, exclude: Sequence[str] | None = None) -> dict:
    """Extracts the payload from the response."""
    if payload is None:
        return {}

    if exclude is None:
        return payload

    for key in exclude:
        payload.pop(key, None)

    return payload


def prepare_payload(response: Response, exclude: Sequence[str] | None = None) -> dict:
    """Get payload."""
    payl = response.json()
    payload = get_payload(payl, exclude)
    return payload
