# create the initial variables below
age=28
sex=0
bmi=26.2
num_of_children=3
smoker=0

# Add insurance estimate formula below
insurcane_cost=250*age-128*sex+370*bmi+425*num_of_children+24000*smoker-12500
print("This person's insurance cost is "+str(insurcane_cost) +" dollars")
# Age Factor
age=age+4
new_insurance_cost=250*age-128*sex+370*bmi+425*num_of_children+24000*smoker-12500

change_in_insurance_cost=new_insurance_cost-insurcane_cost

print("the change in cost of insurance after increasing the age by 4 years is "+str(
change_in_insurance_cost)+" dollars.")

# BMI Factor

age=28

bmi=bmi+3.1

new_insurance_cost=250*age-128*sex+370*bmi+425*num_of_children+24000*smoker-12500

change_in_insurance_cost=new_insurance_cost-insurcane_cost


print("the change in cost of insurance after increasing the bmi by 3.1 years is "+str(
change_in_insurance_cost)+" dollars.")

# Male vs. Female Factor

bmi=26.2

sex=1
new_insurance_cost=250*age-128*sex+370*bmi+425*num_of_children+24000*smoker-12500

change_in_insurance_cost=new_insurance_cost-insurcane_cost


print("The change in estimated cost for being male instead of female is "+str(
change_in_insurance_cost)+" dollars.")


# num_of_children factor
num_of_children = 6

new_insurance_cost=250*age-128*sex+370*bmi+425*num_of_children+24000*smoker-12500

change_in_insurance_cost=new_insurance_cost-insurcane_cost


print("The change in estimated cost for having 6 kids is  "+str(
change_in_insurance_cost)+" dollars.")

# smoker factor
smoker=1
new_insurance_cost=250*age-128*sex+370*bmi+425*num_of_children+24000*smoker-12500

change_in_insurance_cost=new_insurance_cost-insurcane_cost


print("The change in estimated cost for smkoer  is  "+str(
change_in_insurance_cost)+" dollars.")
