# example of how to take input from user
# write a program to accept age from users and calculate & display user's age in days 
age = input("Enter your age")
#convert string input into integer
age = int(age)
#calculate days 
days = age * 365
#display user's age in year and days

print(f"age in years = {age} in days = {days}")
