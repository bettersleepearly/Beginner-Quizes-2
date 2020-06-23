print("Question:\nCALCULATE letters and digits from a sentence...")
n = str(input('Quiz10 now bitch, give me sentences and numbers so i can count them: '))
#my_list = n.split()
#words = 0
#digits = 0


#for i in my_list:
#    i.isalpha()
#    words += 1

#    i.isdigit()
#    digits += 1

#print(my_list)

#for i in n:
#    letters = sum(i.isalpha())
#    digits = sum(i.isdigit())
#    print(letters)
#    print(digits)

letters = 0
digits = 0
for i in n:
    if i.isalpha():
        letters+=1
    elif i.isdigit():
        digits+=1

print("Here's the amount of letters:")
print(letters)
print("Here's the amount of digits:")
print(digits)