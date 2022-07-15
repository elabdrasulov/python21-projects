from serializer import CarsSerializer
from utils import get_obj_or_404
from models import Cars, Comment
# from decimal import Decimal

def create():
    brand = input("Введите марку: ")
    model = input("Введите модель: ")
    year = int(input("Введите год выпуска: "))
    volume = round(float(input("Введите объем двигателя: ")), 1)
    # .quantize(Decimal("1.0"))
    color = input("Введите цвет: ")
    mileage = int(input("Введите пробег: "))
    price = round(float(input("Введите цену: ")), 2)
    # .quantize(Decimal(".01"))
    body = input(f"Выберите кузов: {Cars.carcase}\n")

    Cars(brand, model, year, volume, color, body, mileage, price)
    return "Запись о машине успешно создана"

def car_list(): #listing
    serializer = CarsSerializer()
    car = serializer.serialize_queryset()
    return car

def car_detail(p_id): #retrieve
    car = get_obj_or_404(Cars, "id", int(p_id))
    serializer = CarsSerializer()
    return serializer.serialize_obj(car)

def car_update(p_id):
    car = get_obj_or_404(Cars, "id", int(p_id))
    field = input("Выберите поле, которое следует изменить: ")
    if field in dir(car):
        print(f"Старое значение: {getattr(car, field)}")
        new_value = input(f"{field} = ")
        setattr(car, field, new_value)
    else:
        raise Exception(f"Поля {field} нет")
    return car_detail(p_id)

def car_delete(p_id):
    car = get_obj_or_404(Cars, "id", int(p_id))
    Cars.objects.remove(car)
    return "Запись о машине успешно удалена"

def comment():
    print("Выберите машину:")
    for p in Cars.objects:
        print(p.brand)
    brand = input("=======================\n")
    car = get_obj_or_404(Cars, "brand", brand)
    text = input("Введите комментарий: ")
    Comment(car, text)
    return "Комментарий успешно добавлен"

