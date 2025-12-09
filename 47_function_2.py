#default argument function 
def getInterest(amount,rate=12,year=5):
    print(f"amount {amount},rate {rate},year {year}")
    interest = (amount * rate * year) / 100
    return interest

a = int(input("Enter amount"))
r = int(input("Enter rate"))
y = int(input("Enter year"))

interest = getInterest(a,r,y) #3 argument 
print("interest using 3 argument",interest)

interest = getInterest(a,r) #here year will be 5
print("interest using 2 argument",interest)

interest = getInterest(a) #here year will be 5
print("interest using 1 argument",interest)

