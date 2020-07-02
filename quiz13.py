print("\nQuiz 12, draw a square tringale with fucking money by inserting a number for the tringale sides'length.")
n = int(input("\nNumber bitch:"))
i = 0
j = 0
space = "  "
money = "$"
for i in range(0,2):
    i += 1
    print((money+" ")*i)
for i in range(2,n-1):
    i += 1
    j += 1
    blank = space*j
    print(money+" "+blank+money)
print((money+" ")*n)