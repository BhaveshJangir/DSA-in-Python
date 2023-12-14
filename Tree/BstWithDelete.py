class node:
    def __init__(self,data=None,left=None,right=None):
        self.data= data
        self.left = left
        self.right=right

class Bst:
    def __init__(self):
        self.root = None

    def insert(self,data):
        self.root = self.rInsert(self.root,data)

    def rInsert(self,root,data):
        if root is None:
         return node(data)

        if data<root.data:
            root.left = self.rInsert(root.left,data)
        elif data>root.data:
            root.right = self.rInsert(root.right,data)

        return root

    def search(self,data):
        return self.rSearch(self.root,data)

    def rSearch(self,root,data):
        if root is None or root.data == data:
            return root

        if data<root.data:
          return  self.rSearch(root.left,data)
        elif data>root.data:
           return self.rSearch(root.right,data)


    def inOrder(self):
        self.rInOrder(self.root)

    def rInOrder(self,root):
        if root:
            self.rInOrder(root.left)
            print(root.data,end=" ")
            self.rInOrder(root.right)

    def minItem(self):
        return self.rMinItem(self.root)

    def rMinItem(self,root):
        if root.left is None:
            return root
        return self.rMinItem(root.left)

    def maxItem(self):
        return self.rMaxItem(self.root)

    def rMaxItem(self,root):
        if root.right is None:
            return root
        return self.rMaxItem(root.right)

    def delete(self,data):
        self.root = self.rDelete(self.root,data)

    def rDelete(self,root,data):
        if root is None:
            return None

        if data < root.data:
            root.left = self.rDelete(root.left,data)
        elif data > root.data:
            root.right = self.rDelete(root.right,data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.data=self.rMinItem(root.right).data
            root.right = self.rDelete(root.right,root.data)
        return root






t = Bst()
t.insert(10)
t.insert(6)
t.insert(15)
t.insert(4)
t.insert(7)
t.inOrder()
print(t.search(6).data)
print(t.minItem().data)
print(t.maxItem().data)
t.delete(10)
t.inOrder()



