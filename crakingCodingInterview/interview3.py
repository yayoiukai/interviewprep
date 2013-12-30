#3.1 

#describe how you could use a single array to implement three stacks.
#use modulous and offset. So 0, 3, 6, 9 will be stack no.1
#1, 4, 7, 10, 13, will be stack no.2
#2, 5, 8, 11, 14  will be stack no.3

#3.2 
# add min function.
# push is append. pop is pop.
# so in order to return min O(1), it is necessary to keep 
# track of min number

class Stack():
	def __init__(self):
		self.mm = None 
		self.a=[]

	def length(self):
		return len(self.a)

	def push(self, item):
		if self.mm == None or item < self.mm:
			self.mm = item
		self.a.append(item)

	def pop(self):
		item = self.a.pop()
		if item == self.mm:
			self.mm = min(self.a)
		return item

    def peek(self):
    	item = self.a.pop()
    	self.a.append(item)
    	return item 

	def minitem(self):
		return self.mm

#3.3 

class SetOfStack():
    def __init__(self):
        self.a = [] 
        self.limit = 3
        self.height = 0
        self.lists = []
        self.index = 0 
        self.lists.append(self.a)

    def push(self,item):
        if self.height < self.limit: 
    	    self.a.append(item)
    	    self.height += 1
        else:
            self.height = 0 
            self.index += 1 
            self.a = []
            self.a.append(item)
            self.lists.append(self.a)


    def pop(self):
        return self.a.pop()

    def popAt(self, num):
        temp=self.lists[num]
        return temp.pop()


#3.4

class Tower(object):
	def __init__(self,num):
	self.disks=Stack()
	self.id = num

	def id(self):
		return self.id

	def add(self, item):
        if disks.length() == 0 and disks.peek() < item:
            print "error this should not happen"
        else:
            disks.push(item)

	def moveTopTo(self, t):
        top = self.disks.pop()
        t.add(top)

    def moveDisks(self, num, destination, buf):
    	if num > 0:
    		self.disks.moveDisks(n-1, buf, destination)
    		moveTopTo(destination)
    		buf.moveDisks(n-1,destination,self.disks)


        




def towerofhanoi():
	
	return result 



















	def min(self):
		return 





