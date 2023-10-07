"""This is the main module of my python application that just send http request to server"""
from typing import Optional
import requests


def get_html_content(url: str) -> Optional[str]:
    """That function just accepts url[str] and try to make a request to it"""
    try:
        response = requests.get(url, timeout=2)

        if response.status_code == 200:
            return response.text
        print(
            f"Failed to retrieve HTML content. Status Code: {response.status_code}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {e}")
        return None


if __name__ == "__main__":
    result = get_html_content("http://google.com")
    if isinstance(result, str):
        print(result[:20])
