def get_full_name(first_name: str, last_name: str):
    full_name  = f"{first_name.title()} {last_name.title()}"
    return full_name


print(get_full_name("john", "doe"))

def get_name_with_age(name: str, age: int):
    name_with_age = f"{name} is this old {age}"
    return name_with_age

print(get_name_with_age("Juan", 29))

def process_items(items: list[int]):
    for item in items:
        print(item)

lista = [1,2,3]
print(process_items(lista))

def process_items(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s

tupla = (1, 2, "Coco")
sete = {255, 255, 0, 2}

print(process_items(tupla, sete))

def process_items(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(f"{item_name} su precio es: {item_price}")

prices = {
    "Coca cola" : 11500,
    "Chocolatina" : 5000,
    "Pilsen" : 4500
}

print(process_items(prices))


def process_item(item: int | str):
    print(item)

print(process_item(5))
print(process_item("Coco"))

def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")

print(say_hi("Juan"))
print(say_hi())

class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name

nombre = Person("Juan Esteban")
print(get_person_name(nombre))

