from ..core.username_validator import validate
from ..core.response_fetcher import fetch
from ..core.response_formatter import format
from ..core.events_presenter import present


def request_handler(username: str) -> int:
    try:
        validate(username)
        response = fetch(username)
        events = format(response)
        present(events)
    
    except Exception as e:
        print(e)
        return 1
    
    return 0
