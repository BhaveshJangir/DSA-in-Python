class node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next





class CircLinkedList:

    def __init__(self):
        self.last = None

    def isEmpty(self):
       return self.last is not None

    def insert_at_first(self,data):
        avail = node(data)

        if self.last is not None:
            avail.next = self.last.next
            self.last.next = avail
        else:
            avail.next = avail
            self.last = avail

    def insert_at_end(self,data):
        if self.last is None:
            avail = node(data)
            avail.next = avail
            self.last = avail
        else:
            avail = node(data)
            avail.next = self.last.next
            self.last.next = avail
            self.last = avail


    def search(self,data):
        temp = self.last.next

        while True:
            if temp.data == data:
                return temp
            temp = temp.next
            if temp == self.last.next:
                break

    def insert_after(self,oldNode,data):
        avail = node(data,oldNode.next)
        oldNode.next = avail


    def traversing(self):
        if self.last is not None:
            temp = self.last.next
            while True:
                print(temp.data,end=" ")
                temp = temp.next
                if temp is self.last.next:
                    break
        else:
            print("list is empty")

    def delete_first(self):
        if self.last is not None:
            if self.last == self.last.next:
                self.last = None
            else:
                self.last.next = self.last.next.next
        else:
            print("list is empty")

    def delete_at_last(self):

        temp = self.last.next
        while True:
            temp = temp.next
            if temp.next == self.last:
                break
        temp.next = self.last.next
        self.last = temp


    def delete_item(self,dNode):
        temp = self.last.next
        while True:
            temp = temp.next
            if temp.next == dNode:
                break
        if dNode == self.last:
            self.last = temp
        temp.next = dNode.next








#Driver Code
list = CircLinkedList()
list.insert_at_first(5)
list.insert_at_first(4)
list.insert_at_first(3)
list.insert_at_first(2)
list.insert_at_end(6)
list.insert_at_end(7)
list.insert_at_end(8)
list.insert_after(list.search(2),51)
# list.delete_at_last()
# list.delete_at_last()
# list.delete_at_last()
list.delete_item(list.search(8))
list.delete_item(list.search(7))
list.delete_item(list.search(3))


list.traversing()
