print('This programm is to calculate the age of a person\n')
opt=str(input('Do you want to check an age? Write \'S\' for Yes or any other for No: '))
if opt== 'S' or opt == 's':
	while opt== 'S' or opt == 's':
		try:
			age=int(input('Write your age: '))
			if age <10:
				print ('You haven\'t been born yet')
			elif age>=0 and age <18:
				print ('You are a teenager')
			elif age >=18 and age<27:
				print('You are a teenager')
			elif age >=27 and age <58:
				print('you are an adult')
			else:
				print('You are elderly old')
			opt= input('You did not write a \'S\'. Try again')
		except:		
			print('That isn\'t a number')
			opt= input('You did not write a \'S\'. Try again')
else:
	opt=input('You did not write a \'S\'. Try again')