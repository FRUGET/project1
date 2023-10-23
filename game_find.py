import random

tries = 0
left = 1
print('Ласкаво просимо в числову угадайку')
right = int(input(f'До якого числа загадати?\nВід {left} до '))
random_number = random.randint(left, right)
print(f"Число від {left} до {right} загадано! Спробуйте вгадати:")
temp_left = left
temp_right = right

while True:
    user_input = int(input("Число: "))
    if user_input < temp_left or user_input > temp_right:
        print(f"Ви ввели неправильне число, введіть значення від {temp_left} до {temp_right}")
    elif random_number == user_input:
        tries += 1
        print(f"Ви відгадали, вітаємо! Витрачено спроб: {tries}\nБажаєте зіграти ще? (0: так, 1: ні)")
        choice = int(input())
        if choice == 0:
            print(f"Число від {left} до {right} загадано! Спробуйте вгадати:")
            tries = 0
            temp_left = left
            temp_right = right
            random_number = random.randint(left, right)
            continue
        else:
            print("Дякую, що грали в числову вгадайку. Ще побачимось...")
            break
    elif random_number > user_input:
        temp_left = user_input + 1
        tries += 1
        print(f"Число занадто маленьке, спробуйте ще раз! Межі гадання зменшені (від {temp_left} до {temp_right})")
    else:
        temp_right = user_input - 1
        tries += 1
        print(f"Число занадто велике, спробуйте ще раз! Межі гадання зменшені (від {temp_left} до {temp_right})")