class node:
    def __init__(self,data = None,next =None):
        self.data = data
        self.next = next

class Deque:
    def __init__(self):
        self.start = None
        self.size = 0

    def isEmpty(self):
        return self.start is None

    def insert_front(self,data):
        avail = node(data,self.start)
        self.start = avail
        self.size +=1

    def insert_rear(self,data):
        if self.start is None:
            self.insert_front(data)
        else:
            avail = node(data,None)
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = avail
            self.size +=1

    def delete_front(self):
        if self.start is not None:
            val = self.start.data
            self.start = self.start.next
            self.size -= 1
            return val
        else:
            return "deque is underflow"

    def delete_rear(self):
        if self.start.next is None:
            val = self.start.data
            self.start = None
            return val

        if self.start is not None:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            val = temp.next.data
            temp.next = None
            self.size -= 1
            return val
        else:
            return "deque is underflow"


    def get_front(self):
        if self.start is not None:
            return self.start.data
        else:
            return "deque is underflow"

    def get_rear(self):
        if self.start is not None:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            return temp.data
        else:
            return "deque is underflow"

    def length(self):
        return self.size




#driver Code
a = Deque()
a.insert_rear(5)
a.insert_front(4)
a.insert_front(3)
a.insert_rear(6)
a.insert_rear(8)
print("Delete Front value -> ",a.delete_front())
print("Delete Rear value -> ",a.delete_rear())
print("Front value -> ",a.get_front())
print("Rear value -> ",a.get_rear())
print("Deque is empty -> ",a.isEmpty())
print("Deque size -> ",a.length())
