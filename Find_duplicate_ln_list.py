numbers = [1 ,1 ,2 ,3 ,4, 4,9 , 10]
unique = []
for number in numbers :
    if number not in unique:
        unique.append(number)
        print (unique)
