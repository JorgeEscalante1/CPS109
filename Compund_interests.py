"""Compound interests rate calculator"""
#from decimal import Decimal


principal = float(input('Enter the principal amount: ') or 100)
rate = float(input('Enter the savings rate (.05 for 5%): ') or 0.05)
years = int(input('Enter the number of years to save: ') or 5)
annual = float(input('Enter the annual addition to save ') or 0)
for year in range(1, years + 1):
    amount = principal * (1 + rate) ** years
    if year > 1:
        amount = amount * (1 + rate) ** years
    print(f'{year>2}{amount:>10.2f}')