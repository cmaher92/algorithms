# Binary search

# Notes:
# Psuedocode is preferred while discussing algorithms because of the variance in languages


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 6, 1,
          67, 71, 73, 79, 83, 89, 97]

correct = "We have found the target"

# array primes contains 25 numbers
# 0 represents the smallest index of the list
# min = 0
# max represents the largest index of the list
# max = 24

# Psuedocode
# Let min = 0 and max = n-1.
# Compute guess as the average of max and min, rounded down (so that it is an integer).
# If array[guess] equals target, then stop. You found it! Return guess.
# If the guess was too low, that is, array[guess] < target, then set min = guess + 1.
# Otherwise, the guess was too high. Set max = guess - 1.
# Go back to step 2.
# https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/implementing-binary-search-of-an-array


# Implementation
def binarySearch(primes, min, max, target):
    n = (min + max) // 2
    if primes[n] == target:
        print(correct)
        print(primes[n])
    elif primes[n] < target:
        print("Guess is below target, guessing again")
        binarySearch(primes, n+1, max, target)
    else:
        print("Guess is above target, guessing again")
        binarySearch(primes, min, n-1, target)

binarySearch(primes, 0, len(primes) - 1, 37)

# While loop is probably a better choice
