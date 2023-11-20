class node:
    def __init__(self,prev=None,data=None,next=None):
        self.prev = prev
        self.data = data
        self.next = next

class CircDll:
    def __init__(self):
        self.start = None
        self.size = 0

    def isEmpty(self):
        return self.start is None

    def size(self):
        return self.size()

    def insert_at_start(self,data):
        avail = node(data=data)
        if self.start is not None:
            avail.prev = self.start.prev
            avail.next = self.start

            self.start.prev.next = avail
            self.start.prev = avail
        else:
            avail.prev = avail
            avail.next = avail
        self.start = avail

    def insert_at_last(self,data):
        if self.start is None:
            self.insert_at_start(data)
        else:
            avail = node(self.start.prev,data,self.start)
            self.start.prev.next = avail
            self.prev = avail

    def search_node(self,data):
        temp = self.start
        while True:
            if temp.data == data:
                return temp
            temp = temp.next
            if temp == self.start:
                return None
                break

    def insert_after(self,oldNode,data):
        avail = node(oldNode,data,oldNode.next)
        oldNode.next.prev= avail
        oldNode.next = avail


    def delete_first(self):
        temp = self.start
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        self.start = temp.next

    def delete_last(self):
        temp = self.start
        temp.prev.prev.next = self.start
        temp.prev = temp.prev.prev

    def delete_item(self,node):
        temp = node
        if node == self.start:
            self.start = temp.next

        temp.prev.next = temp.next
        temp.next.prev = temp.prev

    def  travers(self):
        temp = self.start
        while True:
            print(temp.data,end=" ")
            temp = temp.next
            if temp == self.start:
                print()
                break


#Driver Code
a = CircDll()
print(a.isEmpty())
a.insert_at_start(5)
a.insert_at_start(8)
a.insert_at_start(9)
a.insert_at_last(10)
a.insert_after(a.search_node(10),51)
print(a.search_node(1))
a.delete_item(a.search_node(9))



a.travers()
print(a.isEmpty())


