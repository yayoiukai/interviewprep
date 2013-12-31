## implement insertion sort in python

st = "1 9 7 3 8 6 2 5"

def insertion(st):
  nums = st.split(' ')
  #print nums
  num = 0
  original = []
  result = []
  length=len(nums)
  for i in nums:
  	original.append(int(i))

  result.append(original[0])

  added = False

  # go throught the list one by one. 
  for i in range(1,len(original)):
  	place = original[i]

   	j = len(result)-1
  	while place < result[j] and j >= 0:
  		j-=1

  	result.insert(j+1,place)

  	

  #print result
  return result

insertion("1 7 6 4 0 8 2 3")
insertion(st)





