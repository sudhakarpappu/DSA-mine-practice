class Node:
    def __init__(self,data):
        self.data=data 
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None
    def append(self,data):
        node=Node(data)
        if not self.head:
            self.head=node
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=node
    def printa(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next
    def connect(self,other):
        if not self.head:
            self.head=other.head
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=other.head




def convet_list(arr):
    ll=linkedlist()
    for i in arr:
        ll.append(i)
    return ll

ml=[1,2,3,4,5,6,66]
k=convet_list(ml)
k.printa()
ll1 = linkedlist()
for value in [1, 2, 3]:
    ll1.append(value)

# Second linked list
ll2 = linkedlist()
for value in [4, 5, 6]:
    ll2.append(value)

# Connect them
ll1.connect(ll2)

# Print the result
ll1.printa()

