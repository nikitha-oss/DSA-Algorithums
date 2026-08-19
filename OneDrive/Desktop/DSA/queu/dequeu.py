class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)
        print(value, "inserted")

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue Underflow")
        else:
            print(self.queue.pop(0), "deleted")

    def display(self):
        print("Queue:", self.queue)


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

q.dequeue()

q.display()
