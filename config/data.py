import os
from dataclasses import dataclass


class Data:
    LOGIN = os.getenv('LOGIN')
    PASSWORD = os.getenv('PASSWORD')


@dataclass
class Person:
    first_name: str = None
    last_name: str = None
    age: int = None

