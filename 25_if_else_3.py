#Write a program that to accept birth month from user and display how many days are there in month
month = int(input("Enter your birth month (1 to 12)"))
# 1,3,5,7,8,10,12 has 31 days
# 4 6 9 ,11  has 30 days
# 2 has 28-29 days
if month==4 or month==6 or month==9 or month==11:
    print("this month has 30 days")
elif month==2:
    print("this month has 28/29 days")
else:
    print("this month has 31 days")