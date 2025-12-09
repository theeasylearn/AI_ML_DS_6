#example of keyword arguments 
def getMerit(maths,science,english,computer,history,drawing):
    print(f"maths ={maths},science = {science},english = {english},computer = {computer},history = {history},drawing = {drawing}")
    total = maths + science + english
    return total 

m = int(input("Enter maths marks: "))
s = int(input("Enter science marks: "))
e = int(input("Enter english marks: "))
c = int(input("Enter computer marks: "))
h = int(input("Enter history marks: "))
d = int(input("Enter drawing marks: "))

print("merit = ",getMerit(english=e,computer=c,history=h,drawing=d,maths=m,science=s))
