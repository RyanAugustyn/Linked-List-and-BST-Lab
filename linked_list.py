class Node:
    def __init__(self, data) -> None:
        self.data = data    
        self.pointer = None




class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def append_node(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.pointer = node
            self.tail = node
            

    def find_node(self, target):
        current = self.head
        if current.data == target:
            return True
        else:
            while current.pointer is not None:
                current = current.pointer
                if current.data == target:
                    return True
            return False




#O(n) 
"""    def append_node(self, data):
        node = Node(data)
        #initial check for empty list
        if self.head is None:
            self.head = node
            return       
        
        #step through current list until no further nodes found
        temp = self.head
        while temp.pointer is not None:
            temp = temp.pointer 

        #append into the final node
        temp.pointer = node"""