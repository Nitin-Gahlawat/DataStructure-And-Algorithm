import math


class Circular_queue:
    def __init__(self, Numberele):
        # Because there is One space left between the front and rear
        self.queue_size = Numberele + 1
        self.rear = self.front = 0
        self.queue = [0] * self.queue_size

    def isfull(self) -> bool:
        if (self.front) % self.queue_size == (self.rear + 1) % self.queue_size:
            return True
        else:
            return False

    def isEmpty(self) -> bool:
        if (self.front) % self.queue_size == (self.rear) % self.queue_size:
            return True
        else:
            return False

    def enqueue(self, num) -> None:
        # print("enque", num, self.front, self.rear)
        if self.isfull():
            raise Exception("The queue is full")
        self.rear = (self.rear + 1) % self.queue_size
        self.queue[self.rear] = num

    def dequeue(self) -> int:
        # print("dequeue", self.front, self.rear)
        if self.isEmpty():
            raise Exception("The queue is Empty")
        self.front = (self.front + 1) % self.queue_size
        x = self.queue[self.front]
        return x

    def __str__(self) -> str:
        if self.isEmpty():
            return "[]"
        res_queue = "["
        print(self.front, self.rear)
        i = self.front + 1
        while True:
            res_queue += f"{self.queue[i]},"
            i = (i + 1) % self.queue_size

            if i == (self.rear + 1) % self.queue_size:
                break
        return res_queue[0 : len(res_queue) - 1] + "]"

    def __len__(self) -> int:
        if self.rear == self.front:
            return 0
        elif self.rear < self.front:
            return (0 + self.rear) + (self.queue_size - self.front)
        elif self.rear > self.front:
            return self.rear - self.front


if __name__ == "__main__":
    queue = Circular_queue(4)
    queue.enqueue(0)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print(queue)
    queue.dequeue()
    print(queue)
    queue.dequeue()
    print(queue)
    queue.enqueue(45)
    print(queue)
    print(len(queue))
