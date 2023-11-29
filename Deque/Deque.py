class Deque:
    def __init__(self):
        self.list = []

    def isEmpty(self):
        return len(self.list) == 0

    def insert_front(self,data):
        self.list.insert(0,data)

    def insert_rear(self,data):
        self.list.append(data)

    def delete_front(self):
        if not self.isEmpty():
           return self.list.pop(0)
        else:
            return ("Deque is underflow")

    def delete_rear(self):
        if not self.isEmpty():
           return self.list.pop()
        else:
            return ("Deque is underflow")

    def get_front(self):
        if not self.isEmpty():
            return self.list[0]
        else:
            return ("Deque is underflow")

    def get_rear(self):
        if len(self.list) != 0:
            return self.list[-1]
        else:
            return ("Deque is underflow")

    def length(self):
        return len(self.list)


#driver Code
a = Deque()
a.insert_rear(5)
a.insert_front(4)
a.insert_front(3)
a.insert_rear(6)
print("Delete Front value -> ",a.delete_front())
print("Delete Rear value -> ",a.delete_rear())
print("Front value -> ",a.get_front())
print("Rear value -> ",a.get_rear())
print("Deque is empty -> ",a.isEmpty())
print("Deque size -> ",a.length())