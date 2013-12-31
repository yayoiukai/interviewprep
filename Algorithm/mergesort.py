## implement insertion sort in python

st = "1 9 7 3 8 6 2 5"

def mergesort(st):
  nums = st.split(' ')
  #print nums
  num = 0
  original = []
  result = []
  length=len(nums)
  for i in nums:
  	original.append(int(i))
  print original
  result = divide(original)
  print "result is ", result

def divide(st):
	result = []
	if len(st) > 2:
		length = len(st)
		first = length/2
		st1 = st[0:first]
		st2 = st[first:length]
		#print st1
		#print "before", st2
		result = merge (divide(st1), divide(st2))
		#print "result is", result
		return result
	elif len(st) == 1:
		return st
	else:
		if st[0] > st[1]:
			st.reverse()
			#print "after reverse", st
			return st
		else :
			return st 


def merge(st1, st2):
	#print "merge ", st1
	#print "merge ", st2
	for s in st1:
	  #print s
	  for i in range(len(st2)):
	    if s < st2[i]:
		  st2.insert(i,s)
		  break
	  else:
		 st2.append(s)
	#print "after merge", st2
	return st2


mergesort("1 7 6 4 0 8 2 3")
mergesort(st)







