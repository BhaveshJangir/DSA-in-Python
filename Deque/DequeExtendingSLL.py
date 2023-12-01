from LinkedList.SinglyLinkedList import SinglyLinkedList

class Deque:
    def __init__(self):
        self.de = SinglyLinkedList()
        self.count = 0

    def isEmpty(self):
        return self.de.isEmpty()

    def insert_front(self,data):
        self.de.insert_at_first(data)
        self.count+=1

    def insert_rear(self,data):
        self.de.insert_at_last(data)
        self.count +=1

    def delete_front(self):
        val = self.de.start.data
        self.count -=1
        self.de.delete_first()
        return val

    def delete_rear(self):
        temp = self.de.start
        while temp.next is not None:
            temp = temp.next
        val = temp.data
        self.count -=1
        self.de.delete_last()
        return val

    def get_front(self):
        if not self.de.isEmpty():
            return self.de.start.data
        else:
            return

    def get_rear(self):
        if not self.de.isEmpty():
            temp = self.de.start
            while temp.next is not None:
                temp = temp.next
            val = temp.data
            return val
        else:
            return "Deque is under Flow"

    def size(self):
        return self.count

#driver Code
a = Deque()
a.insert_rear(5)
a.insert_front(4)
a.insert_front(3)
a.insert_rear(6)
a.insert_rear(7)
print("Delete Front value -> ",a.delete_front())
print("Delete Rear value -> ",a.delete_rear())
print("Front value -> ",a.get_front())
print("Rear value -> ",a.get_rear())
print("Deque is empty -> ",a.isEmpty())
print("Deque size -> ",a.size())
