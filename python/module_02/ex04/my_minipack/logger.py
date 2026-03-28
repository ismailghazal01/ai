import time
import os
from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        user = os.getenv("USER") or os.getenv("USERNAME")
        name = func.__name__.replace("_", " ").title()
        exec_time = end - start

        if exec_time < 1:
            exec_time = str(round(exec_time * 1000, 3)) + " ms"
        else:
            exec_time = str(round(exec_time, 3)) + " s"

        with open("machine.log", "a") as f:
            f.write(f"({user})Running: {name:<20} [ exec-time = {exec_time} ]\n")

        return result
    return wrapper