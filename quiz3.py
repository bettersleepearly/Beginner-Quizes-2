print("Question:\nAccepts a sequence of comma-seperated numbers then generate a list and tuples of those numbers...")
income = str(input('So...I guess, give me some random numbers (please include "," between each variable):'))
outcome = income.split(',')
tuplez = tuple(outcome)

print(outcome)
print(tuplez)