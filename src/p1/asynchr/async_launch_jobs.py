import asyncio
import threading
from asyncio import sleep, current_task
from datetime import datetime

def ts():
    return datetime.now().timestamp()

def task_name():
    return current_task().get_name()

def thread_name():
    return threading.current_thread().name

def log(msg):
    current_time = datetime.now().strftime("%H:%M:%S.%f")
    print(f'[{current_time[:-3]}]\t{msg}')


async def job(i):
    log(f'starting job {i}, {task_name()}')
    await sleep(0.5)  # non-blocking
    log(f'job {i} done')
    return i


async def main_foo():
    st = ts()
    log(f'start -- na wątku {thread_name()}')
    # await job(1)
    # asyncio.create_task(job(2))  # "fire and forget"
    # asyncio.create_task(job(3))  # "fire and forget"
    # for i in range(10**4):
    #     asyncio.create_task(job(i))
    # await sleep(0)

    # zadanie: trzeba zebrać wyniki job(1) job(2) i job(3), zsumować je -> sum, potem wypisać job(sum)
    t1 = asyncio.create_task(job(1))
    t2 = asyncio.create_task(job(2))
    t3 = asyncio.create_task(job(3))
    w = await asyncio.gather(t1,t2,t3)
    print(w)
    ancestor = sum(w)
    print(ancestor)
    result = await job(ancestor)
    log(f'wynik: {result}')

    log(f'main -- done after {ts() - st:.3f}s')
    await sleep(2)


asyncio.run(main_foo())
