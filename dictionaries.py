d={'key1':[1,2,3],
   'key2':True,
   'Key3':5,
   4:False
}
print (d)
print (d['key2'])
print (d[4])

#dictionaries, you can modify the value on a keyword at any moment; but once the keyword is declared, I can't modify the 'keyword'

d[4]=True
print (d[4])

#you could also change the type of value the keyword had:
d[4]="hello"
print (d[4])


#Arrays and tuples are sequential lists, but the dictionaries are not sequential; so we can't do "slicing", because tey don't have indexes