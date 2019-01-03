l=[2,"tres",True,["uno",10],5,'hi']
print (l)

#using the array index
l2= l[1]

print (l2)

print (str(l[0]))
print (str(l[3]))

#accessing Array's index that are in an Array list: [IndexInArray][indexinlist]
l3=l[3][0]

print(l3)
print(str(l[3][1]))

#modifying inner array's data with the index:
l=[2,"tres",True,["uno,10"],5,'hi']
print(l)
l[1]=4
l2=l[1]
print (l2)

#slicing: copy some information from an Array towards another one [begginingindex:quantityofcpyingelements]:

l3=l[0:3]

print(l3)

#copy some information fron an array towards another one by skipping some information [beginningindex:quantityofcopyingelements:amountofskipsperindex]
l4=l[0:3:2]
print(l4)

#copy some information from an array towards another one by skipping each we want [beginningindex:amountofskipsperindex]
l5=[2,"tres",True,["uno",10],6]
l6=l5[0::2]
print('Imprimir Lista 5: ' + str(l5))
print('Imprimir la informacion con datos consecutivos: ' + str(l6))




#Lists / Arrays / Vectors
#Declare the Array list
#Idx 0 , 1   ,  2   ,    3     ,4, 5
l = [2,"tres", True, ["uno",10],5,'Hi']
print ('Imprimir Lista: ' + str(l))
l[1] = 4
l2 = l[1]
print ('Imprimir cambio de dato Indice: ' + str(l2))
#Slicing: copy some information from an Array towards another one [beginningIndex:QuantityofCopyingElements]:
l3 = l[0:3]
l7 = l[1:2]
print ('Imprimir Slicing de Indice 0, 3 Elementos: ' + str(l3))
#Copy some information from an Array towards another one by skipping some information [beginningIndex:Quantity
#ofCopyingElements:AmountOfSkipsPerIndex]
l4 = l[0:3:2]
print ('Imprimir desde indice 0 , 3 elementos, saltando cada 2 elementos: ' + str(l4))
#Copy some information from an Array towards another one by skipping each we want [beginningIndex:Amount
#OfSkipsPerIndex]
l5 = [2,"tres",True,["uno",10],6]
l6 = l5[0::2]
print ('Imprimir Lista 5: ' + str(l5))
print ('Imprimir la informacion saltando los datos consecutivos: ' + str(l6))


print ("new lines")

l5[0:2] = [4,3]
print (l5)

#modify several elements in the array list with just one data [FromIndex:Quantityof Elements]:
l6 = [2,"tres",True,["uno",10],6]
l6[0:2]=[5]
print(l6)

#Get the data form an array with negative index:
l6=[2,"tres",True,["uno",10],6]
l7=l6[-1]
l8=l6[-2]
print(l7)
print(l8)