#Use Sublime Text 3, save it as Functions3.py”””
__author__ = 'AnDr3w-JeY' #Set the author of the code
#Defining the Function: (‘somethingMore’ will become a “Dictionary”, so we print accordingly to its Keywords)
def my_function(cad, v=2,**somethingMore):
	print(cad*v)
	print(somethingMore['extraString'])
	print(somethingMore['anotherString'])
#Activation of the Function and assignation of Dictionary’s keyword: (in this case, ‘extraString’ is the KeyWord of the first value of the Dictionary)
my_function('Python ',5, extraString = '\nHello', anotherString = '\nBye')
#Execute in Terminal

