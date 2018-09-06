import time


def timeit(func):
    def call_with_print_time(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return call_with_print_time


def some(func):
    return lambda *args, **kwargs: (print("begin"), func(*args, **kwargs), print("end"))


if __name__ == '__main__':

    @timeit
    def cal():
        result = 0
        for i in range(1, 10 + 1):
            time.sleep(0.2)
            result += i
        print(result)


    cal()
