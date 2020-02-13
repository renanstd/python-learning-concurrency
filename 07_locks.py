#!python3

import asyncio
import time

async def my_worker(lock):
    print("Attempting to attain lock")
    with await lock:
        print("Currently locked")
        time.sleep(2)
    print("Unlocked frm critical session")

async def main():
    lock = asyncio.Lock()
    await asyncio.wait([my_worker(lock), my_worker(lock)])


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print("All workers complete")
    loop.close()
