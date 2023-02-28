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
        #print(f"\ninserting {data}...\n")
        
        if self.head is None:
            self.head = node
            #print(f"head is {self.head.data}")
            return       
        #check if data in head first, then check if new data is greater, less or equal. If equal end, if the other two check if None exists in slot and insert new node if yes...
        #otherwise change the current node to that node and rerun checks 
        current_node = self.head
        while current_node is not None:
            #print(f"current node: {current_node.data}")
            #check not doubling data
            if node.data == current_node.data:
                print("duplicate value")
                return 
            elif node.data > current_node.data:
                if current_node.right is None:
                    current_node.right = node
                    #print(f"inserting {data} node to right")
                    return
                current_node = current_node.right
               # print("going right")
            elif node.data < current_node.data:
                if current_node.left is None:
                    current_node.left = node
                    #print(f"inserting {data} node to left")
                    return
                current_node = current_node.left
                #print("going left")
        #print(f"Node with value {current_node.data} inserted")


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



    def in_order_traversal(self):
        result = []
        current = self.head
        node_list = [current]
        #check for empty tree
        if current is None:
            return
        while len(node_list) > 0:
            result.append(node_list[0].data)
            if current.left is not None:
                node_list.append(current.left)
            if current.right is not None:
                node_list.append(current.right)
            
            del node_list[0]
            if len(node_list) > 0:
                current = node_list[0]
        print(f"Unordered list is {result}")
        result.sort()
        print(f"In order traversal results: {result}")
        return result
    
    

    def pre_order_traversal(self):
        current = self.head
        if current is None:
            return
        result = [self.head.data]
        node_list = []
        lrtraversal = [current.left, current.right]

        for x in lrtraversal:
            current = x
            node_list.append(current)
            while len(node_list) > 0:
                result.append(node_list[0].data)
                if current.left is not None:
                    node_list.append(current.left)
                if current.right is not None:
                    node_list.append(current.right)
                del node_list[0]
                if len(node_list) > 0:
                    current = node_list[0]

        print(f"Pre order traversal results: {result}")
        return result       



    def post_order_traversal(self):
        current = self.head
        if current is None:
            return
        result = []
        node_list = []

        #traverse left 
        current = current.left
        node_list.append(current)
        while len(node_list) > 0:
            result.insert(-1, node_list[0].data)
            del node_list[0]
            if current.left is not None:
                node_list.insert(0, current.left)
            if current.right is not None:
                node_list.insert(1, current.right)
            if len(node_list) > 0:
                current = node_list[0]
            
        
        #traverse right
        list2 = []
        current = self.head.right
        node_list.append(current)
        while len(node_list) > 0:
            list2.insert(-1, node_list[0].data)
            del node_list[0]
            if current.left is not None:
                node_list.insert(0, current.left)
            if current.right is not None:
                node_list.insert(1, current.right)
            if len(node_list) > 0:
                current = node_list[0]
        
        list2.append(self.head.data)

        result.extend(list2)

        print(f"Post order traversal results: {result}")
        return result        


'''
    def grab_next_nodes_data(self, node):
        result = []
        if node.left and node.left.data not in result:
            temp = self.grab_next_nodes_data(node.left)
            result.extend(temp)
        elif node.right is not None and node.right.data not in result:
            result.extend(self.grab_next_nodes_data(node.right))
        else: 
            result.append(node.data)
        return result
        

    def broken_in_order_traversal(self):
        result = []
        #check for empty
        if self.head is None:
            print("nothing to traverse")
            return
        #traverse
        result.append(self.grab_next_nodes_data(self.head))
        
        return result

'''
            
            #grab current node data 
            #checking if there are values in left and right
            #if so save them to temporary list 
            #choose 1 of them, and remove that node from temporary list 
            #grab its data and check again if values left and right
            #if so choose 1 of them, and remove node from temporary list
            #etc
            #when no values remain in temporary list or left/right return the data list
            


        #check if left is empty, if not set as new node
        #go until none found, then check right
        #if nothing, return value 






#trash heap of attempted solutions:

"""
while current.left is not None and current.right is not None:
            if current.left is not None and current.left.data not in result:
                result.append(current.left.data)
            if current.right is not None and current.right.data not in result:  
                result.append(current.right.data)
            if current.left.left is not None and current.left.left.data not in result:
                current = current.left
                continue
            if current.right.right is not None and current.right.right.data not in result:
                current = current.right
                continue
        return result"""

"""
   def grab_next_nodes_data(self, node):
        result = []
        if node.left is not None and node.left.data not in result:
            result.extend(self.grab_next_nodes_data(node.left))
        elif node.right is not None and node.right.data not in result:
            result.extend(self.grab_next_nodes_data(node.right))
        else: 
            result.append(node.data)
            return result
        

    def in_order_traversal(self):
        result = []
        #check for empty
        if self.head is None:
            print("nothing to traverse")
            return
        #traverse
        result.append(self.grab_next_nodes_data(self.head))
        
        return result
        
        


    def pre_order_traversal(self):
        current = self.head
        if current is None:
            return
        result = [self.head.data]
        node_list = []

        #traverse left 
        current = current.left
        node_list.append(current)
        while len(node_list) > 0:
            result.append(node_list[0].data)
            if current.left is not None:
                node_list.append(current.left)
            if current.right is not None:
                node_list.append(current.right)
            del node_list[0]
            if len(node_list) > 0:
                current = node_list[0]
        
        #traverse right
        current = self.head.right
        node_list.append(current)
        while len(node_list) > 0:
            result.append(node_list[0].data)
            if current.left is not None:
                node_list.append(current.left)
            if current.right is not None:
                node_list.append(current.right)
            del node_list[0]
            if len(node_list) > 0:
                current = node_list[0]

        print(f"Pre order traversal results: {result}")
        return result"""       
