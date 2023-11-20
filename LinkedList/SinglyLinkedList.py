class node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.start = None

    def isEmpty(self):
        return self.start is None

    def insert_at_first(self, data):
        avail = node(data, self.start)
        self.start = avail

    def insert_at_last(self, data):
        avail = node(data)
        temp = self.start
        while temp.next is not None:
            temp = temp.next
        temp.next = avail

    def search_node(self, data):
        temp = self.start
        while temp is not None:
            if temp.data == data:
                return temp
            temp = temp.next

    def inser_after(self, oldNode, data):
        avail = node(data, oldNode.next)
        oldNode.next = avail

    def delete_first(self):
        self.start = self.start.next

    def delete_last(self):
        temp = self.start
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

    def delete_item(self, dNode):
        temp = self.start
        if self.start is dNode:
            self.start = dNode.next
            return

        while temp is not None:
            if temp.next == dNode:
                break
            temp = temp.next
        temp.next = dNode.next

    def travesing(self):
        temp = self.start
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def __iter__(self):
        return SllIterator(self.start)


class SllIterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data



# driver code
a = SinglyLinkedList()
print("Is list is empty -> ", a.isEmpty())
a.insert_at_first(5)
a.insert_at_first(6)
a.insert_at_last(8)
a.insert_at_last(10)
a.inser_after(a.search_node(10), 7)
a.delete_item(a.search_node(6))
print(a.search_node(10).data)
a.travesing()

print("Is list is empty -> ", a.isEmpty())
print()
for x in a:
    print(x, end=' ')
