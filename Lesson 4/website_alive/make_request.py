import requests


def reqGet(url):
    # to receive the status from url
    status = requests.get(url)
    return status
