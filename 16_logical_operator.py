#use of logical operator (and, or, not)
num1 = int(input("Enter value for num1"))
num2 = int(input("Enter value for num2"))
num3 = int(input("Enter value for num3"))

result = num1 == num2 and num2 == num3
print(f"and -> {result} = {num1} == {num2} and {num2} == {num3}")

result2 = num1 == num2 or num2 == num3
print(f"or -> {result2} = {num1} == {num2} or {num2} == {num3}")

result3 = not (num1 == num2 and num2 == num3)
print(f"not -> {result3} = not ({num1} == {num2} and {num2} == {num3})") 