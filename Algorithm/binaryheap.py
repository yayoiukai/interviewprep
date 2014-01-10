
#binary heap is perfectly balanced binary tree. So there is no need to
# keep track of the link to parent and child. We just need to calcurate
# where the child or parents it. If I want to find a child, it will be 2k, and 2k+1
# and if I want to find a parent, it will be k/2 

# for example, T, P, R, N, H, O, A, E, I, G is correct binary heap tree. 

# goal insert, del max, max all logN impelementation 


class BinaryHeap:

    def __init__(self):
        self.pq = []

    def exch(self,k,l):
        temp = self.pq[l]
        self.pq[l] = self.pq[k]
        self.pq[k] = temp
        print "exchange position", l , " and ", k
        print "after exchange",self.pq

    def less(self,k,l):
        if self.pq[k] < self.pq[l]:
            return True
        else:
            return False 

    def swim(self,k):
        while k > -1 and self.less(k/2, k):
            self.exch(k, k/2)
            k = k/2
        print "new k is", k, "and list is", self.pq
    
    def sink(self,k):
    	length = len(self.pq)
    	while k < length and length > 1:
    	    if k == 0 and self.less(0,1):
    	        self.exch(k,1)
    	    elif k == 0 and length >2 and self.less(0,2):
    	        self.exch(k,2)
    	    elif 2 * k < length and self.less(k, k * 2):
    	        self.exch(k,2 * k)
            elif 2 * k + 1 < length and self.less(k, k * 2 + 1):
                self.exch(k, 2 * k + 1)
            else:
                k += 1
        print "after sink", self.pq  
   


    def insert(self,x):
        self.pq.append(x)
        N = len(self.pq)-1
        self.swim(N)


    def delMax(self):
        m = self.pq[0]
        self.exch(0,len(self.pq)-1)
        self.pq.pop()
        self.sink(0)
        print "after removed", self.pq
        return m

    def getMax(self):
        num = self.pq[0]
        self.delMax()
        return num 

    def isEmpty(self):
        if len(self.pq) == 0:
            return 0
        else:
            return len(self.pq)


# heap sort testing example
test = ['S','O','R','T','E','X','A','M','P','L','E']
print test

bh = BinaryHeap()

for i in test:
    print i
    bh.insert(i)


testresult = [] 
print "list is ", bh.pq



print "this is", bh.isEmpty()


while bh.isEmpty() > 0:
    a = bh.getMax()
    print "max is ", a
    testresult.append(a)
    

print "the binary heap was", testresult
testresult.reverse()
result = ['A','E','E','L','M','O','P','R','S','T','X']
print "the result should be", result
print "the result is", testresult




#Other lesson.. immutability (from slide 27, cousera, binary heap lesson)
# properties 
# data type - set of values and operations on those values
# immutable data type - can't change the data type once created.

# Advantages 
# simplified debugging
# safer in presence of hostile code
# simplified concurrent programming
# safe to use as key in priority queue or symbol table 


# heap sort is NlogN for the worse case. 
# merge sort is linear for the worst case and extra space
# qucik sort is quadratic in worst case











