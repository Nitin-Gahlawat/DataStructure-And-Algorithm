from Queue.Queue import Queue
from Queue.Linked_queue import Linked_queue
from Queue.Circular_queue import Circular_queue
from Queue.Deque import Deque

from Queue.Queue_two_stk import queue_using_stack
from Queue.Priority_queue import Priority_queue


def introduction():
    print("\nQueue")
    print("-" * 120)
    print("This Module contains all the algorithm related to the Queue datastructure")
    print("example")
    p = Queue(5)
    p.enqueue(1)
    p.enqueue(2)
    p.enqueue(3)
    p.enqueue(4)
    p.enqueue(5)
    print(f"Queue is {p}")
    p.dequeue()
    print(f"Queue after dequeuing one element from the queue {p}")
