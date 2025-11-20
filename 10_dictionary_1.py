# example of dictionary
teacher = {'name':"ankit","age":40,"weight":80.20,"gender":True,"secret":123123}
print(teacher) 
print(teacher['weight']) # 80.20
print(teacher['age']) # 40
print(teacher['gender']) # True
# print(teacher['email']) #  key error because key not exists
#add new key value 
teacher['city'] = "Bhavnagar"
teacher['pincode'] = 364001
#update
teacher['name'] = "Ankit Patel"
del teacher['secret'] #delete key value pair secret
print(teacher)