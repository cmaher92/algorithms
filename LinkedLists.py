# Vectors
# Linked Lists
# Circular
# Resizable Arrays

# Linked Lists
# In its most basic form, a linked list is a string of nodes,
# sort of like a string of pearls, with each node containing both data and a
# reference to the next node in the list (Note: This is a singly linked list.
# The nodes in a doubly linked list will contain references to both the next
# node and the previous node)

# Main Advantage
# The main advantage of using a linked list over a similar data structure,
# like the static array, is the linked list’s dynamic memory allocation:

# If you don't know the amount of data you want to store before hand,
# the linked list can adjust on the fly.

# Disadvantage
# *In practice this means certain insertions are more expensive. For example,
# if the list initially allocates enough space for eight nodes, on the
# ninth insertion the list will have to double its allocated space to 16 and
# copy over the original 8 nodes, a more expensive operation than a normal insertion.

# Challenge
# What if somebody is putting in a linked LinkedList that has a node that references
# the wrong node, creating a loop, what would be the function to detect this



# Node class
# -item
# -next

# LinkedList class
# +insert (insertAtTail, insertAtPosition, insertAtIndex)
# +delete (head, tail, index, value)
# +search(item) -> index
# +isEmpty
# +size
# +clear
# -head
# -count -=1 +=1
