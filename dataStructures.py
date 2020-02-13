""" data structures used """

class DoublyNode():

    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList():

    def __init__(self):
        self.len = 0
        self.head = None
        self.tail = None


    def append(self, data):
        """ Adds a Node to the end of the linked list"""
        if self.head == None:
            self.head = DoublyNode(data)
            self.tail = self.head
            self.len += 1
        else:
            self.tail.next = DoublyNode(data)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
            self.len += 1


    def insert_between(self, data, node1, node2):
        """ Inserts a node between to other nodes """

        # Traversing to node1
        traverse_point = self.head
        while ((traverse_point.data != node1) and (traverse_point.next.data != node2)):
            traverse_point = traverse_point.next

        new_node = DoublyNode(data)

        # Setting new nodes next and prev to node1 and node2 respectivly
        new_node.next = traverse_point.next
        new_node.prev = traverse_point

        # Setting the next and prev of node1 and node2 respectivly to new_node
        traverse_point.next.prev = new_node
        traverse_point.next = new_node

        self.len += 1


    def remove(self,data):
        """ Removing a node """

        removed = True

        # Checking for special case: Head being removed
        if self.head.data == data:
            self.head = self.head.next
            self.head.prev.next = None
            self.head.prev = None

            # Reduce length of list
            self.len -= 1

        else:

            #Traversing to node to be removed
            traverse_point = self.head
            while traverse_point.data != data:
                if traverse_point.next:
                    if traverse_point.data == data:
                        # Removing Node, deallocate memory
                        traverse_point.prev.next = traverse_point.next
                        traverse_point.next.prev = traverse_point.prev
                        traverse_point = None
                        # Reduce length of list
                        self.len -= 1
                        break

                    traverse_point = traverse_point.next

                else:
                    print("Node " + str(data) + " does not exist")
                    removed = False
                    break

        if removed:
            print("Node " + str(data) + " removed")


    def head_insert(self, data):
        """ Insert at the head """

        new_node = DoublyNode(data)

        # Connecting new node to current head and setting node as current head
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

        self.len += 1
