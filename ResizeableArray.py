# Vectors
# Linked Lists
# Circular
# Resizable Arrays

# Risizable Arrays / Dynamic Arrays
# Physical size - maximum possible size without relocating data-turbolinks-track
# An array that can shrink and grow in size, constantly considering memory implications
# Ruby & Python the arrays do this automatically


# Psuedocode
# Start with an array
# When the array reaches max-size create a new array double the size
# Shift all of the previous elements to the new array
#

# Growth Factor
# Consider how much copying you would have to do
# Doubling array limits the n of times you have to create new array
# n work / n insertions (amortized) 1/1 O(1)

# Potential Challenges
# Example of arrays that are often fragmented are user_id's because they are
# given out incrementally

# Prevention to Overcome Challenges
# A way to prevent this would be using a sparse array
# Hashtable
