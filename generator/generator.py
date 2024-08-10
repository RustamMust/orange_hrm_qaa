import random

from config.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')
faker_en = Faker('En')
Faker.seed()


def generated_person():
    yield Person(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        age=random.randint(10, 80),
    )



