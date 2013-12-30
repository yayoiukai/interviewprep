class Node:
	def __init__(self):
		self.data=None
		self.next=None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, newdata):
		self.data = newdata

	def setNext(self, newnext):
		self.next = newnext

class linked_list:
	def __init__(self):
		self.head=None

	def isEmpty(self):
		return self.head == None 

	def add(self,item):
		temp=Node() #create a new node
		temp.setData(item)
		temp.setNext(self.head) #link to the new node to previous node
		self.head=temp # set the current node to the new one

	def size(self):
		current = self.head
		count = 0
		while current != None:
			count = count + 1
			current = current.getNext()

		return count

	def search(self,item):
		current = self.head
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()

		return found

	def remove(self,item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()

		if previous == None:
			self.head = current.getNext()
		else:
		    previous.setNext(current.getNext())


	def list_print(self):
		node=self.head
		while node != None:
			print node.data
			node=node.getNext()


#2.1 
def removedup(ll):
	ll.list_print()
	node=ll.head
	previous=None
	nodelist=Set()
	while node:
		if node.data in nodelist:
			previous.setNext(node.getNext())
		else:
			nodelist.add(node.getData())
			previous=node
		node=node.getNext()
	ll.list_print()
	return ll

#2.2 
def findkthlast(ll,k):
	node=ll.head
	i=1
	while node:
		node=node.getNext()
		i+=1
	position=i-k+1
	i=1
	node=ll.head
	while i<position-1:
		node=node.getNext()
		i+=1
	return node

#2.3
def deletemiddle(m):
	if m.getNext()!=None and m.getData() !=None:
		node=m.getNext()
		m.setData(node.getData())
		m.setNext(node.getNext())

#2.4 
def partition(ll,x):
    node=ll.head
    less=liked_list()
    more=linked_list()
    more.add(x)
    for i in range(ll.size()): 
        if node.getData() < x:
            less.add_node(node.getData())
        else:
            more.add_node(node.getData())

        node = node.getNext()



#2.5

def addtwo(ll1, ll2):
    sumvalue = 0 
    node1 = ll1.head
    node2 = ll2.head
    ans = linked_list()
    carry = 0 
    while node1 != None and node2 != None:
        sumvalue = node1.data + node2.data + carry 
        if sumvalue < 10:
            ans.add_node(sumvalue)
            carry = 0 
        else:
            ans.add_node(sumvalue%10)
            carry = 1
        node1 = node1.getNext()
        node2 = node2.getNext()
		

    if node1 == None and node2 != None:
        while node2 != None:
            sumvalue = node2.data + carry
            if sumvalue < 10:
                ans.add_node(sumvalue)
                carry = 0 
            else:
                ans.add_node(sumvalue%10)
                carry = 1 
            node2 = node2.getNext()


    elif node1.getData() != None and node2.getData() == None:
        while node1.getData() != None:
            sumvalue = node2.getData() + carry
            if sumvalue < 10:
                ans.add(sumvalue)
                carry = 0 
            else:
                ans.add(sumvalue%10)
                carry = 1
            node1 = node1.getNext()
    return ans




#2.6
# assume that all values are unique 

def circularstart(ll):
    start = ll.head  # start of the linked list 
    node1 = ll.head
    node2 = ll.head
    circ = linked_list() 
	

	# first find out the circular links 
    while node1 != None:
        if node1.data == node2.data:
            break
        else:
            node1 = node1.getNext()
            node2 = node2.getNext()

    #Add all the node values in the circular links 
    circ.add(node1.getData())
    temp = node1
    node1 = node1.getNext()
    while node1.data != temp.data:
    	circ.add(node1.data)
    	node1 = node1.next 

    #now check from the begining 
    node1 = temp 
    node2 = node1 
    
    # start data is increment one by one and check against all the data 
    # until it finds the equals 

    while start.data != node1.data:
        node2=node1
        while start.data != node2.data:
            node2 = node2.getNext()
        if start.data == node2.data: 
            break 
        else:
            start = start.getNext()
    
    return start.getData()

print "test cirularstart"

ll=linked_list()
ll.add(1)

ll.add(2)
temp=ll.head
ll.add(3)
ll.add(temp.getData())


#ll.list_print()
print "first attempt should be 1", circularstart(ll)

ll.remove(1)
ll.remove(2)
ll.add(4)
ll.add(5)
ll.add(3)


print "second attempt should be true", palindrome(ll)



def palindrome(ll):
    current = ll.head
    last = ll.head
    length = ll.size()
    #print "length is", length
    for j in range(0,ll.size()/2):
        for i in range(0,length):
            if i == length-1:
                if current.getData() == last.getData():
                    #print "sugoi"
                    pass
                else:
                    #print "hello"
                    return False 
            else:
            	#print "here is i ", i , "and j", j
                last = last.getNext()

        length -= 1
        current = current.getNext()
        last = ll.head
    #print "hihi"
    return True  


print "test palindrome"

ll=linked_list()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
ll.add(5)
#ll.list_print()
print "first attempt should be false", palindrome(ll)

ll.add(4)
ll.add(3)
ll.add(2)
ll.add(1)

print "second attempt should be true", palindrome(ll)








    








ll=linked_list()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
ll.add(5)
ll.list_print()

node=Node()
node=findkthlast(ll,3)
print node.getData()

