
x=int(input("Please insert 1 to start: "))
#print (type(x))
while x==1:
	g=int(input("Please insert grade: "))
	if g>100 or g<1 :
		print ('Incorrect value, insert numbers between 1 and 100.')
		x=int(input("Please insert 1 to start: "))
	else:
		if g>89:
			print('Grade: A. Student passes the course')
		else:
			if g>69 and g<90:
				print('Grade: B. Student passes the course')
			else:
				if g>59 and g<70:
					print('Grade: C. Student failed the course')
				else:
					if g>50 and g<60:
						print('Grade: D. Student failed the course')
					else:
						print('Grade: E. Student failed the course')
		x=int(input("Please insert 1 to continue grading: "))	
else:
	print('End')