# Write a Python program to multiply all the items in a list.

import math

data = [1, 2, 3, 4, 5]
mult_total = math.prod(data)

print(f"The multiplies of all item in a list: {data} is {mult_total}")

# OR

j = 1
if len(data) >= 1:
    for i in data:
        j = j * i
else:
    j = 0
print(f"The multiplies of all item in a list: {data} is {j}")
