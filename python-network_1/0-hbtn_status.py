#!/usr/bin/python3
"""Fetch and display the status from the ALU intranet."""
import urllib.request


def main():
    """Send a GET request to the ALU intranet status endpoint 
and print details """
    url = 'https://intranet.hbtn.io/status'
    headers = {
        'User-Agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/99.0.4844.84 Safari/537.36'
        )
    }

    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf8 content:", content.decode("utf-8"))


if __name__ == "__main__":
    main()
