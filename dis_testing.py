import time
import dis

"""
Anjana Vakil - Exploring Python Bytecode
https://www.youtube.com/watch?v=GNPKBICTF2w&list=WL&index=15&
"""


def function_timer(func):
    def wrapper(*arg, **kwargs):
        start = time.time()
        ret = func(*arg, **kwargs)
        end = time.time()
        return (end - start), ret
    return wrapper


@function_timer
def run_loop():
    for i in range(10**8):
        i


if __name__ == "__main__":
    s = time.time()
    for item in range(10**8):
        item
    e = time.time()
    print("Loop outside function took:", e - s, "seconds")
    time_taken, value = run_loop()
    print("Loop inside function took:", time_taken, "seconds")
    print("dis inside function")
    print(dis.dis(run_loop))
    print("dis outside function")
    # dis can be run on strings as well
    print(dis.dis(open('inside_fn.py').read()))
