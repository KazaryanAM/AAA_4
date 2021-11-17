import json
from keyword import iskeyword


class GetAttributes:
    def __init__(self, data: dict):
        for key, value in data.items():
            if iskeyword(key):
                key = f'{key}_'
            if key == 'price':
                key = f'_{key}'
            if isinstance(value, dict):
                setattr(self, key, GetAttributes(value))
            else:
                setattr(self, key, value)


class ColorizeMixin:
    repr_color_code = 33

    def __repr__(self):
        text = super().__repr__()
        return f'\033[1;{self.repr_color_code};40m{text}'


class ReprAdvert:
    def __init__(self, data: dict):
        super().__init__(data)

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


class Advert(ColorizeMixin, ReprAdvert, GetAttributes):
    def __init__(self, data: dict):
        super().__init__(data)

    @property
    def price(self):
        if hasattr(self, '_price'):
            if self._price < 0:
                raise ValueError('must be >= 0')
            else:
                return self._price
        else:
            return 0


if __name__ == "__main__":
    corgi_str = """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs",
        "location": {
            "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
        }
    }"""
    lesson_str = """{
        "title": "python",
        "price": 0,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
        }
    }"""
    corgi_json = json.loads(corgi_str)
    corgi = Advert(corgi_json)
    print(corgi)
    print(corgi.class_)
    print(corgi.location.address)
    lesson_json = json.loads(lesson_str)
    lesson = Advert(lesson_json)
    print(lesson.location.address)
    print(lesson.price)
    print(lesson)
    