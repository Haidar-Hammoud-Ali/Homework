salary= float(input ("Please enter your month salary: "))
month=  input ("Provide the name of This month: ")
saving_percentage= float(input ("Enter the percentage for saving: "))
rent_percentage=float(input("Enter the percentage for rent: "))
electricity_percentage=float(input("Enter the percentage for electricity: "))

saving=(saving_percentage/100)* salary
rent =(rent_percentage/100)*salary
electricity= (electricity_percentage/100)*salary

total_expense = saving+ rent+ electricity
remainder= salary- total_expense

rent_year= rent * 12
electricity_year= electricity*12

salary_power_2= salary **2
