#we need input from user
# Total rent
#total food orderd for snacking
#elecricity units spend
#charge per units
#Persons living in room /flat


#output
#total amount you habe to pay is

rent =int(input("Enter your hostel/flat rent = "))
food =int(input("Enter the amount of food ordered = "))
elecricity_spend = int(input("Enter the total of elecricityspend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons =int(input("enter the number of persons living in room/flat= "))

total_bill = elecricity_spend * charge_per_unit
output =(food+rent+total_bill)//persons


print("Each person will pay =",output,"/=")