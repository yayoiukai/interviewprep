# N^2/2 compares


def selection(st):
  
  nums = st.split(' ')
  print nums
  num = 0
  result = []
  length = len(nums)
  for i in nums:
  	result.append(int(i))

  # find min for the entire list and
  #  place it front and they look through the rest of the list. 

  # this is just a big number to start off the list. 
  minlist = max(result)+100
  for i in range(length):

  # find min
    for j in range(i,length):
      if result[j] < minlist:
        minlist = result[j]
        index = j 

    temp = result[i]
    result[i] = minlist
    result[index] = temp
    minlist = max(result)+100

  print result

selection("1 7 6 4 0 8 2 3")

  

