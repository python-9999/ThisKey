class BaseClass(Exception):
    """
    --базовый класс--
    аргументы:
    message - основное сообщение ошибки,
    extra_info - доп. Информация об ошибке (необязательный аргумент, поэтому extra_info=None)
    """
    def __init__(self, message, extra_info=None):
        if type(self) is BaseClass: # проверка, если вызовут базовый класс (так нельзя)
            raise NotImplementedError("базовый класс вызывать нельзя")
        super().__init__(message, extra_info)

# ---ИСКЛЮЧЕНИЯ---
class ThisNotLetter(BaseClass):
    """ исключение которое означает что 'это не клавиша (буква)' """
    pass

class ThisNotNum(ThisNotLetter):
    """ исключение которое означает что 'это не цифра (цифра)' """
    pass

class LenError(ThisNotNum):
    """исключение означает что буква больше или меньше 1 символа (потому что если буква не равно один символ это не буква)"""
    pass