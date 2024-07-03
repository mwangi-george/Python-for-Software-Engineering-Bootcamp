
import time
import asyncio


async def sleep_a_little(time_to_sleep):
    await asyncio.sleep(time_to_sleep)


async def go_do_something():
    time_to_sleep = 5
    await sleep_a_little(time_to_sleep)


# calling asynchronous function
asyncio.run(go_do_something())
