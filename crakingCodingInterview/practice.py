
ll=[[5, 12],  [17, 19],  [45, 50]]

def rangenumber(ll):
    numbers=[]
    for l in ll:
        numbers.append(l[0])
        numbers.append(l[1])
    return numbers

numberlist = rangenumber(ll)

def findnumber(num, numberlist,n):
    length = len(numberlist)
    center = length/2
    if num in numberlist:
        return True 
    elif num == numberlist[center]:
        return True
    elif length == 3: 
        if  n == 1 and ( num < numberlist[0] or numberlist[1] < num < numberlist[2]):
           return True
        elif n== 0 and (numberlist[0] < num < numberlist[1] or num > numberlist[2]):
            return True
        else:
            return False 
    elif length == 2:
           if num > numberlist[1]:
                return False
           else: 
                return True 
    elif num <  numberlist[center]:
        return findnumber(num, numberlist[0:center],0)
    else: 
        return findnumber(num, numberlist[center:length],1)


print "test by 16, should return false", findnumber(16,numberlist,0)
print "test by 20, should return false", findnumber(20,numberlist,0)
print "test by 17, should return True", findnumber(17, numberlist,0)
