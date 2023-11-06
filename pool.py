from multiprocessing import Pool

def doubler(num):
    return num * 2


if __name__ == '__main__':
    nums = [5, 10, 20]
    pool = Pool(processes=4)
    print(pool.map(doubler, nums))