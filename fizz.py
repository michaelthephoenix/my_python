x = list(input())
y = list(input())
print(x)
print(len(x))
print(y)
print(len(y))
add = len(x) + len(y)
print(add)
if add % 3 == 0 and add % 5 != 0:
    print("fizz")
if add % 5 == 0 and add % 3 != 0:
    print("buzz")
if add % 3==0 and add % 5==0:
    print("fizzbuzz")
