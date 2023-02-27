from linked_list import LinkedList
from binary_node import BinaryTree

# my_list = LinkedList()

# my_list.append_node(20)
# my_list.append_node(45)
# my_list.append_node(60)

# print(my_list.find_node(60))
# print(my_list.find_node(90))


my_tree = BinaryTree()

my_tree.insert_node(27)
my_tree.insert_node(14)
my_tree.insert_node(35)
my_tree.insert_node(10)
my_tree.insert_node(19)
my_tree.insert_node(31)
my_tree.insert_node(42)

print("\n\nNow trying search function: \n")
my_tree.search_for_node(32)
