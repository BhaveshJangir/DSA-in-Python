class node:
    def __init__(self,prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

class DoublyLikendList:
    def __init__(self):
        self.start = None

    def isEmpty(self):
        return self.start is None

    def insert_at_start(self,data):
        avail = node(None,data,self.start)
        if self.start is not None:
            self.start.prev = avail
        self.start = avail

    def insert_at_last(self,data):
        avail = node(data= data)
        temp = self.start
        while temp.next is not None:
            temp = temp.next

        avail.prev = temp
        temp.next = avail

    def search_node(self,data):
        temp = self.start
        while temp is not None:
            if temp.data == data:
                return temp
            temp = temp.next

        return node()

    def insert_after(self,oldNode,data):
        avail = node(prev = oldNode,data=data)
        if oldNode.next is not None:
            avail.next = oldNode.next
            oldNode.next.prev = avail
        oldNode.next = avail

    def delete_first(self):
        self.start.next.prev = None
        self.start = self.start.next

    def delete_last(self):
        temp = self.start
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

    def delete_item(self,dNode):
        temp = self.start

        if self.start == dNode:
            self.start = dNode.next
            dNode.next.prev = None
            return

        while temp is not None:
            if temp.next == dNode:
                temp.next.next.prev = temp
                temp.next = temp.next.next
            temp = temp.next


    def traversing(self):
        temp = self.start
        while temp is not None:
            print(temp.data,end=" ")
            temp = temp.next

    def __iter__(self):
        return DllIterator(self.start)


class DllIterator:
    def __init__(self,start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data


#driver Code
a = DoublyLikendList()
print(a.isEmpty())
a.insert_at_start(2)
a.insert_at_start(1)
a.insert_at_start(0)
a.insert_at_last(3)
a.insert_at_last(4)
a.insert_after(a.search_node(4),51)
print(a.search_node(51).next)
a.traversing()
a.delete_first()
print()
print("delete first")
for x in a:
    print(x,end=" ")
print()
print("delete last node")
a.delete_item(a.search_node(1))
a.traversing()


