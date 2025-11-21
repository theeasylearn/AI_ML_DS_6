fruits = {'Papaya', 'Orange', 'Guava', 'Kiwi', 'Apple', 'Mango', 'Watermelon', 'Grape', 'Pineapple', 'Strawberry', 'Banana', 'Pomegranate'}
fruits.add('Cherry')
fruits.remove('Papaya')
print(fruits)

list = ['Apple', 'Banana', 'Mango', 'Orange', 'Apple', 'Grape', 'Pineapple', 'Strawberry', 
 'Banana', 'Watermelon', 'Kiwi', 'Mango', 'Pomegranate', 'Apple', 'Guava']
print(list)
#convert list into set (remove duplicate value if any )
list2 = set(list)
print(list2)

num1 = {1,2,3}
num2 = {2,3,4}

#create set which has unique value from both set
union = num1.union(num2)
print(union)

#create set which has common value from both set
intersection = num1.intersection(num2)
print(intersection)

#get values which exists in set1 but not in set2
difference = num1.difference(num2)
print(difference)