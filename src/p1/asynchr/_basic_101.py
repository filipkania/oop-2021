import asyncio
from asyncio import sleep, current_task


def task_name():
    return current_task().get_name()


# from random import


async def goo():
    print(f'subtask -- task: {task_name()}')
    await sleep(0.3)

async def foo():
    print(f'start -- task: {task_name()}')
    tt = asyncio.create_task(goo())
    print(f'after subtask creation via fire-and-forget, tt={type(tt)}')
    await sleep(1.3)
    await tt
    print('doing')
    await goo()
    await sleep(1.3)
    print('done')

asyncio.run(foo())