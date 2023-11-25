from Node import Node

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.length = 1

    def print_stack(self):
        temp = self.top
        while temp != None:
            print(temp.value)
            temp = temp.next
    
    def add(self, value):
        new_node = Node(value)
        if self.top == None:    
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1
        return new_node.value
    
    def pop(self):
        if self.top == None:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.length -= 1
            return temp.value