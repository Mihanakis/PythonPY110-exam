from conf import MODEL
from itertools import count
from random import randint, uniform, choice
import faker, json
fake = faker.Faker("ru")
fake.isbn13()


def gen_counter(counter=1):  # генератор-счётчик
    for current_number in count(counter):
        yield current_number
    return


def title():
    input_file = "books.txt"
    f = open(input_file, "r", encoding="utf-8")
    for i, line in enumerate(f):
        line = line.replace("\n", "")
        if i >= randint(0, 5):
            return line


def year():  # случайный год от даты изобретения книгопечатания
    return randint(1445, 2022)


def pages():  # случайное количество страниц
    return randint(10, 1000)


def isbn13():  # возвращает случайное числв в формате ISBN13
    return fake.isbn13()


def rating():  # случайный рейтинг
    return round(uniform(0, 5), 2)


def price():  # случайная цена
    return str(round(uniform(1, 100), 2)) + "$"


def author():
    output_names = []
    for i in range(randint(1, 3)):
        if i % 2 == 0:
            output_names.append(fake.first_name_male() + " " + fake.last_name_male())
        else:
            output_names.append(fake.first_name_female() + " " + fake.last_name_female())
    return output_names


def to_json_file(obj_data):
    output_file = "output.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(obj_data, f, indent=4, ensure_ascii=False)


def main():
    pk = next(gen_counter())
    fields = {"title": title(),
              "year": year(),
              "pages": pages(),
              "isbn13": isbn13(),
              "rating": rating(),
              "price": price(),
              "author": author()}
    data = {"model": MODEL, "pk": pk, "fields": fields}
    to_json_file(data)


if __name__ == '__main__':
    main()
