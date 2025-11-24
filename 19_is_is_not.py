num1 = int(input("Enter value for num1"))
num2 = int(input("Enter value for num2"))

result = num1 is num2
print("location(address in ram) of num1 =",id(num1))
print("location(address in ram) of num2 =",id(num2))

print(f"{result} = {num1} is {num2}")

result = num1 is not num2
print(f"{result} = {num1} is not {num2}")
