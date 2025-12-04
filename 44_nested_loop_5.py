'''
				*
			  *	  *
		   *	*	*
	     *	 *	 * 	  *
      *	  *   *    *	*
'''
row = 5
counter = 1
while row>=1: #outer while loop 
    column = 1
    while column<=row: #inner loop 1
        print('',end=' ')
        column+=1
    astrik = 1
    while astrik<=counter:
        print('* ',end='')
        astrik+=1
    print() #new line
    row-=1
    counter+=1
