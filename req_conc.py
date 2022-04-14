import requests
import threading
from simplejson import JSONDecodeError
from utils.helper import time_elapsed, type_check, func_info

@time_elapsed
@func_info
def get_url(url: str):
    resp = requests.get(url)
    try:
        print(f"\nResponse: {resp.json()}")
    except JSONDecodeError:
        print(f"\nResponse: {resp.text}")

@type_check((str,list))
def thread_exec(url):
    th = threading.Thread(target=get_url, args=([url]))
    th.start()

def main():
    # Run each request on a thread
    urls = ['https://httpbin.org/headers', 'https://httpbin.org/get']
    [thread_exec(url) for url in urls]

    # Run each request on same thread
    # for url in urls:
    #     url_parser(url)

if __name__ == "__main__":
    main()