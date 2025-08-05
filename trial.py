class Node:
    def __init__(self,data):
        self.data=data
        self.next=None 
class LinkedList:
    def __init__(self):
        self.head=None 
    
    def appenda(self,data):
        newnode=Node(data)
        if not self.head:
            self.head=newnode
            return
        last=self.head 
        while last.next:
            last=last.next
        last.next=newnode
    def printl(self):
        if self.head==None:
            return None 
        curr=self.head
        while curr:
            print(curr.data,end="->")
            curr=curr.next 
    
    def rotate_right(self, k):
        if not self.head or not self.head.next or k == 0:
            return
        
        # Step 1: Count length and get tail
        length = 1
        tail = self.head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Normalize k
        k = k % length
        if k == 0:
            return
        
        # Step 3: Find new tail (length - k) and new head
        new_tail = self.head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        
        # Step 4: Break and rotate
        new_tail.next = None
        tail.next = self.head
        self.head = new_head

def list_ll(arr):
    ll=LinkedList()
    for i in arr:
        ll.appenda(i)
    return ll 

my_list = [10, 20, 30, 40,3,5,99,6665]
ll = list_ll(my_list)
#ll.printl()


def sep(ll):
    even=LinkedList()
    odd=LinkedList()

    curr=ll.head
    while curr:
        if curr.data%2==0:
            even.appenda(curr.data)
        else:
            odd.appenda(curr.data)
        curr=curr.next

    even.printl()
    print("")
    odd.printl()
def ll_list(ll):
    a=[]
    curr=ll.head 
    while curr:
        a.append(curr.data)
        curr=curr.next
    print(a)
ll = LinkedList()
for val in [10, 20, 30, 40, 50, 60]:
    ll.appenda(val)

print("Original List:")
ll.printl()

ll.rotate_right(3)
print("After rotating right by 2:")
ll.printl()
