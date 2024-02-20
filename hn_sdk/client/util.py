from urllib.parse import urlencode, urljoin

import requests
from requests import Response


def rest_call(rest_call: callable, *args, **kwargs) -> Response:
    """
    Make a general REST call and handle exceptions.
    """
    try:
        response = rest_call(*args, **kwargs)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        print(f"Error during REST call: {e}")
        raise e


@staticmethod
def build_url_with_params(base_url: str, query_params: dict[str, any]) -> str:
    """
    Build a URL with query parameters.
    """

    # Convert values to strings since urlencode expects string values
    query_params = {key: str(value) for key, value in query_params.items()}

    url_with_params = urljoin(base_url, "?" + urlencode(query_params))

    return url_with_params
