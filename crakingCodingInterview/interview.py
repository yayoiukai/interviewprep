
#interview.py
#1.1
def uniquenonset(st):
	index=0
	for c in st:
		print "c is %s and index is %s" % (c,index)
		if index==0:
			if(st.find(c,index+1,len(st))!=-1):
				return False
		elif(st.find(c,0,index)!=-1 or st.find(c,index+1,len(st))!=-1):
			return False
		index+=1
	return True
#Above takes O(n^2) times and use set to reduce it once 

#1.1- more efficient solution 
def unique(st):
	letters=set()
	for c in st:
		if c in letters:
			return False
		else:
			letters.add(c)
	return True


#1.2 
def reverse(st):
	index=len(st)-1
	rst=''
	while index>=0:
		rst=rst+st[index]
		index-=1
	return rst

#1.3 
def permutationold(st1,st2):
	if st1 == st2:
		return True
	if len(st1) != len(st2):
		return False
	for c in st1:
		index=st2.find(c,0,len(st2))
		if index==-1:
			return False
		else:
			st2=st2[0:index]+st2[index+1:len(st2)]
	return True

def permutation(st1,st2):
	letters1=[]
	letters2=[]
	for c in st1:
		letters1.append(c)
	for d in st2:
		letters2.append(d)
	if sorted(letters1) == sorted(letters2):
		return True
	else:
		return False



#1.4 
def replacespace(st):
	index=0
	for c in st:
		if c==' ':
			st=st[0:index]+'%20'+st[index+1:len(st)]
			index+=2
		index+=1
	return st

#this may not not be correct


#1.5
def compress(st):
	index=1
	newst=''
	i=0
	while i<len(st) and index < len(st):
		c=st[i]
		while index < len(st) and c==st[index]:
			index+=1
		newst=newst+c+str(index-i)
		i=index
		index+=1
	if len(st)<len(newst):
		return st
	else:
		return newst



#1.6
def rotate90(matrix):
	n=len(matrix)
	for layer in range(0,n/2):
		first = layer
		last = n - 1 - layer
		for i in range(first,last):
		    int offset = i - first
		    #save top 
		    int top = matrix[first][i]
		    # left to top 
		    matrix[first][i] = matrix[last - offset][first]
		    # bottom to left 
            matrix[last-offset][first] = matrix[last][last - offset]
            # right to bottom 
            matrix[last][last - offset] = matrix[i][last]
            # top to right
            matrix[i][last] = top


    return matrix 


#1.7 

def setzeros(matrix):
	row= []
	column = []
	for i in range(0,n):
		row[i] = False
		colum[i] = False

	n=len(matrix)
    for i in range(0,n):
    	for j in range(0,n):
    		if matrix[i][j] == 0
    		  row[i] = True
    		  column[j] = True
    
    for i in range(0,n):
    	for j in range(0,n):
    		if row[i] or column[j]:
    		  matrix[i][j] = 0 

    return matrix



#1.8 
def isSubstring(st1,st2):
	if st1.find(st2)!=-1 or st2.find(st1)!=-1:
		return True
	else:
		return False

def rotation(st1,st2):
	newst1=st1+st1
	if isSubstring(newst1,st2):
		return True
	else:
		return False















