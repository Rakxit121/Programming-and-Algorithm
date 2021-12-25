# Write a Python script to check if a given key already exists in a dictionary.
a = input("Enter a key to remove from Dictionary if present: ")
integer = {"first": 1, "second": 2, "third": 3, "tenth": 10, "seventy": 70}
b = 0

for key, value in integer.items():
    if key == a:
        print(a, " already exist as key in dictionary ' ", integer, " '")
        break
    else:
        b = b + 1

if b == len(integer):
    print(a, " is Not found in Dictionary : '", integer, "'")
