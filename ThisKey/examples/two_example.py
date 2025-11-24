from src import key

# игра "введи по клавишам слово pass"
keys = ("p", "a", "s", "s")
count = 0

while count < len(keys):
    user_key = input(f"введите клавишу {keys[count]}: ")
    if key.is_press(user_key, keys[count]):
        count += 1
    else:
        print(f"ошибка, нужно было ввести клавишу \"{keys[count]}\" а не \"{user_key}\"")
print(f"Вы успешно ввели слово '{''.join(keys)}'")