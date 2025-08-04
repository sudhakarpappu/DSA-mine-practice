class Node:
    def __init__(self,data):
        self.data=data 
        self.next=None 

class LinkedList:
    def __init__(self):
        self.head=None 
    
    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return 
        lastnode=self.head
        while lastnode.next:
            lastnode=lastnode.next
        lastnode.next=new_node
    def print_list(self):
        if not self.head:
            return None
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
def list_linkedlist(arr):
    linkedlist=LinkedList()
    for i in arr:
        linkedlist.append(i)
    return linkedlist

my_list = [10, 20, 30, 40,60,70]
ll = list_linkedlist(my_list)

ll.print_list()

