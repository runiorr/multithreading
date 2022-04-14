import requests
import threading
from utils.info import time_thread

@time_thread
def url_parser(url: str):
    resp = requests.get(url)
    try:
        print(resp.json())
    except Exception as err:
        print(resp.text)

def thread_exec(urls: list):
    th_count = 0
    for url in urls:
        th = threading.Thread(target=url_parser, args=([url]))
        th.start()
        th_count+=1
        
    print(f'{th_count} Threads created and closed\n')

# @time_thread
def main():
    # Run each request on a thread

    urls = ['https://httpbin.org/headers', 'https://httpbin.org/get']
    thread_exec(urls)


    # Run each request on same thread

    # for url in urls:
    #     url_parser(url)

if __name__ == "__main__":
    main()