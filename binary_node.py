class BinaryNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None



class BinaryTree:
    def __init__(self) -> None:
        self.head = None

    def insert_node(self, data):
        node = BinaryNode(data)
        print(f"\ninserting {data}...\n")
        
        if self.head is None:
            self.head = node
            print(f"head is {self.head.data}")
            return       
        #check if data in head first, then check if new data is greater, less or equal. If equal end, if the other two check if None exists in slot and insert new node if yes...
        #otherwise change the current node to that node and rerun checks 
        current_node = self.head
        while current_node is not None:
            print(f"current node: {current_node.data}")
            #check not doubling data
            if node.data == current_node.data:
                print("duplicate value")
                return 
            elif node.data > current_node.data:
                if current_node.right is None:
                    current_node.right = node
                    print(f"inserting {data} node to right")
                    return
                current_node = current_node.right
                print("going right")
            elif node.data < current_node.data:
                if current_node.left is None:
                    current_node.left = node
                    print(f"inserting {data} node to left")
                    return
                current_node = current_node.left
                print("going left")
        print(f"Node with value {current_node.data} inserted")


    def search_for_node(self, target):
        if self.head.data == target:
            return True
        
        current_node = self.head
        while current_node is not None:
            print(f"current node is {current_node.data}")
            if target == current_node.data:
                print(f"the target of {target} was found")
                return True
            elif target > current_node.data:
                print("searching right")
                current_node = current_node.right
            elif target < current_node.data:
                print("searching left")
                current_node = current_node.left
        print(f"Target value of {target} not found")
        return False

