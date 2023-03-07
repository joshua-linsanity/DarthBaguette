from numpy import *

spending = {'Defense Spending': 0.152, 'Non-Defense Discretionary Spending': 0.148, 'Health Care': 0.253, 'Social Security': 0.234, 'Other Mandatory Spending': 0.13, 'Interest on the Debt': 0.085}
revenues = {'Individudal Income Taxes': 0.496, 'Corporate Taxes': 0.066, 'Payroll Taxes': 0.359, 'Other Revenue': 0.079}

total_spending = 1.4E12 / 1E9 # billions
total_revenues = 3.6E12 / 1E9 # billions

for key in spending:
    print(f"{key}: ${(spending[key] * total_spending):.2f} bn")

print()

for key in revenues:
    print(f"{key}: ${(revenues[key] * total_revenues):.2f} bn")

