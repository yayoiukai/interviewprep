import insertion

## implement shell sort in python

st = "1 11 9 7 3 8 6 2 5 10 4"

def shell(st):
  nums = st.split(' ')
  #print nums
  num = 0
  original = []
  step =[7,3,1]
  mul = 0 
  sublist = []

  mulp = 0 


  length=len(nums)
  for i in nums:
  	original.append(int(i))

  #print original

  ## first go through 7, and 3 and 1. 
  for s in step: 
    for i in range(length):
      mul = 0
      #print "i is", i
      position = i + s * mul
      sublist =[]
      while position < length:
        #print "position is", position
        sublist.append(str(original[position]))
        mul += 1
        position = i + s * mul

      
      if len(sublist) < 2:
          sublist=[]
          break
      else: 
        #print "sublist", sublist
        al=' '.join(sublist)
        #print "before insertion is", al
        sublist=insertion.insertion(al)
        al = ''
        #Sprint "sublist after i is", sublist
        mul=0
        position = i + s * mul
        while position < length and mul < len(sublist):
          original[position] = sublist[mul]
          mul += 1
          position = i + s * mul
        #print "after it is", original

      mulp += 1
      sublist=[]
      




  print original

shell("1 7 6 4 0 8 2 3")
shell(st)





