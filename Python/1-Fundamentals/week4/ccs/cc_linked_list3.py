class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print("Head Node created:", self.head.value)
            return

        node = self.head
        while node.next is not None:
            node = node.next

        node.next = new_node
        print("Append new Node with value:", node.next.value)

    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print("Head Node created: ", self.head.value)
            return

        node = self.head
        while node is not None:
            node = new_node
            print("Prepended new Head Node with value:", node.value)
            node = node.next
            print("Node following Head is:", node.value)


llist = LinkedList()
llist.prepend("First Node")
llist.prepend("Inserted New First Node")
