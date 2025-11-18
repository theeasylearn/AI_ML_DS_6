# write a program to convert hours into minutes & seconds
'''
    take input into hours variable
    convert string hours into integer hours
    multiply hours with 60 and store into minutes
    multiply minutes with 60
    display hours and minutes
'''
hours = input("Enter hours")
hours = int(hours)
minutes = hours * 60
seconds = minutes * 60
print(f"hours = {hours} minutes = {minutes} seconds = {seconds}")
