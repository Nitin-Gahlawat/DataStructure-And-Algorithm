class Deque:
    # Time Complexity O(1)
    def __init__(self, Numberele) -> None:
        self.queue_size = Numberele
        self.rear = self.front = -1
        self.queue = [0] * self.queue_size

    # Time Complexity O(1)
    def isEmpty(self) -> bool:
        if self.rear == self.front:
            return True
        return False

    # Time Complexity O(n)
    def __str__(self) -> str:
        if self.isEmpty():
            return "[]"

        res_queue = "["
        # Starting from the next term of the first and up to rear
        for i in range(self.front + 1, self.rear + 1):
            res_queue += f"{str(self.queue[i])},"
        return res_queue[0 : len(res_queue) - 1] + "]"

    # Time Complexity O(1)
    def queue_size(self) -> int:
        return self.queue_size

    # Time Complexity O(1)
    def font_loc(self) -> int:
        return self.front

    # Time Complexity O(1)
    def rear_loc(self) -> int:
        return self.rear

    # Time Complexity O(1)
    # return number of elements in the array
    def __len__(self) -> int:
        return self.rear - self.front

    # Time Complexity O(1)
    def get_Front(self) -> int:
        return self.queue[self.front + 1]

    # Time Complexity O(1)
    def get_rare(self) -> int:
        return self.queue[self.rear]

    # Time Complexity O(1)
    def enqueue_right(self, ele: int) -> None:
        if self.queue_size == self.rear:
            raise Exception("The queue is full from right")
        self.rear = self.rear + 1
        self.queue[self.rear] = ele

    # Time Complexity O(1)
    def enqueue_left(self, ele: int) -> None:
        if self.front == -1:
            raise Exception("The queue is full from left")
        self.queue[self.front] = ele
        self.front = self.front - 1

    # Time Complexity O(1)
    def dequeue_left(self) -> int:
        if self.front == self.rear:
            raise Exception("queue is Empty")
        x = self.queue[self.front]
        self.queue[self.front] = 0
        self.front = self.front + 1
        return x

    # Time Complexity O(1)
    def dequeue_right(self) -> int:
        if self.front == self.rear:
            raise Exception("queue is Empty")
        x = self.queue[self.rear]
        self.queue[self.rear] = 0
        self.rear = self.rear - 1
        return x


if __name__ == "__main__":
    x = Deque(4)
    x.enqueue_right(30)
    x.enqueue_right(500)
    x.enqueue_right(900)
    x.enqueue_right(800)
    x.dequeue_left()
    x.dequeue_left()
    x.enqueue_left(10)
    x.enqueue_left(20)
    x.dequeue_right()
    x.dequeue_right()

    print(x)
