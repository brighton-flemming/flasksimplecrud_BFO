from collections import deque

class Queue():
    def __init__(self):
        self.items = deque()
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.popleft()
    def peek(self):
        return self.items[0]
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def __str__(self):
        return str(self.items) 
    
if __name__ == "__main__":
    q = Queue()

    print(q)
    print(q.is_empty())

    q.enqueue("Hannah")
    q.enqueue("Roxy")
    q.enqueue("Miley")
    q.enqueue("Tracey")

    q.dequeue()

    q.enqueue("Marey")
    q.enqueue("Golderline")
    q.enqueue("Patricia")
    q.enqueue("Laqueefa")

    print(q)
    print("Size of the queue: ", q.size())

    print("Furthemost Name/Sexiest Name: ", q.peek())
    print(q)



    