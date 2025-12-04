'''
1	0	1	0	1
1	0	1	0	
1	0	1		
1	0			
1				
'''
row = 5
while row>=1:
    column = 1
    while column<=row:
        print(column%2,end=' ')
        column+=1
    print() #new line
    row-=1
