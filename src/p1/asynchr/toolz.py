import random
from asyncio import sleep


async def is_really_prime(x: int) -> bool:
    if x <= 1: return False
    for div in range(2, int(x ** 0.5) + 1):
        if x % div == 0: return False
    return True



class Monitor:
    counter = 0

    async def run(self):
        while True:
            await sleep(0.0001)
            # zbierać czasy między kolejnymi wykonaniami tej pętli


    async def report(self):
        # narysować histogram czasów wykonania pętli
        pass


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    x = [random.gauss(0,1) for _ in range(10000)]
    plt.hist(x, bins=50)
    plt.show()
