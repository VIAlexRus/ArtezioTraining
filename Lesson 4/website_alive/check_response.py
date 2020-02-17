import make_request as req


def chekUrl(url):
    status = req.reqGet(url)
    if status.status_code == 200:
        return True
    else:
        return False
    pass


chekUrl('http://google.ru/')
