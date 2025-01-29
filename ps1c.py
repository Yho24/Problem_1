## 6.100A PSet 1: Part C
## Name:
## Time Spent:
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Enter the initial deposit:"))
def part_c(initial_deposit):
    low = 0.01
    high = 0.5
    r = (high+low)/2.0
    steps = 0
    epsilon = 100
    amount_saved = 0
    while abs(amount_saved-down_payment_house) >= epsilon:
        amount_saved = 0
        months = 0
        for months in range(36):
            amount_saved = initial_deposit *(1+(r/12))**(months+1)
        if amount_saved < down_payment_house:
            low = r
        else:
            high = r
        r = (high + low)/2.0
        steps += 1
        if steps >1000:
            return None
    return (r, steps)
#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
cost_house = 800000
portion_down_payment = 0.25
down_payment_house = cost_house*portion_down_payment
amount_saved = 0
a = part_c(initial_deposit)
print("Best savings rate:"+ str(a[0]))
print("Steps in bisection search:" +str(a[1]))

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################

