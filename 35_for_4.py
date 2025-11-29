# count no of values in list 
numbers = [25,10,45,5,30,9,87,36,40,51,150,99]
count = 0
for num in numbers:
    print(num,end=' ')
    count+=1
print() #insert new line
print(f"total no of values = {count}")

# count odd and even values 
odd = 0 
even = 0 
for num in numbers:
    if num%2==0: #even 
        even+=1
    else:
        odd+=1
print(f"odd = {odd} even = {even}")

#findout maximum value in unsorted list 
max = numbers[0] #assume 1st item in list is maximum 25
for num in numbers:
    if max<num:
        max = num #max = 45
    num = 0
print(f"list has maximum value {max}")
print(numbers)