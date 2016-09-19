

class LinkedList():
    head_node = None
    tail_node = None
    number_of_nodes = None

    def __init__(self):
        self.number_of_nodes = 0

    def add_node_to_end(self, data):
        self.number_of_nodes += 1
        NODE = Node()
        if not self.head_node:
            self.head_node = NODE
            self.tail_node = NODE
            NODE.data = data
        elif self.head_node:
            self.tail_node.next_node = NODE
            self.tail_node = NODE
            NODE.data = data
        else:
            print "Something went wrong: LinkedList.add_node_to_end()"

    def print_all_nodes(self):
        current_node = self.head_node
        while True:
            print "Node Data: ", current_node.data
            if current_node == self.tail_node:
                break
            current_node = current_node.next_node


class Node(object):
    data = None
    next_node = None



L = LinkedList()
L.add_node_to_end(1)
L.add_node_to_end(2)
L.print_all_nodes()