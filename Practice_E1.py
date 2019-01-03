x=int(input("Insert 1 if you wish to proceede with the purchase: "))
cantA=0
cantB=0
cantC=0
cantD=0
while x==1:
	a=int(input("Please insert the amount of product A items you wish to purchase"))
	b=int(input("Please insert the amount of product B items you wish to purchase"))
	c=int(input("Please insert the amount of product C items you wish to purchase"))
	d=int(input("Please insert the amount of product D items you wish to purchase"))
	cantA=cantA + a
	cantB=cantB + b
	cantC=cantC + c
	cantD=cantD + d
	z=int(input("To display the cost of your purchase insert 1, or any other number to disregard"))
	while z==1:
		t=int(input("If you want to know the cost per product insert 1, to display only the total amount press any 2"))
		if t==1:
			print("The total cost of product A is: ", 750*(1-0.75)*cantA, " .The total cost of product B: ", 1500*(1-0.25)*cantB, " .The total cost of product C: ",cantC*500, " .The total cost of product D: ", 250*cantD, " .Total of purchase: $",  750*(1-0.75)*cantA + 1500*(1-0.25)*cantB + cantC*500 + cantD*250)
		else:
			if t==2:
				print("Total of purchase: $",  750*(1-0.75)*cantA + 1500*(1-0.25)*cantB + cantC*500 + cantD*250)
			else:
				z=int(input("Incorrect value. Press 1 to try again"))
		z=int(input("if you want to review the cost press 1, if not press any other number"))
	x=int(input("To continue shopping insert 1, if not insert any other number"))	
print("Thank you for shopping with us")