#!python3

import asyncio
import time
import random

async def news_producer(my_queue):
    while True:
        await asyncio.sleep(1)
        await my_queue.put(random.randint(1, 5))

async def news_consumer(my_queue):
    while True:
        print(f"Consumer: {my_queue} attemting to get from queue")
        item = await my_queue.get()
        if item is None:
            break
        print("Consumer: {} consumed article with id : {}".format(id, item))

async def main(loop):
    my_queue = asyncio.Queue(loop=loop, maxsize=10)
    await asyncio.wait([news_producer(my_queue), news_consumer(my_queue)])


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    print("All workers complete")
    loop.close()
