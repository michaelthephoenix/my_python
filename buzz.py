def fizzbuzz(list1, list2):
    total_lenght = len(list(list1)) + len(list(list2))
    print(int(total_lenght))
    #conditions
    if total_lenght % 3 == 0 and total_lenght % 5 != 0:
        print("fizz")
    if total_lenght % 5 == 0 and total_lenght % 3 != 0:
        print("buzz")
    if total_lenght % 3 == 0 and total_lenght % 5 == 0:
        print("fizzbuzz")

fizzbuzz([1, 2, 3, 4, 5], [1,2,3,4,5,6,7,8,9,0])
print(12 % 3)