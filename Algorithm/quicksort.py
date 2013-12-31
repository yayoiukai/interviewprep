## implement insertion sort in python

st = "1 9 7 3 8 6 2 5"

def quicksort(st):
  nums = st.split(' ')
  #print nums
  num = 0
  original = []
  result = []
  length = len(nums)
  for i in nums:
  	original.append(int(i))
  print original
  result = divide(original)
  print "result is ", result

def divide(st):
	result = []
	if len(st) < 2 : 
	  return st
	else:
	  pivot = st[0]
	  st1 = []
	  st2 = [] 

	  for i in range(1,len(st)):
	    if st[i] < pivot :
		  st1.append(st[i])
	    else:
		  st2.append(st[i])

	  st1.append(pivot)
	  result = divide(st1) + divide(st2)
	  return result

quicksort("1 7 6 4 0 8 2 3")
quicksort(st)







