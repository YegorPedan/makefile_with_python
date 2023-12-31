"""That file just test code in main.py file"""
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

import src.main


def test_get_html_content() -> None:
    """Test get_html_content function"""
    websites = ["https://google.com", "https://yandex.com/", ]

    for website in websites:
        assert src.main.get_html_content(website) is not None


def test_ping_site() -> None:
    """Test ping_site function"""
    assert src.main.ping_site("https://google.com") == 200
    assert src.main.ping_site("https://github.com/Valll-v/BoysJobsds") == 404


if __name__ == '__main__':
    test_get_html_content()
    test_ping_site()
