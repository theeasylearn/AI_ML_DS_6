#Write a program that takes a 5 subject marks from student. findout whether student is passed or failed in. if user has above 39 marks in all subject, he is passed otherwise failed.
marks = [0,0,0,0,0]

marks[0] = int(input("Enter marks for 1st subject"))
marks[1] = int(input("Enter marks for 2nd subject"))
marks[2] = int(input("Enter marks for 3rd subject"))
marks[3] = int(input("Enter marks for 4th subject"))
marks[4] = int(input("Enter marks for 5th subject"))

if marks[0]>39 and marks[1]>39 and marks[2]>39 and marks[3]>39 and marks[4]>39:
    print("Student is passed in exam")
else:
    print("Student is failed in exam")
