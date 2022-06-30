"==========CRUD============"
# Create - создать
# Read - прочитать
# Update - обновить 
# Delete - удалить

from utils import validate_id

# database = {
#     "Бекзат": "скала",
#     "Эртай": "пароль",
#     "Оомат": "Кыргызстан",
#     "Имран": "12345",
#     "Жийде": "return",
#     "Манас": "Маке",
#     "Арафат": "54321",
#     "Элжаз": "парол",
#     "Гулсана": "312",
#     "Эркайым": "Айдин",
#     "Бекназ": "Арёль",
#     "Эдиль": "ьлорап",
#     "Айгул": "май",
#     "Закир": "@@@",
#     "Бегайым": "makers",
#     "Мырзайым": "Bootcamp2221",
#     "Даниэл": "covid19",
#     "Жибек": "1404",
#     "Калысбек": "стол",
#     "Ырыс": "suuuuuuuuiiiiiiiiiiii",
#     "Айканыш": "qwerty",
#     "Арген": "11172332",
#     "Нурмухамед": "Не верный",
#     "Бектур": "0101",
#     "Алан": "душу питона",
#     "Куба": "1",
#     "Жаангер": "ох блин",
#     "Богдан": "Кудайберген",
#     "Айгерим": "синий маркер",
#     "Настя": "Python21",
#     "Жаркынай": "Мафия"
# }

# import random


# ids = []

# for key, value in database.copy().items():
#     id = random.randint(100, 999)
#     while id in ids:
#         id = random.randint(100, 999)
#     ids.append(id)

#     database[id] = {
#         'name': key,
#         'password': value,
#         'info': '...'
#     }
#     del database[key]

# print(database)

database = {
    296: {'name': 'Бекзат', 'password': 'скала', 'info': '...'}, 
    134: {'name': 'Эртай', 'password': 'пароль', 'info': '...'}, 
    987: {'name': 'Оомат', 'password': 'Кыргызстан', 'info': '...'}, 
    273: {'name': 'Имран', 'password': '12345', 'info': '...'}, 
    596: {'name': 'Жийде', 'password': 'return', 'info': '...'}, 
    514: {'name': 'Манас', 'password': 'Маке', 'info': '...'}, 
    912: {'name': 'Арафат', 'password': '54321', 'info': '...'}, 
    801: {'name': 'Элжаз', 'password': 'парол', 'info': '...'}, 
    518: {'name': 'Гулсана', 'password': '312', 'info': '...'}, 
    366: {'name': 'Эркайым', 'password': 'Айдин', 'info': '...'}, 
    861: {'name': 'Бекназ', 'password': 'Арёль', 'info': '...'}, 
    599: {'name': 'Эдиль', 'password': 'ьлорап', 'info': '...'}, 
    567: {'name': 'Айгул', 'password': 'май', 'info': '...'}, 
    394: {'name': 'Закир', 'password': '@@@', 'info': '...'}, 
    672: {'name': 'Бегайым', 'password': 'makers', 'info': '...'}, 
    182: {'name': 'Мырзайым', 'password': 'Bootcamp2221', 'info': '...'}, 
    770: {'name': 'Даниэл', 'password': 'covid19', 'info': '...'}, 
    420: {'name': 'Жибек', 'password': '1404', 'info': '...'}, 
    556: {'name': 'Калысбек', 'password': 'стол', 'info': '...'}, 
    570: {'name': 'Ырыс', 'password': 'suuuuuuuuiiiiiiiiiiii', 'info': '...'}, 
    954: {'name': 'Айканыш', 'password': 'qwerty', 'info': '...'}, 
    149: {'name': 'Арген', 'password': '11172332', 'info': '...'}, 
    267: {'name': 'Нурмухамед', 'password': 'Не верный', 'info': '...'}, 
    209: {'name': 'Бектур', 'password': '0101', 'info': '...'}, 
    731: {'name': 'Алан', 'password': 'душу питона', 'info': '...'}, 
    718: {'name': 'Куба', 'password': '1', 'info': '...'}, 
    653: {'name': 'Жаангер', 'password': 'ох блин', 'info': '...'}, 
    405: {'name': 'Богдан', 'password': 'Кудайберген', 'info': '...'}, 
    698: {'name': 'Айгерим', 'password': 'синий маркер', 'info': '...'}, 
    744: {'name': 'Настя', 'password': 'Python21', 'info': '...'}, 
    689: {'name': 'Жаркынай', 'password': 'Мафия', 'info': '...'}
    }


def read(u_id):
    """
    Принимает id юзера\n
    Выводит его имя и информацию\n
    Если такого юзера нет, вызывается Exception
    """
    validate_id(database.keys(), u_id)
    name = database[u_id]['name']
    info = database[u_id]['info']
    print(f"""
==========={u_id}============
Name: {name}
Info: {info}
==========================
""")


def create():
    """
    Запрашивает данные о пользователе\n
    Записывает их в базу данных
    """
    from utils import generate_id, validate_passwords
    name = input('Введите имя: ')
    password = input("Введите пароль: ")
    password2 = input("Введите подтверждение пароля: ")
    validate_passwords(password, password2)
    info = input("Введите информацию о вас: ")
    id_ = generate_id(database.keys())
    database[id_] = {
        "name": name, 
        "password": password,
        "info": info
    }

    print("Вы были успещно добавлены в Python21")
    

def delete(u_id):
    """
    Принимает id пользователя\n
    Если юзер существует, он удаляется из базы данных\n
    Если юзера нет, то вызывается ошибка
    """
    validate_id(database.keys(), u_id)
    name = database[u_id]['name']
    del database[u_id]
    print(f'user {name} был успешно удален')


def update(u_id):
    """
    Принимает id юзера\n
    Выводит старые данные\n
    Принимает новые данные\n
    Изменяет в базе данных
    """
    validate_id(database.keys(), u_id)
    read(u_id)
    #  принимает новые данные
    name = input("Введите имя: ")
    info = input("Введите информацию о вас: ")
    # sex = input("Укажите пол (м,ж): ")

    database[u_id]['name'] = name
    database[u_id]['info'] = info
    # database[u_id]['sex'] = sex
    read(u_id)
