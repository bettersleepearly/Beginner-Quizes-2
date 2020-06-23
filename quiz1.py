print("Question:\nFind numbers that dividable to 7 and 5 in the range of 2000, 3200...")
print('Hi!!!\nSee now, I know your name is ADAM :)')
intro = str(input('\nRight? If yes type "fuckyea", if no type "byebitch" :):'))
print('___________________________________________________________________________________________________________________________________________________')
if intro == "byebitch":
    print('Oh... Well shit :)')
if intro == "fuckyea":
    for number in range(2000, 3200 + 1):
        if(number % 7 == 0, number % 5 != 0):
            print(number)