class node:
    def __init__(self,data = None,left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class Bst:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None


    def insert(self,data):
       self.root = self.rinsert(self.root,data)

    def rinsert(self,root,data):
        if root is None:
            return node(data)

        if data < root.data:
            root.left = self.rinsert(root.left,data)

        elif data > root.data:
            root.right = self.rinsert(root.right,data)

        return root


    def search(self,data):
        return self.rSearch(self.root,data)

    def rSearch(self,root,data):
        if root is None or root.data == data:
            return root

        if data < root.data:
            return  self.rSearch(root.left,data)
        elif data > root.data:
            return self.rSearch(root.right,data)



    # def search(self,data):
    #     return self.rsearch(self.root,data)
    # def rsearch(self,root,data):
    #     if root is None or root.data==data:
    #         return root
    #     if data <root.data:
    #         return self.rsearch(root.left,data)
    #     else:
    #         return self.rsearch(root.right,data)
    def inorder(self):
         self.rinorder(self.root)

    def rinorder(self,root):
        if root:
            self.rinorder(root.left)
            print(root.data,end=" ")
            self.rinorder(root.right)

    def pre_order(self):
        self.rPreOrder(self.root)

    def rPreOrder(self,root):
        if root:
            print(root.data,end=" ")
            self.rPreOrder(root.left)
            self.rPreOrder(root.right)

    def post_order(self):
        self.rPostOrder(self.root)

    def rPostOrder(self,root):
        if root:
            self.rPostOrder(root.left)
            self.rPostOrder(root.right)
            print(root.data,end=" ")


#driver code
a = Bst()
a.insert(50)
a.insert(70)
a.insert(40)
a.insert(30)
a.insert(60)
a.insert(100)
a.insert(5)

a.inorder()
print()
a.pre_order()
print()
a.post_order()
print()
print(a.search(5))
i = 30
if a.search(i) is not None:
    print(a.search(i).data)
else:
    print(None)



