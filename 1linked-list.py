# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Function to insert at the end
    def append(self, data):
        new_node = Node(data)
 
        if not self.head:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Function to print the linked list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Convert list to linked list
def convert_list_to_linked_list(arr):
    linked_list = LinkedList()
    for item in arr:
        linked_list.append(item)
    return linked_list

# Example usage
my_list = [10, 20, 30, 40]
ll = convert_list_to_linked_list(my_list)
ll.print_list()
