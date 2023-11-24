class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self,data):
        self.stack.append(data)

    def peek(self):

        if self.isEmpty():
            print("Stack is empty")
            return
        print(self.stack[-1])

    def pop(self):
        if not self.isEmpty():
          return self.stack.pop()
        else:
            print("Stack is empty")


a = Stack()
a.push(1)
a.push(2)
a.push(3)
a.peek()
print('pop element',a.pop())
a.peek()
print(a.isEmpty())