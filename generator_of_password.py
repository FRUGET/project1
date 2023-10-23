import random

varinats = ['0123456789', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz', '!#$%&*+-=?@^_.']
chars = ''
questions = ['Включати цифри?', 'Включати великі літери?', 'Включати маленькі літери?', 'Включати символи?']
result = ''

print("Вітаю в програмі генерації паролів! Але перед початком генерації, я задам Вам декілька запитань")
count_password = int(input("Кількість паролів: "))
length_password = int(input("Довжина одного пароля: "))
my_list = {0: None, 1: None, 2: None, 3: None} #digits, upperletters, lowerletters, punctuations
for obj in my_list:
    user_input = int(input(f"{questions[obj]} (0: так, 1: ні)\n"))
    if user_input == 0:
        my_list[obj] = True
    elif user_input == 1:
        my_list[obj] = False

for obj in my_list:
    if my_list[obj] == True:
        chars += varinats[obj]
    else:
        continue

if chars == '':
    print("Всі параметри виключені, пароль не може бути сгенерований.")
else:
    for i in range(count_password):
        for j in range(length_password):
            result += random.choice(chars)
        print(result)
        result = ''