'''booleans: True False
= is an assignment operator, assigning variables
== is an equality operator
!= not equal operator'''

#assignment =
boolean = True
print(boolean)

#comparison ==
print(90==120)
print(100==100)

#not equal !=
print(90!=100)
print(90!=90)

#greater > and smaller than <
print(90>100)
print(90<100)

#greater or equal >= and smaller or equal than <=
print(90>=90)
print(90<=90)
'''
#if
n=int(input('Please write a number: '))
if n>=10:
	print('the number you entered is greater or equal than 10')
else:
	print('the number you entered is lower than 10')


#elif statement: else if
m=int(input('Please write a number: '))
if m==10:
	print('Number entered equals 10')
elif m>10:
	print('Number entered is greater than 10')
elif m<10 and m>0:
	print('Number entered is lower than 10 and greater than 0')
else:
	print('Number is lower than 0')

#not: inverts an argument
print(not 100>1000) #false, inverted to true
	
                       
if not True:
   print("1")
elif not (1 + 1 == 2):
   print("2")
else:
   print("3")
'''
#while

print('while begins')
i=1
while i<=12:
	print(i)
	i=i+1

#infinite loop
#while 1==1:
	#print('infinite')

#breaking a loop:

i=0
while i<10:
	print(i)
	i=i+2
	if i==8:
		break

#continue: skipps but continues
i=0
while i<10:
	i=i+1
	if i==2:
		#print('skipping 2')
		continue
	print(i)
	'''if i==5:
		print('breaking')
		break
	print(i)'''

#lists
l=[]
print(l)

string='Hi everyone'
print(string[0])

listA=[0,1,2,3,4,5,'six']
print(listA)

listA[0]='zero'
print(listA)

listB=listA + [7,8,9]
print(listB)

#in or not in: True or False results
print('zero' in listB)
print(9 in listB)

print(10 not in listB)

#operations with lists
listC= [-3,-2,-1] + listB
print(listC)

#append
listC.append(10)
print(listC)

#length
print(len(listC))

if len(listC)>len(listA):
	print('ListC is longer than ListA')

#insert in any place, append only inserts at the end
words=['oranges', 'fruits']
words.insert(1,'are')
print(words)

'''#insert one by one only
words.insert(3,'and'; 4,'are'; 5,'yummy') #doesn't work
print(words)'''

#index (position of word)
print(words.index('oranges'))

#how many times an object appears in the list
print(listC.count(-4))

#remove object from list:
listC.remove(4)
print(listC)

words.remove('oranges')
print(words)

print(words.reverse())

#range
numbers=list(range(10))
print(numbers)

#from 2 to 12
rangelist=list(range(2,12))
print(rangelist)

#from 10 to 100 every 10
rangeinter=list(range(10,100,10))
print(rangeinter)

#for loops
fruits=['bananas', 'oranges', 'grapes', 'tangerines', 'pears', 'apples', 'nectarines']
for i in fruits:
	print(i + '!')

for i in range(5):
	print ('Hello!!!')

#while True:
#	print('infinite')

#while False:
	print('Not infinite')

#defining functions
def addingfunction(x,y):
	sum=x+y
	return sum
	print('this won\'t be printed since is after the return')
print(addingfunction(9,0))


from math import pi,sqrt 
print(sqrt(12233))

def func(x):
  res = 0
  for i in range(x):
     res += i
  return res

print(func(4))


