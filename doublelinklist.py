from node import Node
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def print_multilist(self, level=0):
        if self.head is None:
            print("Empty list"); return
        current = self.head
        while current:
            print("  " * level + str(current))
            if current.sub_list:
                current.sub_list.print_multilist(level + 1)
            current = current.next

    def search_by_attr(self, attr, value):
        current = self.head
        while current:
            if getattr(current, attr) == value:
                return current
            current = current.next
        return None
    
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def add_child(self, parent:Node, child:Node):
        if parent.sub_list is None:
            sublist = DoubleLinkedList()
            sublist.head = child
            sublist.tail = child
            parent.sub_list = sublist
        else:
            current = parent.sub_list.tail
            current.next = child
            child.prev = current
            parent.sub_list.tail = child
        return parent.sub_list