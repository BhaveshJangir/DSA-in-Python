from LinkedList.SinglyLinkedList import SinglyLinkedList
class Stack:
    def __init__(self):
        self.list = SinglyLinkedList()
        self.count = 0

    def is_Empty(self):
       return  self.list.isEmpty()

    def push(self,data):
        self.list.insert_at_first(data)
        self.count +=1

    def pop(self):
        self.count -=1
        self.list.delete_first()

    def peek(self):
        return self.list.start.data

    def size(self):
        return self.count

#driver Code
b = Stack()
b.push(5)
b.push(10)

print("peek element",b.peek())
print("size ",b.size())
print("delete ",b.pop())
print("peek element",b.peek())
print("size ",b.size())
print(b.is_Empty())

