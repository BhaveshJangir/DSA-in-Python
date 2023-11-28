from LinkedList.SinglyLinkedList import SinglyLinkedList
class Queue(SinglyLinkedList):
    def __init__(self):
        self.list = SinglyLinkedList()
        self.size = 0

    def is_Empty(self):
        self.list.isEmpty()

    def enqueue(self,data):
        self.list.insert_at_last(data)
        self.size +=1

    def dequeue(self):
        val = self.list.start.data
        self.list.delete_first()
        self.size -=1
        return val

    def get_front(self):
        return self.list.start.data

    def get_rear(self):
        temp = self.list.start
        while temp.next is not None:
            temp = temp.next
        return temp.data

    def length(self):
        return self.size


#driver Code
a = Queue()

a.enqueue(15)
a.enqueue(20)
a.enqueue(25)
print("Dequeue element ->",a.dequeue())
print("Dequeue element ->",a.dequeue())
print("length -> ",a.length())
print("Front element -> ",a.get_front())
print("Rear element -> ",a.get_rear())



