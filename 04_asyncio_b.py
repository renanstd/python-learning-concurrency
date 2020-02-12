#!python3

import asyncio
import random

async def my_coroutine(id):
    process_time = random.randint(1, 5)
    await asyncio.sleep(process_time)
    print('Coroutine {}, has successfully completed after {} seconds'.format(id, process_time))


async def main():
    tasks = []
    for i in range(10):
        tasks.append(asyncio.ensure_future(my_coroutine(i)))

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
