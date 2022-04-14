import requests
import threading
from simplejson import JSONDecodeError
from utils.helper import time_elapsed, type_check, func_info

@time_elapsed
@func_info
@type_check(str, str)
def url_parser(url: str, method: str):
    resp = requests.get(url)
    if method == "GET":
        try:
            print(f"\nResponse: {resp.json()}")
        except JSONDecodeError:
            print(f"\nResponse: {resp.text}")

@type_check(str)
def thread_exec(url: str):
    th = threading.Thread(target=url_parser, args=([url, "GET"]))
    th.start()

def main():
    urls = ['https://httpbin.org/headers', 'https://httpbin.org/get']
    [thread_exec(url) for url in urls]

if __name__ == "__main__":
    main()