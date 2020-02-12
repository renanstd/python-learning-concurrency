#!python3

import asyncio
import time

async def my_task():
    time.sleep(1)
    print('Processing task')

async def other_task(number):
    time.sleep(1)
    return number * 2

async def my_task_generator():
    for i in range(5):
        asyncio.ensure_future(my_task())
    pending = asyncio.Task.all_tasks()
    print(pending)

async def launch_tasks(coroutines):
    for futures in asyncio.as_completed(coroutines):
        print(await futures)

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(my_task_generator())
    coroutines = [other_task(1), other_task(2), other_task(3), other_task(4)]
    loop.run_until_complete(launch_tasks(coroutines))
    print('Completed all tasks')
    loop.close()


if __name__ == "__main__":
    main()
