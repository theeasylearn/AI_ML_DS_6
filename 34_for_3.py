#Qs:1 print all elements

fruits=['apple','banana','papaya','pineapple','tomato']

for fruit in fruits:
    print(fruit)

print("Good Bye")

#Qs:2 count number of items

vegetables = ("Potato", "Tomato", "Onion", "Brinjal", "Okra")

count=0
for vege in vegetables:
    count=count+1
print("Total number of elements: ",count)

#Qs:3 calculate total & Average

marks = {"Math": 88, "English": 75, "Science": 92, "History": 80, "Geography": 78, "Computer": 95}

total=0
count=0
for mark in marks:
    total=total+marks[mark]
    count=count+1
    
print("Total Marks: ",total)
print("Total number of subject: ",count)
ave=total/count
print("Average marks: ",ave)