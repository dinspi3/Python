calculation_to_hours=50
name_of_unit="hours"

def days_to_units(num_of_days):
 if num_of_days > 0:
    return (f"{num_of_days} days are {num_of_days*calculation_to_hours} {name_of_unit}")
   # print(custom_message)

user_input = input("Enter numbers of day : ")
user_input_number = int(user_input)

calculated_value = days_to_units(user_input_number)
print(calculated_value)

#my_var = days_to_units(18.3987772,"Awesome !")

#10print (my_var)

