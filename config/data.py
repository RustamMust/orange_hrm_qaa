import os
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()


class Data:
    LOGIN = os.getenv('LOGIN')
    PASSWORD = os.getenv('PASSWORD')


@dataclass
class Person:
    first_name: str = None
    last_name: str = None
    age: int = None
