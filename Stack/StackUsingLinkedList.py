class node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.start = None
        self.count = 0

    def item_count(self):
       return self.count

    def isEmpty(self):
        return self.start is None

    def push(self,data):
        avail = node(data)
        if self.start is None:
            self.start = avail
        else:
            avail.next = self.start
            self.start = avail
        self.count += 1

    def peek(self):
        if self.start is None:
            print("stack is empty")
            return
        return self.start.data

    def pop(self):
        if self.start is None:
            print("stack is empty")
            return
        val = self.start.data
        self.start = self.start.next
        self.count -=1
        return val


    def size(self):
        return  self.count


#driver code
a = Stack()

a.push(5)
a.push(10)
a.push(15)

print(a.peek())
print('remove data',a.pop())
print(a.item_count())
print(a.peek())
print(a.isEmpty())




