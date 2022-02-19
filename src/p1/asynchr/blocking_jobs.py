# ---------------------------------------
# - przychodzą requesty
# - request wymaga jakichś danych
# - dane wymagają dalszych "calli" do DB, albo do innych serwisów
# - czekanie na dane >>> obróbka danych
#
#

import threading
from datetime import datetime
from time import sleep


def ts():
    return datetime.now().timestamp()


def thread_name():
    return threading.current_thread().name

def job(i):
    print(f'starting job {i}')
    sleep(9.5)  # blocking
    print(f'job {i} done')

def web_job():
    import requests
    r = requests.get('https://sars2.wsi.edu.pl/api/data?from=2022-01-23&districts=2405,2466')  # blocking
    return r.json()


if __name__ == '__main__':
    st = ts()
    print(f'start -- na wątku {thread_name()}')
    job(1)
    job(2)
    web_job()
    job(3)
    print(f'main -- done after {ts() - st:.3f}s')
