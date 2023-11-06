import os
from multiprocessing import Process

def doubler(num):
    result = num * 2
    proc = os.getpid()
    print(f'number {num} got doubled to {result} by process id {proc}')

if __name__ == '__main__': # very important to keep this line
    numbers = [5, 10, 15, 20, 25]
    procs = []

    for index, number in enumerate(numbers):
        proc = Process(target=doubler, args=(number,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()