class Stack(list):
    def isEmpty(self):
        return len(self) == 0

    def push(self,data):
        self.append(data)

    def pop(self):
        if not self.isEmpty():
            return super().pop()
        else:
            raise IndexError("List is empty")

    def peek(self):
        if not self.isEmpty():
            return self[-1]
        else:
            raise IndexError("List is empty")

    def size(self):
        return len(self)

    def insert(self,index,data):
        raise AttributeError("insert in not working in stack")

#driver code
a = Stack()
print(a.isEmpty())
a.push(5)
a.push(8)
a.push(10)
print(a.size())
print("remove element ->",a.pop())
print(a.peek())
print(a.isEmpty())
