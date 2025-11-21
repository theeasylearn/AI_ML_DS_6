subject = {'name':'AI/ML/DS','trainer':'Ankit Patel','duration':240,'isCertified':True}

#copy dictionary into another dictionary
subject2 = subject.copy()
print(subject)
subject2.update({'name':'cyber security'}) #update existing key value pair
subject2.update({'fees':50000}) #it creates new key value pair
print(subject2)
print(subject2['fees'])
# print(subject2['city'])
# above line generate error if key does not exists, to overcome that situation we have to use 
print(subject2.get('city'))
print(subject2.get('city','not found'))

#get keys of dictionary
print(subject2.keys())

#get all values of dictionary
print(subject2.values())

#get all items of dictionary
print(subject2.items())

#remove specific key & value from dictionary
subject2.pop('duration')
#remove last key & value pair
subject2.popitem()
print(subject2)

student = ['name','mobile','email']
#let us create dictionary using list 
madhav = dict.fromkeys(student)
print(madhav)
madhav.update({'name':'madhav zanzrukiya'})
madhav.update({'mobile':'1234567890'})
madhav.update({'email':'madhav@gmail.com'})
print(madhav)
#remove all key value pair
madhav.clear()
print(madhav)