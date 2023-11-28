class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self,data):
        self.items.append(data)


    def dequeue(self):
        if not self.isEmpty():
          return  self.items.pop(0)
        else:
            print("Queue is empty")

    def get_front(self):
        if not self.isEmpty():
            return self.items[0]
        else:
            print("Queue is empty")


    def get_rear(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            print("Queue is empty")


    def size(self):
        return len(self.items)

#driver code
a = Queue()
a.enqueue(5)
a.enqueue(7)
a.enqueue(8)
a.enqueue(15)
a.enqueue(17)
print(a.get_rear())
print(a.get_front())
print('remove element -> ',a.dequeue())
print('size',a.size())
print(a.items)
print(a.isEmpty())