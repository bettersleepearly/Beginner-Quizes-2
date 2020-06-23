print("Question:\n Find even numbers in range 1000,3000...")
n = str(input("It's quiz 11 bietchh, type any fockin thing at all to start the equation of finding even numbers from 1000 to 3000: "))
nums = []
for i in range(1000, 3000 + 1):
    if i % 2 == 0:
        nums.append(i)
str_num = [str(x) for x in nums]
result = ", ".join(str_num)
print(result)
#print(my_list)