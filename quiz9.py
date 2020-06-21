print('Quiz9 matafakar!!!')
n = str(input('Give me a list of numbers of 4 digits binaries so i can find if they are dividable to 5 or not \n(divide each numbers with ","): '))


my_list = n.split(",")
#while my_list < 1111:
#    my_list.remove(my_list /5 != 0)
#else:   
#    print('This need to be all binaries')  

#my_list = []
#for i in n:
#    my_list.append(i / 5)
#print(my_list)

#num = my_list[0][1][2][3] % 5
#while num != 0:
#    del 
#else:
#    print(num)


for i in my_list:
    a = int(i, 2)
    if a % 5 == 0:
        print('\nThe binary number that is dividable to 5 is:'+ "\n" + i)