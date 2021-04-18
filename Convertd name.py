
lname = input ("Enter you Last name :")
fname = input ("Enter you First name :")
stringlname= len(lname)
stringfname= len(fname)
slicedString= lname [stringlname::-1]
slicedString1= fname [stringfname::-1]
print ('You first and last name is converted to : ')

print (slicedString,slicedString1)
