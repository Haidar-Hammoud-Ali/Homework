salary= float(input ("Please enter your month salary: "))
month=  input ("Provide the name of This month: ")
saving_percentage= float(input ("Enter the percentage for saving: "))
rent_percentage=float(input("Enter the percentage for rent: "))
electricity_percentage=float(input("Enter the percentage for electricity: "))

saving=(saving_percentage/100)* salary
rent =(rent_percentage/100)*salary
electricity= (electricity_percentage/100)*salary

print(salary, saving, rent, electricity)

total_expense = saving+ rent+ electricity

print (total_expense)