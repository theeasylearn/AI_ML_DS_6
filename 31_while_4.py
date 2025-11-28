#write a program to generate sum of all digits in given number 
# input = amount : 12345 process : 1+2+3+4+5 output : 15
sum = 0
num = int(input("Enter number")) # 12345

while num > 0:
    reminder = num % 10 #5
    sum = sum + reminder #5
    num = num // 10 #1234

print(sum)
