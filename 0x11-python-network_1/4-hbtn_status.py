#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    page = response.text
    print("Body response:")
    print("    - type: ", type(page))
    print("    - content: ", page)
