import time
import requests
import threading
from simplejson import JSONDecodeError
from utils.helper import time_elapsed, type_check, func_info

@time_elapsed
@func_info
@type_check(str, str)
def url_parser(url: str, method: str):
    if method == "GET":
        resp = requests.get(url)
        try:
            print(f"Response: {resp.json()}")
        except JSONDecodeError:
            print(f"Response: {resp.text}")

def create_thread(fun, *args):
    th = threading.Thread(target=fun, args=(args))
    th.start()

@time_elapsed
@func_info
@type_check(int)
def sleep(sleep: int):
    time.sleep(sleep)
    print("I'm really tired...")

def main():
    urls = ['https://httpbin.org/headers', 'https://httpbin.org/get']
    [create_thread(url_parser,url,"GET") for url in urls]

    sleeps = [2,4]
    [create_thread(sleep,rest) for rest in sleeps]


if __name__ == "__main__":
    main()