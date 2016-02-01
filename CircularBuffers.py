# Vectors
# Linked Lists
# Circular
# Resizable Arrays

# Circular Buffers
# The useful property of a circular buffer is that it does not need to
# have its elements shuffled around when one is consumed.
# circular is FIFO

# Alan's definition
# Array with many cells, wraps around
# An example is an array of 30 frames, each object is a single frame


# A circular buffer can be implemented using four pointers,
# or two pointers and two integers:

# buffer start in memory
# buffer end in memory, or buffer capacity
# start of valid data (index or pointer)
# end of valid data (index or pointer), or amount of data currently in the buffer (integer)

# methods
# insert
