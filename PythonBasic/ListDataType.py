lst1 = [20,30,10,60,45]
lst2 = list((12,43,67,89))
print(lst1)
print(lst2)

# list with eliment


lst3 = ['Kamal',45,'ruchika',False,77]
print(lst3[0],',',lst3[1],',',lst3[2],',',lst3[3])

print(lst3[0:3])


# add the data into the list


mylist = ['Kamal',45,'ruchika',False,77]
mylist.append("Ruchika")   #add the value in the behind the list
mylist.extend(["hi","bye"])  #add the more value behind the list
mylist.insert(0,"welcome")   #add the value to the index number.
mylist.pop(0) #remove the vlue from what we give as a index
mylist.remove(45) #remove the vlue from what we give as a value

print(mylist)