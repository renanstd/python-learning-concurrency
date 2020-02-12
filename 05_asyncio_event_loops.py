#!python3

import asyncio

async def my_coroutine():
    while True:
        await asyncio.sleep(1)
        print('My coroutine')

async def other_coroutine():
    while True:
        await asyncio.sleep(1)
        print('Second coroutine')


def main():
    loop = asyncio.get_event_loop()
    try:
        asyncio.ensure_future(my_coroutine())
        asyncio.ensure_future(other_coroutine())
        loop.run_forever()
    except KeyboardInterrupt as e:
        pass
    finally:
        print('Closing loop')
        loop.close()

if __name__ == "__main__":
    main()
