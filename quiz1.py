print('Hi!!!\nSee now, I know your name is ADAM :)')
intro = str(input('\nRight? If yes type "fuckyea", if no type "byebitch" :):'))
print('___________________________________________________________________________________________________________________________________________________')
if intro == "byebitch":
    print('Oh... Well shit :)')
if intro == "fuckyea":
    for number in range(2000, 3200):
        if(number % 7,5 != 0):
            print(number)
