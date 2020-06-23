print("Question:\nCheck if a list of 4 digit binary numbers % to 5...")
print('Quiz9 matafakar!!!')
n = str(input('Give me a list of numbers of 4 digits binaries so i can find if they are dividable to 5 or not \n(divide each numbers with ","): '))


my_list = n.split(",")

#1st terribly failed attemp:
#while my_list < 1111:
#    my_list.remove(my_list /5 != 0)
#else:   
#    print('This need to be all binaries')  

#2nd terribly failed attemp:
#my_list = []
#for i in n:
#    my_list.append(i / 5)
#print(my_list)

#3rd terribly failed attemp:
#num = my_list[0][1][2][3] % 5
#while num != 0:
#    del 
#else:
#    print(num)

#While loop use failed attemp:
#i = my_list.append()
#a = int(i,2)
#while a % 5 == 0:
#    print('\nThe binary number that is dividable to 5 is:'+ "\n" + i)


#Perfectly success attemp:
for i in my_list:
    a = int(i, 2)
    if a % 5 == 0:
        print('\nThe binary number that is dividable to 5 is:'+ "\n" + i)