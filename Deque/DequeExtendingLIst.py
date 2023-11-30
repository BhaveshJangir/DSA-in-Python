class Deque(list):
    def isEmpty(self):
        return len(self) == 0

    def insert_front(self,data):
        self.insert(0,data)

    def insert_rear(self,data):
        self.append(data)

    def delete_front(self):
        if not self.isEmpty():
            return self.pop(0)
        else:
            return 'deque is underflow'

    def delete_rear(self):
        if not self.isEmpty():
            return self.pop()
        else:
            return 'deque is underflow'

    def get_front(self):
        if not self.isEmpty():
            return self[0]
        else:
            return 'deque is underflow'

    def get_rear(self):
        if not self.isEmpty():
            return self[-1]
        else:
            return 'deque is underflow'

    def size(self):
        return len(self)

#driver code
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
print("Deque size -> ",a.size())