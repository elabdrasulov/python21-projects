
class Cars:
    objects = []
    carcase = ("седан", "универсал", "купе", "хэтчбек", "минивен", "внедорожник", "пикап")
    _id = 0
    
    def __init__(self, brand, model, year, volume, color, body, mileage, price):
        self.id = Cars._id
        self.brand = brand
        self.model = model
        self.volume = volume
        self.year = year
        self.volume = volume
        self.color = color
        self.mileage = mileage
        self.price = price
        if body in Cars.carcase:
            self.body = body
        else:
            raise Exception("Введите кузов из списка!" )
        Cars.objects.append(self)
        Cars._id += 1
    
    @property
    def comment(self):
        return [com for com in Comment.objects if com.car == self]

class Comment:
    objects = []

    def __init__(self, car, text):
        from datetime import datetime
        self.car = car
        self.text = text
        self.created_at = datetime.now()
        Comment.objects.append(self)
