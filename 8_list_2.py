#list related methods 
fruits = [] #empty list 
fruits.append('banana')
fruits.append('apple')
fruits.append('orange')
fruits.append('coconut')
fruits.append('coconut')
#insert item at begining
fruits.insert(0,'kiwi')
fruits.insert(1,'mango')
print(fruits)
fruits.remove('apple') #remove by value
print(fruits)
fruits.pop(1) #remove by position
print(fruits)
position = fruits.index('orange') #2
print(position)
coconut_count = fruits.count('coconut')
print(coconut_count)
vegis = ['potato','brinjal','tomato']
fruits.extend(vegis)
print(fruits)
vegis.clear()
print(vegis)
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
fruits2 = fruits.copy() #correct way
#fruits2 = fruits wrong way 
print(fruits,fruits2)
fruits2.clear()
print(fruits,fruits2)
