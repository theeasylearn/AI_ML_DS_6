# working with list 
fruits = ['banana','mango','orange','apple','graps']
box = [100,'pinapple',3.14,True,None,False]
print(fruits) # ['banana','mango','orange','apple','graps']
print(fruits[0]) # banana 
print(fruits[2]) # orange
print(fruits[1:4]) # mango orange apple 
print(fruits[2:]) #orange apple graps
print(fruits*2) # ['banana','mango','orange','apple','graps'] ['banana','mango','orange','apple','graps']
print(fruits + box)

#we can change list as list is mutable 
fruits[0] = "Kiwi"
del fruits[1] #delete mango 
#we can also insert new value 
fruits.append('coconut')
print(fruits) 
