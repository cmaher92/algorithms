class Node:
    # By default, both the cargo and the link, next, are set to None
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

    # The string representation of the node is the string representation of the
    # cargo, any value can be stored in the cargo
    def __str__(self):
        return str(self.cargo)

    def getCargo(self):
        return self.cargo

    def getNext(self):
        return self.next

    def setCargo(self, new_cargo):
        self.cargo = new_cargo

    def setNext(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.length = 0 # contains the length of the list
        self.head   = None # reference to the first node

    def size(self):
        return self.length

    def traverse(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getCargo() == item:
                found = True
            else:
                current = current.getNext()

    def removeNode(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getCargo() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            # if item is first in list set new head to be the next node
            self.head = current.getNext()
        else:
            # otherwise set the previous next pointer to the next node
            previous.setNext(current.getNext())



    def isEmpty(self):
        return self.head = None
        # only will return True if the LinkedList object has no head

    def insertAtFirst(self, cargo):
        node = Node(cargo) # create a variable of the node instance
        node.setNext = self.head # set the new node's pointer to prev 1st node
        self.head = node # changes the class' reference to the new node
        self.length = self.length + 1 # increments the length of list by 1

    def insertAtTail(self, cargo):
        node = Node(cargo)
        # find the last node
        # set the last node's pointer to new node
        # increment the length of the list by 1



def print_list(node):
    while node:
        print node,
        node = node.next
    print
