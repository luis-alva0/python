# Multiple assignments
n, m = 0, "abc"

# Increment
n = + 1
n += 1

# None is null
n = 4
n = None

# If statements 
n = 1
if n > 2:
    n -= 1
elif n == 2:
    n *= 2
else:
    n += 2

# Parentheses needed for multi-line conditions
# and = &&
# or = ||

n, m = 1, 2
if ((n > 2 and n != m) or n == m):
    n += 1

# While loops
n = 0
while n < 5:
    print(n)
    n += 1

# For loops
for n in range(5):
    print(n)

for i in range(2, 6):
    print(i) # from 2 to 5

for i in range(5, 1, -1):
    print(i) # from 5 to 2

# Division is decimal by default
print(5/2) # 2.5
print(5 // 2) # 2

# Modular
print(10 % 3) # 1

# Math
import math

print(math.fmod(-10, 3)) # -1.0 
print(math.floor(3 / 2))
print(math.ceil(3 / 2))
print(math.sqrt(2))
print(math.pow(2, 3))

# Max / Min int
float("inf")
float("-inf")

print(math.pow(2, 200) < float("inf")) # true

# Array
arr = [1, 2, 3]
print(arr)

arr.append(4)
arr.pop()
arr.insert(1, 7) # O(n)
arr[0] = 0 # O(1)

# Initialize arr of size n with default value of 1
n = 5
arr = [1] * n

# Miscelaneous
print(arr[-1]) # read the last item of an array
print(arr[-2]) # next to last
print(arr[1:3]) # sublist from index 1 to index 2

# Unpacking
a, b, c = [1, 2, 3]

# Looping through arrays
nums = [1, 2, 3]

for i in range(len(nums)):
    print(nums[i])

for n in nums:
    print(n)

for i, n in enumerate(nums):
    print(i, n) # item and index

# Loop through multiple arrays simultaneously with unpacking
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]

for n1, n2 in zip(nums1, nums2):
    print(n1, n2)

# Array functions
arr = [5, 4, 6, 3, 8]
arr.reverse()
arr.sort()
arr.sort(reverse=True)

arr = ["bob", "alice", "jane", "doe"]
arr.sort() # default sort by alphabetical order
arr.sort(key=lambda x: len(x)) # custom sort (by lenght of string)

# List comprehension
arr = [i for i in range(5)]
print(arr) # [0, 1, 2, 3, 4]

arr = [i+i for i in range(5)]
print(arr) # [0, 2, 4, 6, 8]

# Strings
s = "abc"
print(s[0:2])
s += "def" # O(n)

# ASCII
print(ord("a"))

# Combine a list of strings (with an empty string delimitor)
strings = ["abc", "de", "fg"]
print("".join(strings))

# Queues
from collections import deque
queue = deque()
queue.append(1)
queue.popleft()
queue.appendleft(1)
queue.pop()

# HashSet
mySet = set()
mySet.add(1)
mySet.add(2)
print(mySet, len(mySet))
print(1 in mySet)
mySet.remove(2) # O(1)

print(set([1, 2, 3])) # List to Set

mySet = {i for i in range(5)} # Set comprehension

# Hashmap (aka dict)
myMap = {}
myMap["alice"] = 88
print(myMap, len(myMap))
print(myMap["alice"])
myMap.pop("alice") # O(1)
print("alice" in myMap)

myMap = {"Alice": 90, "Bob": 70}

myMap = { i: 2*i for i in range(3)} # dict comprehension
print(myMap) # {0: 0, 1: 2, 2: 4}

for key in myMap:
    print(key, myMap[key])

for val in myMap.values():
    print(val)

for key, val in myMap.items():
    print(key, val)

# Tuples
# like arrays but inmutable

tup = (1, 2, 3)
print(tup[0])

myMap = {(1, 2): 3} # using tuples as a key because list can not be keys

# Heaps
import heapq

# to find min and max

minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

print(minHeap[0]) # 2

while len(minHeap):
    print(heapq.heappop(minHeap)) # from smallest to largest

# work around for max heaps

maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)

print(-1 * maxHeap[0])

while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap)) # from larges to smalles

# Build heap from inicial values
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))

# Functions

def myFunc(n, m):
    return n * m

# Nested functions

def outer(a, b):
    c = "c"
    
    def inner():
        return a + b + c
    return inner()

print(outer("a", "b"))

# Classes

class MyClass:
    def __init__(self, nums):
        self.nums = nums
        self.size = len(nums)
    
    def getLenght(self):
        return self.size
    
    def getDoubleLenght(self):
        return 2 * self.getLenght()
    
myObj = MyClass([1, 2, 3])
print(myObj.getLenght())
print(myObj.getDoubleLenght())