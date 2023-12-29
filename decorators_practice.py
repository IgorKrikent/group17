from typing import Callable, Any

import time


def logs_time_name(func: Callable) -> Callable:
    """decorator for writing functions' runtimes into text files"""
    def wrapper(*args, **kwargs) -> Any:

        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()

        elapsed_time = end_time - start_time

        name_log = func.__name__

        with open(f'{name_log}.txt', mode='a', encoding='utf-8') as file:

            file.write(f'The function worked for {elapsed_time} seconds\n')

        return result

    return wrapper


@logs_time_name
def foo() -> None:
    """Function-example"""

    time.sleep(2)


foo()

