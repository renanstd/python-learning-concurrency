#!python3

import asyncio

async def my_coroutine():
    print("Simple coroutine example")


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(my_coroutine())
    loop.close()

if __name__ == "__main__":
    main()
