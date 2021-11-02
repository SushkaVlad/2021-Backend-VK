
dict_of_cars = dict()


class Car:

    def __init__(self, idx: int, model: str, price: int, comment: str):
        self.id = idx
        self.model = model
        self.price = price
        self.comment = comment
