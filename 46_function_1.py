# Without return value without argument
def printLine():
    print("_"*100)
# Without return value with argument 
def printLetter(letter,howManyTimes):
    print(letter*howManyTimes)
# With return value without argument
def getPi():
    pi = 22 / 7.0 #here pi is local variable (we can use pi variable only inside getPi function)
    return pi 

# With return value with argument 
def getSquare(number):
    #here square is local variable (we can use pi variable only inside getPi function)
    square = number * number  
    return square

printLine() #function call/execute
print("the easylearn academy")
printLine() 
print("AI/ML/DS, Web Development, Mobile app development/ Cyber Security / UI/UX ")
printLetter('*',120)
print('105,223, opp aksharwadi temple, waghawadi road, bhavnagar')
printLetter('^',180)
result = getPi()
print(f"value of pi = {result}")

num = int(input("Enter any one number"))
result = getSquare(num)
print(f"square of {num} = {result}")