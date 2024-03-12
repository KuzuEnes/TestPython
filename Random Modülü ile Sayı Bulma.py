# random modülü ile rastgele sayı bulma oyunu

import random

x = random.randint(0,10) # 0 ile 10 arasında rastgele bir sayı oluşturuyor.


while True:
    number = int(input("Enter a number: "))
    if number > x:
        print("Too high")
    elif number < x:
        print("Too low")

    else:
        print("İt is a number.Congratulation !! ")
    break

