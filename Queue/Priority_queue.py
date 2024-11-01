from enum import Enum
from collections import deque
from typing import Iterator


class Priority(Enum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3


# dict[str, Enum[Priority]]
def Priority_queue(x) -> tuple:
    Q1, Q2, Q3 = deque(), deque(), deque()
    for i in x:
        if x[i] == Priority.HIGH:
            Q1.append(i)
        elif x[i] == Priority.LOW:
            Q2.append(i)
        else:
            Q3.append(i)

    return Q1, Q2, Q3


if __name__ == "__main__":

    x = {
        "a": Priority.HIGH,
        "b": Priority.HIGH,
        "c": Priority.MEDIUM,
        "d": Priority.LOW,
        "e": Priority.MEDIUM,
        "f": Priority.HIGH,
        "e": Priority.MEDIUM,
        "f": Priority.LOW,
        "g": Priority.MEDIUM,
        "h": Priority.HIGH,
    }
    q1, q2, q3 = Priority_queue(x)
    print("HIGHEST proterities", q1)
    print("MEDIUM proterities", q2)
    print("LOWEST proterities", q3)
