# "For loop using range value"
#
# for i in range(0,10):
#     print(i)
#
# for i in range(10):
#     print(i)
#
# for i in range(0,10,2):
#     print(i)
#
# "Print even numbers"
# for i in range(0,21,2):
#     print(i)

"Print odd numbers"
# for i in range(1,21,2):
#     print(i)
# "On Reverse value"
# for i in range(20,0,-2):
#     print(i)

# fruits = ["Cherry", "Bannana", "Apple"]
# for x in (fruits):
#     print(x)

"Loop using strings"

# for x in "Bannana":
#     print(x)

"Using Break statement"
fruits = ["Cherry", "Bannana", "Apple"]
for x in (fruits):
    print(x)
    if x == "Bannana":
        break

fruits = ["Cherry", "Bannana", "Apple"]
for x in (fruits):
    if x == "Bannana":
        break
    print(x)

"Using Continue Statement"
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)