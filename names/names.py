import time
from bst import bst

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


duplicates = []  # Return the list of duplicates in this data structure

# STRETCH STARTS
# set_1 = set(names_1)
# set_2 = set(names_2)
# duplicates = list(set_1.intersection(set_2))
# STRETCH ENDS

# create new tree and set the root value
tree = bst(names_1[0])

# loop over names_1 list and insert names to tree
# so I could utilise bst contains method on it
for name in names_1:
    tree.insert(name)
# loop over names_2 list and pass each name to contains method
# of tree in order to find duplicates
# append to duplicates list if found
for name in names_2:
    if tree.contains(name):
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

