"1. While loop"
"While loop with increment"
i = 1
while i < 10:
    print(i)
    i = i+1

# "While loop with decrement"
i = 10
while i >= 1:
    print(i)
    i = i -1

# eg:2
i = 1
while i <10:
    print(i)
    i += 1

"While loop using break statement"

i = 1
while i < 10:
    print(i)
    if(i ==6):
        break
    i = i +1

"While loop using Continue statement"
i = 0
while i < 10:
    i = i +1
    if(i == 6):
        continue
    print(i)

"While loop using Else condition"

i = 1
while i < 10:
    print(i)
    i = i+1
else:
    print("Condition get satisfied")
