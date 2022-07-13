class Queue:
    def __init__(Self, d):
        Self.queue = []
        Self.front = Self.rear = 0
        Self.capacity = d
    def queueEnqueue(Self, data):
        if (Self.capacity == Self.rear):
            print("\nQueue is full")
        else:
            Self.queue.append(data)
            Self.rear += 1
    def queueDequeue(Self):
        if (Self.front == Self.rear):
            print("Queue is empty")
        else:
            y = Self.queue.pop(0)
            Self.rear -= 1
    def queueDisplay(Self):
        if (Self.front == Self.rear):
            print("\nQueue is Empty")
        for i in Self.queue:
            print(i, "<--", end='')
    def queueFront(Self):
        if (Self.front == Self.rear):
            print("\nQueue is Empty")
        print("\nFront Element is:",
              Self.queue[Self.front])
if __name__ == '__main__':
    q = Queue(4)
    q.queueDisplay()
    q.queueEnqueue(10)
    q.queueEnqueue(30)
    q.queueEnqueue(20)
    q.queueEnqueue(80)
    q.queueDisplay()
    q.queueEnqueue(60)
    q.queueDisplay()
    q.queueDequeue()
    print("\n\nafter node deletion\n")
    q.queueDisplay()
    q.queueFront()


