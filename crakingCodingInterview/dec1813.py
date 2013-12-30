### Google Hangout Session with Natalie Han. Some of the earlier code came from
### previous week's women who code white board interview practice session 


#Q1: Finding anagrams for word in arrays
## women who code: build a hash for all the words, then return one key vale
def anagrams(word, arrays):
	hash = {}
	for w in arrays:
		sortedWord = ''.join(sorted(w))
		if sortedWord in hash:
			hash[sortedWord].append(w)
		else:
			hash[sortedWord] = [w]

	sWordNew = ''.join(sorted(word))
	if sWordNew in hash:
		return hash[sWordNew]
	else:
		return None
## use a set to store only the anagram
def anagram1(word, arrays):
	myset = set()
	truth = ''.join(sorted(word))
	for w in arrays:
		if len(w) == len(truth):
			sw = ''.join(sorted(w))
			if sw == truth:
				myset.add(w)

	return myset
		
word = 'bac'
array = ['acb', 'cba', 'efd']

print anagrams(word, array)
print anagram1(word, array)









#Question3: Check if a set of input str of ((())))) are matched 
#eg. this is correct: ()();  this is not correct: )())((, )))))(((((
#      this is not correct ()) 
#     this is not correct ((((())))))))))
#     this is correct ((()))(((()))); (()())

#this is not quite right 
def checkMatched(st):
    openp = 0
    closep = 0 
    for i in range(0,len(st)):
        if st[i] == '(':
            openp += 1 
        if st[i] == ')' :
            while st[i] == ')':
                closep +=1 
                i +=1 

    if openp == closep:
        openp = 0
        closep =0
    else:
        return False 
    return True

class Stack():
    def __init__(self):
        self.st = [] 

    def push(self,item):
        self.st.append(item)

    def pop(self):
        return self.st.pop()


    def isEmpty(self):
        if len(self.st) == 0:
            return True
        else:
            return False 


#correct version 


def checkPara(st):
  s = Stack()
  bal = True
  for ch in st:
     if ch == '(':
        s.push(ch) 
     else:
        if s.isEmpty():
             bal = False
        else:
           s.pop()

  if bal and s.isEmpty():
     return True
  else:
     return False

#Test CheckPara

print "CheckPara Test"
print "This should be true", checkPara('((()))')

print "this should not be True", checkPara('())') 
print "this should be False", checkPara('((((())))))))))')
print "This should be True", checkPara('((()))(((())))')
print "This should be True", checkPara('(()())')

print "This should be True",checkPara('((()))')    
     
# Question4: implement Queue using two stacks


class MyQueue(object):
    def __init__(self):
        self.stack1=Stack()
        self.stack2=Stack()
    def enqueue(self,item):
        self.stack1.push(item)

    def dequeue(self):
        if not self.stack2.isEmpty():
            item = self.stack2.pop()
            return item
        else:
        # reverse stack1 to stack2
            item = None
            if not self.stack1.isEmpty():
                while not self.stack1.isEmpty():
                    item = self.stack1.pop()
                    self.stack2.push(item) 
                item = self.stack2.pop() 
            return item

    def isEmpty(self):
        if self.stack1.isEmpty() and self.stack2.isEmpty():
            return True
        else:
            return False


print "queue Test" 
q = MyQueue()
q.enqueue(1) # s1: 1; s2: None
q.enqueue(2)          # s1: 1, 2; s2: None   
print "it should print 1,", q.dequeue() # return 1; s1: None, s2: 2

q.enqueue(3)         # s1: 3; s2: 2
print "it should print 2,", q.dequeue() # return 2, check s2 first. 
print "it should print 3,", q.dequeue()# return 3, put s1 reverse to s2. 

                   


	
     

#Question: remove duplicates from unsorted linked list

class Node():
    def __init__(self):
        self.data = None
        self.next = None
       

class LinkedList():
    def __init__(self):
        self.head = Node()

    def addInFront(self,item):
        temp = Node()
        temp.data = item
        temp.next = self.head
        self.head = temp
        

    def addInBack(self,item):
        if self.head.data == None:
            self.head.data =item
        else:
            temp = Node()
            temp.data =item
            previous = self.head
            current = self.head.next
            while current != None:
                previous = current
                current = current.next
            previous.next = temp

    def printList(self):
      ll=[]
      temp = self.head
      while temp != None:
          ll.append(temp.data)
          temp = temp.next
      print ll

print "create linked list and test remove dublicate"
llst = LinkedList()
llst.addInFront(1)
llst.addInFront(2)
llst.addInFront(1)
llst.addInFront(3)
llst.addInFront(4)
llst.addInFront(5)

print "list is"
temp = llst.head
while temp.data != None:
  print temp.data
  temp = temp.next 




def removedup(ll):
    a = set()
    start = ll.head 
    previous = ll.head
    current = previous.next 
    a.add(previous.data) 

    while current.data != None:
        if current.data in a:  #this is duplicate 
            #then update the current 
            current =current.next 
            previous.next = current
        else:
            a.add(current.data)
            previous = current
            current = current.next

    return start

print " after remove dublicate, list is"
temp = removedup(llst)
while temp != None:
  print temp.data
  temp = temp.next 







class TreeNode():
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None 

print "first I need to build a tree. "

#Question2: Build a minimum height binary tree with a sorted array

print "list is l=[1,3,4,5,6,7,8,9,10]"

l=[1,3,4,5,6,7,8,9,10]

def makeBT(l):
  queue = MyQueue()
  root = TreeNode()
  queue.enqueue(root)
  while l:
    node = queue.dequeue()
    node.value = l.pop()
    node.Right = TreeNode()
    node.Left = TreeNode()
    queue.enqueue(node.Right)
    queue.enrueue(node.Left)

  return root


def makeTree(ll):
  length = len(ll)
  root = TreeNode()
  if length == 0:
      return None
  elif length == 1:
      root.data = ll[0]
  elif length == 2:
      root.data = ll[0]
      root.left = TreeNode()
      root.left.data = ll[1]
  elif length == 3:
      root.right = TreeNode()
      root.right.data = ll[0]
      root.data = ll[1]
      root.left = TreeNode()
      root.left.data = ll[2]
  else:
      center = length/2
      root.data = ll[center]
      root.right = makeTree(ll[0:center])
      root.left  = makeTree(ll[center+1:length])
  return root



#Questions: Find Common Ancestor of two nodes in a Binary tree

rt = makeTree(l)

def isParent(root, leaf):
    if root == None:
        return False
    elif root.data == leaf:
        return True
    elif isParent(root.left, leaf) or isParent(root.right, leaf):
        return True 
    else:
        return False 

def parentHelper(p, leaf1, leaf2):
    print "Helloworld!!"
    q = MyQueue() 
    temp = p.dequeue()
    print "temp is", temp.data
    node = TreeNode()
    while temp != None:
        if isParent(temp, leaf1) and isParent(temp, leaf2):
            node = temp
            if temp.left != None:
                q.enqueue(temp.left)
            if temp.right != None:
                q.enqueue(temp.right) 
            node = parentHelper(q, leaf1, leaf2)
            if node == None:
                node = temp
        else:
            node = None
        temp = p.dequeue()
    print node
    return node

def findParent(root, leaf1, leaf2):
   p=MyQueue()
   node = TreeNode()
   #first check both leaves exists in tree
   if isParent(root, leaf1) and isParent(root, leaf2):
        p.enqueue(root.left)
        p.enqueue(root.right)
        node = parentHelper(p,leaf1,leaf2)
   else:
       print "One of leaf does not exists" #no common ancenstor

   if node == None:
       node = root 
   return node.data 


rt = makeTree(l)

print "find parent. It should be False", findParent(rt, 1, 2)
print "find parent. it should be 1", findParent(rt, 1, 3)
ans = findParent(rt,1,10)
print "find parent. It should be", rt.data, ans


     






#Question: Given a binary tree, create a linked list for node in each level

#linked list = a
#linked list = b->b

def createLinkedList(bt):
    q1= MyQueue()
    q2= MyQueue()
    q1.enqueue(bt)
    ll = LinkedList()
    res =helper(ll,q1, q2)
    return res

   
def helper(ll,q1, q2):
    llist = ll 
    while not q1.isEmpty():
        tmp = q1.dequeue()
        temp = Node()
        temp.data = tmp.data
        llist.addInBack(tmp.data)
        print "llist is",llist.printList()  
        if tmp.left != None:
            print "temp left", tmp.left.data
            q2.enqueue(tmp.left)
        if tmp.right != None:
            print "temp right", tmp.right.data
            q2.enqueue(tmp.right)
    q1=MyQueue() 
    print "q1 is empty?",q1.isEmpty()
    # creating linked list of linked list 
    if not q2.isEmpty():
        llist = helper(llist,q2, q1)
        return llist
    else :
        return llist
  
   

lll=createLinkedList(rt)

print lll.printList()
        
     
	

    