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

print ("The managed finance for ", month, " is as follows:")
print ("The Total Salary is: ", salary, "$")
print ("The Saving Amount is: ",saving, "$")
print ("The Renting Amount is: ", rent, "$")
print ("The Electricity Bills Amount is: ",electricity, "$")
print ("Then, the Total Expense will be: ",total_expense, "$")
print ("The Remainder from your Salary will be: ", remainder, "$")
print ("The Estiamted Yearly Rent is: ", rent_year,"$")
print ("The Estimated Yearly Electricity Bills is: ",electricity_year, "$")
print ("Just for fun!, Your squared salary value is: ", salary_power_2, "$")
