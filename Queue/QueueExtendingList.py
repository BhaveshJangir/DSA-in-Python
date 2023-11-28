class Queue(list):
     def enqueue(self,data):
         self.append(data)

     def dequeue(self):
        return self.pop(0)

     def get_rear(self):
         return self[-1]

     def get_front(self):
         return self[0]

     def length(self):
         return len(self)


#driver Code
a = Queue()

a.enqueue(15)
a.enqueue(20)
a.enqueue(25)
a.enqueue(30)

print("Dequeue element ->",a.dequeue())
print("Dequeue element ->",a.dequeue())
print("length -> ",a.length())
print("Front element -> ",a.get_front())
print("Rear element -> ",a.get_rear())
