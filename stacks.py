class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def __str__(self):
        return str(self.items)
    
if __name__ == "__main__":
    s = Stack()
    print(s)
    s.push("Michael")
    print(s)

    s.push("Fred")
    s.push("Paul")
    s.push("Tyrone")
    s.push("Oswald")
    s.push("Walter")
    s.push("Francis")
    s.push("Ricky")
    print(s)

    print(s.pop())
    print(s)

    print(s.peek())