import time
import collections

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements



# ========== Original Solution ==========

# class BSTNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

#     def insert(self, value):
#         if self is None:
#             self = BSTNode(value)
#         else:
#             if value < self.value:
#                 if self.left is None:
#                     self.left = BSTNode(value)
#                 else:
#                     self.left.insert(value)
#             else:
#                 if(value == self.value):
#                     duplicates.append(value)
#                 if self.right is None:
#                     self.right = BSTNode(value)
#                 else:
#                     self.right.insert(value)

# bst = BSTNode("")
# for name_1 in names_1:
#     bst.insert(name_1)
# for name_2 in names_2:
#     bst.insert(name_2)




# ========== Stretch Solution ==========

biglist = []
for x in names_1:
    biglist.append(x)
for x in names_2:
    biglist.append(x)
duplicates = ([item for item, count in collections.Counter(biglist).items() if count > 1])


# Original Runtime: 6.978585720062256 seconds
# Improved Runtime: 0.10893392562866211 seconds
# Stretch runtime: 0.008994340896606445 seconds
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.


