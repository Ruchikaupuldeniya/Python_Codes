temp = 35
if temp > 30:
    print("verry hot")
    
elif temp <20:
    print("its good")
else:
    print("enjoy")
    
    
    #  Ternary Operator
    
    
age = input("Enter your age: ")
age =int(age)
print(type(age))

message = "Eligible" if age > 20 else "Not Eligible"
print(message)




     #Logical Operator

            #and
            
high_income = True
good_credit = True
student = True

if high_income and good_credit:
    print("Eligible")
    
    
        #OR

high_income = True
good_credit = True
student = True

if high_income or good_credit:
    print("Eligible")
    
    
    
    
            #not
            
            
            
high_income = True
good_credit = True
student = True

if not student:
    print("Eligible")
    
else:
    print("Not Eligible")
