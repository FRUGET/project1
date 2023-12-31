upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
result = []

isEncryption = int(input("Шифр Цезаря\nШифрувати(парне) чи Дешифрувати(непарне)?\nВибрати число: "))

if isEncryption % 2 == 0:
    isEncryption = True #парне (шифрувати)
    print("*Шифрувати*")
else:
    isEncryption = False #непарне (дешифрувати)
    print("*Дешифрувати*")

step = int(input('Крок здвигу: '))


def encryption(text):
    if step < 0:
        print("Рух в ліву сторону не розроблено, в завданні вказано тільки праворуч :)")
        return
    for char in text:
        if char in upper_case:
            for i in range(len(upper_case)):
                if char == upper_case[i]:
                    if i + step > len(upper_case):
                        i += step - len(upper_case)
                        while i > len(upper_case):
                            i -= len(upper_case)
                            if i > 25:
                                result.append(upper_case[i - 1])
                        result.append(upper_case[i])
                    else:
                        result.append(upper_case[i + step])
        elif char in lower_case:
            for i in range(len(lower_case)):
                if char == lower_case[i]:
                    if i + step > len(lower_case):
                        i += step - len(lower_case)
                        while i > len(lower_case):
                            i -= len(lower_case)
                            if i > 25:
                                result.append(lower_case[i - 1])
                        result.append(lower_case[i])
                    else:
                        result.append(lower_case[i + step])
        else:
            result.append(char)
    print('Не зашфирований текст: ', text, '\nЗашифрований текст: ', ''.join(result))

def decryption(text):
    for char in text:
        if char in upper_case:
            for i in range(len(upper_case)):
                if char == upper_case[i]:
                    if i + step > len(upper_case):
                        i += step - len(upper_case)
                        while i > len(upper_case):
                            i -= len(upper_case)
                            if i > 25:
                                result.append(upper_case[i - 1])
                        result.append(upper_case[i])
                    else:
                        result.append(upper_case[i + step])
        elif char in lower_case:
            for i in range(len(lower_case)):
                if char == lower_case[i]:
                    if i + step > len(lower_case):
                        i += step - len(lower_case)
                        while i > len(lower_case):
                            i -= len(lower_case)
                            if i > 25:
                                result.append(lower_case[i - 1])
                        result.append(lower_case[i])
                    else:
                        result.append(lower_case[i + step])
        else:
            result.append(char)
    print('Зашфирований текст: ', text, '\nНе зашифрований текст: ', ''.join(result))

if isEncryption == True:
    user_input = input('Введіть текст який потрібно зашифрувати:\n')
    encryption(user_input)
else:
    user_input = input('Введіть текст який потрібно розшифрувати:\n')
    decryption(user_input)