#!python3

import asyncio


async def my_worker(semaphore):
    await semaphore.acquire()
    print("successfully acquired the semaphore")
    await asyncio.sleep(3)
    print("Releasing the semaphore")
    semaphore.release()

async def main():
    my_semaphore = asyncio.Semaphore(value=2)
    await asyncio.wait([
        my_worker(my_semaphore), 
        my_worker(my_semaphore), 
        my_worker(my_semaphore), 
    ])
    print("Finished all workers")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print("Our loop has completed")
    loop.close()
