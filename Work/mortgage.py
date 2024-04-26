# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
total_months = 0
extra_payment = 1000
extra_payment_start = 61
extra_payment_end = 108

while principal > 0: 
    if total_months >= extra_payment_start and total_months <= extra_payment_end:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
    principal = principal * (1+rate/12) - payment 
    total_paid = total_paid + payment 
    total_months = total_months + 1
    if principal <= payment:
        total_paid = total_paid + principal
        principal = principal - principal
        total_months = total_months + 1
    print(total_months,round(total_paid,2),principal)

print('Total paid', round(total_paid,2), 'over',total_months,'months')

print(f'You paid {round(total_paid)} over {total_months} months')