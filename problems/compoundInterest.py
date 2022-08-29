import decimal
# taking information from user
principal = float(input('Enter Principal Amount: '))
interest_rate = float(input('Enter interest rate (in %): '))
num_years = int(input('Enter number of years: '))


amount = principal * (1 + interest_rate) ** num_years

print(f'Amount at the end of {num_years} is {amount}')