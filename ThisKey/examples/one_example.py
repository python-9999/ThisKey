# примеры кода на библиотеке ThisKey
from src import key

# просто отслеживает клавишу и показывает её, в случаи ошибки покажет текст из extra_info и ошибку
while True:
    user_key = input("press...")
    print(key.LetterKey.key(user_key, extra_info="введите букву а не цифру или что то другое."))

# cd C:\Users\masen\.vscode\ThisKey
# python -m examples.one_example.py