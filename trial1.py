class node:
    def __init__(self,data):
        self.data=data 
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None 
    
    def appenda(self,a):
        nodde=node(a)
        if self.head is None:
            self.head=nodde 
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=nodde 
    def printt(self):
        if self.head is None:
            print(None) 
        curr=self.head 
        while curr:
            print(curr.data)
            curr=curr.next 

def arr_LL(arr):
    ll=Linkedlist()
    for i in arr:
        ll.appenda(i)
    return ll 


arr=[1,2,3,4,5]
ll=arr_LL(arr)
ll.printt()