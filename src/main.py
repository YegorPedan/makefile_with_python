import requests
from typing import Optional


def get_html_content(url: str) -> Optional[str]:
    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.text
        else:
            print(
                f"Failed to retrieve HTML content. Status Code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {e}")
        return None


if __name__ == "__main__":
    response = get_html_content("http://google.com")
    if isinstance(response, str):
        print(response[:20])
