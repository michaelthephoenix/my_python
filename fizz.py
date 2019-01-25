
x = list(input())
y = list(input())
print(x)
length_1 = len(x)
print("the length of the list_1 is " + str(length_1))
print(y)
length_2 = len(y)
print("the length of the list_2 is " + str(length_2))
add = len(x) + len(y)
print("the length of both lists is " + str(add))
def fizzbuzz():
    if add % 3 == 0 and add % 5 != 0:
        print("fizz")
    if add % 5 == 0 and add % 3 != 0:
        print("buzz")
    if add % 3==0 and add % 5==0:
        print("fizzbuzz")

fizzbuzz()



