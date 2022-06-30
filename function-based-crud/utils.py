"""Файл с дополнительными функциями"""


def generate_id(ids):
    """
    Принимает список существующих id\n
    Возвращает новое id в диапазоне от 100 до 1000
    """
    import random
    id_ = random.randint(100, 1000)
    while id_ in ids:
        id_ = random.randint(100, 1000)
    return id_

def validate_passwords(p1, p2):
    """
    Принимает 2 пароля\n
    Если они не совпадают, вызывается ошибка
    """
    if p1 != p2:
        raise Exception("Пароли не совпадают")

def validate_id(ids, u_id):
    """
    Принимает список существующих id и id, которое нужно проверить\n
    Если такого id нет в списке, вызывается Exception
    """
    if u_id not in ids:
        raise Exception("Такого юзера нет")
