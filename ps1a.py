## 6.100A PSet 1: Part A
## Name:
## Time Spent:
## Collaborators:

def part_a(yearly_salary, portion_saved, cost_of_dream_home):
    portion_down_payment = 0.25
    amount_saved = 0
    anual_return = 0.05
    months = 0
    cost_of_downpayment = cost_of_dream_home*portion_down_payment
    while amount_saved<cost_of_downpayment:
        amount_saved += amount_saved*(anual_return/12)
        amount_saved += (yearly_salary/12)*portion_saved
        months += 1
    #print("Number of months:"+ str(Number_of_months))
    return months
##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################

yearly_salary = float(input('Enter your yearly salary:'))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
cost_of_dream_home = float(input("Enter the cost of your dream house:"))
months = part_a(yearly_salary, portion_saved, cost_of_dream_home)
print("Number of months:"+ str(months))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################


###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
