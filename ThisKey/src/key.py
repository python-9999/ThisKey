from src import data_keys as dtk
from src import exceptions as exp

# КЛАССЫ ДЛЯ РАБОТЫ С НАЖАТИЯМИ
class LetterKey:
    """класс для работы с клавишами (с буквами)"""
    @staticmethod
    def key(key: str, extra_info=None):
        # проверка, разработчик указал в аргументе key str тип, или нет
        if not isinstance(key, str):
            raise TypeError("ошибка, вы передали в аргумент key не тип str")
        
        # проверка длины буквы
        if len(key) != 1:
            raise TypeError(f"ошибка, len(key) != 1 | ({key}❌)")

        # проверка, указана ли в аргументе буква
        if not key in dtk.list_keys_letters:
            raise exp.ThisNotLetter("ошибка, это не буква", extra_info)
        # --если нажата клавиша--
        return key


class NumberKey:
    """класс для работы с клавишами (с цифрами)"""
    @staticmethod
    def key(key: int, extra_info=None):
        # проверка, указана ли в аргументе цифра
        if key not in dtk.list_keys_numbers:
            raise exp.ThisNotNum("ошибка, это целое число а не нажатая клавиша", extra_info)

        # --если введена правильная цифра--
        return key

# ФУНКЦИИ ПРОВЕРКИ НАЖАТА ЛИ ОПРЕДЕЛЕНАЯ КЛАВИША
def is_press(k, desired):
    # --если это буква--
    if isinstance(k, str):
        # проверка длины буквы
        if len(k) != 1:
            raise exp.LenError(f"ошибка, вы передали в функцию is_press не клавишу ({k}❌)")
    
    # --если это цифра--
    elif isinstance(k, int):
        if k not in dtk.list_keys_numbers:
            raise exp.ThisNotNum("ошибка, это целое число а не нажатая клавиша")
    
    # если нажата клавиша
    if k == desired:
        return True
    return False