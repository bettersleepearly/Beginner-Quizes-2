income = str(input('Now...I guess give me a sentence with bunch of repeating words for reason :):'))
my_list = income.split(" ")
my_list = list(dict.fromkeys(my_list))
my_list.sort()
extra = " "
result = extra.join(my_list)
print(result)