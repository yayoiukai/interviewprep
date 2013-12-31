## implement insertion sort in python

st = "1 9 7 3 8 6 2 5"

def bubble(st):
  nums = st.split(' ')
  print nums
  num = 0
  original = []
  length = len(nums)
  for i in nums:
  	original.append(int(i))

  switched = False 

  while switched != True: 
    for i in range(length):
      if i + 1 < length and original[i+1] < original[i]:
        temp = original[i]
        original[i] = original[i+1]
        original[i+1] = temp 
        switched = True
    if switched == True:
        switched = False
    else: 
       switched = True 

    
  

  	

  print original

bubble("1 7 6 4 0 8 2 3")
bubble(st)





