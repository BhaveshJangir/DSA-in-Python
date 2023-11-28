class node:
    def __init__(self,data = None, next = None):
        self.data =data
        self.next = next

class Queue:
    def __init__(self):
        self.start = None
        self.size = 0

    def enqueue(self,data):
        avail = node(data)
        if self.start is not None:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = avail
        else:
            self.start = avail
        self.size +=1

    def dequeue(self):
        if self.start is not None:
            val = self.start.data
            self.start = self.start.next
            self.size -=1
            return val
        else:
            return "Queue is underflow"

    def get_front(self):
        if self.start is not None:
            return self.start.data
        else:
            return "Queue is underflow"

    def get_rear(self):
        if self.start is not None:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            return temp.data
        else:
            return "Queue is underflow"


    def length(self):
        return self.size

#driver code
a = Queue()
a.enqueue(5)
a.enqueue(6)
a.enqueue(7)
print(a.dequeue())
print(a.dequeue())
print("Front element -> ",a.get_front())
print("Rear elemnent ->",a.get_rear())
print(a.length())