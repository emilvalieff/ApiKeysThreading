import threading
import requests
import time
import asyncio
import aiohttp

# Request

def get_data_sync(urls):
    st = time.time()
    json_array = []
    for url in urls:
        json_array.append(requests.get(url).json)
    et = time.time()
    elapsed_time = et - st
    print("Execution time" ,elapsed_time, "seconds")
    return json_array

# Thread
class  ThreadingDownloader(threading.Thread):
    json_array = []

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        response = requests.get(self.url)
        self.json_array.append(response.json())
        print(self.json_array)
        return self.json_array

def get_data_threading(urls):
    st = time.time()
    threads = []
    for url in urls:
        t = ThreadingDownloader(url)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
        #print(t)

    et = time.time()
    elapsed_time = et - st
    print("Execution time:", elapsed_time, "seocnds")


async def get_data_async_but_as_wrapper(urls):
    st = time.time()
    json_array = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            async with session.get(url) as response:
                json_array.append(await response.json())

    et = time.time()
    elapsed_time = et - st
    print("Execution time:", elapsed_time, "seconds")
    return json_array


async def get_data(session, url, json_array):
    async with session.get(url) as resp:
        json_array.append(await resp.json())


async def get_data_async_concurrently(urls):
    st = time.time()
    json_array = []

    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(asyncio.ensure_future(get_data(session, url, json_array)))
        await asyncio.gather(*tasks)



    et = time.time()
    elapsed_time = et - st
    print("Execution time:", elapsed_time, "seconds")

urls = ["http://postman-echo.com/delay/3"] * 10
#get_data_sync(urls) # 34 seconds
#get_data_threading(urls) # 4 seconds
# asyncio.run (get_data_async_but_as_wrapper(urls)) # 40 seconds :D
# asyncio.run(get_data_async_concurrently(urls)) # 4.7 seconds