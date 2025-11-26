#write a program to accept product purchrase & sales price and findout profit or loss or break even amount (use if elif decision)
purchase_price = int(input("Enter product purchase price"))
sales_price = int(input("Enter product sales price"))

difference = sales_price - purchase_price
if difference>0: 
    print(f"you have earned profit of {difference} amount")
elif difference<0:
    print(f"you have made loss of {difference} amount")
elif difference==0:
    print(f"you have made no loss and earned no profit, break even")
print("Good bye....")
