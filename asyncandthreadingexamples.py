import threading
import requests
import time


def get_data_sync(urls):
    json_array = []
    for url in urls:
        json_array.append(request.get(url).json)
    return json_array