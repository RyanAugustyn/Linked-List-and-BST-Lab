#instructor video on how to build and sort binary search tree


class BinarySearchNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None 

    #Insert mode uses Post-order transversal: Left->Right->Root
    def insert_node(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinarySearchNode(data)
                else:
                    self.left.insert_node(data) #recursion 
            elif data > self.data:
                if self.right is None:
                    self.left = BinarySearchNode(data)
                else:
                    self.left.insert_node(data)
            else:
                self.data = data #establish root node 

    #Search mode uses Pre-order transversal: Root->Left->Right
    def search_for_node(self, root, data):
        if root:
            if data == root.data:
                print("Node found!")
            elif data < root.data:
                print("Direction left")
                self.search_for_node(root.left, data)
            elif data > root.data:
                print("Direction left")
                self.search_for_node(root.right, data)
        else:
            print("Node not found")
        return
    

    #in order transversal: left, root, right
    def print_tree(self):
        #Process left side
        if self.left:
            self.left.print_tree()
        #Handle the root/current node
        print(self.data)
        #process right side
        if self.right:
            self.right.print_tree()

    #in-order traversal: left, root, right
    #like the print_tree(), uses same traversal, but takes 'root' as a 
    #parameter and uses recursion to build a list 
    def inorder_traversal(self,root):
        result = []
        if root:
            result = self.inorder_traversal(root.left)
            result.append(root.data)
            result = result + self.inorder_traversal(root.right)
        return result
    
    #pre order traversal
    #root, left, right
    def preorder_traversal(self, root):
        result = []
        if root:
            result.append(root.data)
            result = result + self.preorder_traversal(root.left)
            result = result + self.preorder_traversal(root.right)
        return
    
    #left, right, root
    def postorder_traversal(self, root):
        result = []
        if root:
            result = self.preorder_traversal(root.left)
            result = result + self.preorder_traversal(root.right)
            result.append(root.data)
        return result

            
