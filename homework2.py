# calculator that will support basic math operations
# 1 - ADD
# 2 - SUBTRACT
# 3 - MULTIPLY
# 4 - DIVIDE
print("Choose an operation")
print("1 - ADD")
print("2 - SUBTRACT")
print("3 - MULTIPLY")
print("4 - DIVIDE")

operation = input()

a = input("Enter first number ")
b = input("Enter second number ")

if  operation == "1":
    print("Sum of given 2 numbers equals to " + str(int(a) + int(b)))
elif operation == "2":
    print("The difference of given 2 numbers is " + str(int(a) - int(b)))
elif operation == "3":
    print("The product of given 2 numbers is " + str(int(a) * int(b)))
elif operation == "4":
    print("The result is " + str(int(a) / int(b)))
else :
    print("ERROR")
