## 6.100A PSet 1: Part B
## Name:
## Time Spent:
## Collaborators:

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################
yearly_salary = float(input('Enter your yearly salary:'))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
cost_of_dream_home = float(input("Enter the cost of your dream house:"))
semi_anual_raise = float(input("Enter the semi-anual raise, as a decimal:"))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
def part_b(yearly_salary, portion_saved, cost_of_dream_home, semi_anual_raise):
    portion_down_payment = 0.25
    amount_saved = 0
    anual_return = 0.05
    months = 0
    new_yearly_salary = yearly_salary
    cost_of_downpayment = cost_of_dream_home*portion_down_payment
    while amount_saved<cost_of_downpayment:
        amount_saved += amount_saved*(anual_return/12)
        amount_saved += (new_yearly_salary/12)*portion_saved
        months += 1
        if months%6 == 0:
            new_yearly_salary *= 1+semi_anual_raise
    #print("Number of months:"+ str(Number_of_months))
    return months

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
months = part_b(yearly_salary, portion_saved, cost_of_dream_home, semi_anual_raise)
print("Number of months:"+ str(months))
