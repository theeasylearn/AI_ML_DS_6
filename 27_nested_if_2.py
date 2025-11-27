#write a program to findout whether given year is leap year or not
year = int(input("Enter year"))
if year<=0:
    print("invalid year, year must be above 0")
else:
    reminder1 = year % 4 
    reminder2 = year % 100
    reminder3 = year % 400
    print(reminder1,reminder2)
    if reminder1==0 and reminder2!=0:
        print("it is leap year")
    elif reminder2==0 and reminder3==0:
        print("it is leap year")
    else:
        print("it is not leap year")
