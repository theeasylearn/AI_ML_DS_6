# using for loop with string
# count no of letters, words, vowels 
# task
# count symbols and digits
line = "QuIck zebra jumps over lazy 3 dogs at DelhI park around 12:30 pm near cage no 5 @ vIsItor day"
count = 0
word = 1
vowels = 0
list = ['a','e','i','o','u','A','E','I','O','U']
for letter in line:
    count+=1
    if letter==' ':
        word+=1
    elif letter in list:
        vowels+=1
print()
print("no of letters ",count)
print("no of words ",word)
print("no of vowels ",vowels)