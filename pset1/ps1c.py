annual_salary = float(input("Enter the starting salary: "))
best_portion_saved = 0.0
total_cost = 1000000
portion_down_payment = 0.25
r = 0.04
low = 0
high = 1
count = 0

def calculate_savings(annual_salary, portion_saved, months = 36, semi_annual_raise = 0.07):
    current_savings = 0.0
    for i in range(months):
        current_savings += current_savings*r/12
        current_savings += annual_salary*portion_saved/12
        if i%6 == 0:
            annual_salary = annual_salary*(1+semi_annual_raise)
    return current_savings

while True:
    gap = calculate_savings(annual_salary, best_portion_saved) - total_cost*portion_down_payment
    if abs(gap) < 100:
        print("Best savings rate:", round(best_portion_saved,2))
        print("Steps in bisection search:", count)
        break
    elif gap > 0:
        high = best_portion_saved
    else:
        low = best_portion_saved
    if best_portion_saved == (high + low)/2:
        print("It is not possible to pay the down payment in three years.")
        break
    best_portion_saved = (high + low)/2
    count += 1