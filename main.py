import json
import faker
from conf import MODEL
from random import randint, uniform
from itertools import count
fake = faker.Faker("ru")


def gen_counter(counter: int = 1) -> iter:
    """
    Фабрика генераторов для подсчёта вызова с шагом 1.
    :param counter: начало работы счётчика, тип int (по умолчанию 1);
    :return: счётчик-итератор с шагом 1;
    """
    for current_number in count(counter):
        yield current_number
    return


def title() -> str:
    """
    Функция для вывода произвольной строки названия книги из файла "books.txt".
    :return: строка str с названием книги;
    """
    input_file = "books.txt"
    f = open(input_file, "r", encoding="utf-8")
    for i, line in enumerate(f):
        line = line.replace("\n", "")
        if i >= randint(0, 5):
            return line


def year() -> int:
    """
    Функция возвращает случайный год в промежутке от года изобретения книгопечатания до текущего.
    :return: число типа int от 1445 до 2022;
    """
    return randint(1445, 2022)


def pages() -> int:
    """
    Функция возвращает случайное количество страниц книги.
    :return: число типа int от 10 до 1000;
    """
    return randint(10, 1000)


def isbn13() -> str:
    """
    Функция возвращает случайный набор чисел по формату ISBN13.
    :return: строка с набором чисел формата ISBN13;
    """
    return fake.isbn13()


def rating() -> float:
    """
    Функция возвращает случайное число для вывода рейтинга.
    :return: число типа float от 1 до 5, округлённое до двух знаков после запятой;
    """
    return round(uniform(0, 5), 2)


def price() -> str:
    """
    Функция возвращает случайную цену книги.
    :return: произвольное число от 1 до 100, округлённое до 2-х знаков, типа str с добавлением знака $ в конце;
    """
    return str(round(uniform(1, 100), 2)) + "$"


def author() -> list:
    """
    Функция возвращает список в котором содержится от 1 до 3 имён и фамилий, произвольно мужских или женских.
    :return: список строк, от 1 до 3 элементов внутри списка, состоящий из имён и фамилий
    """
    output_names = []
    for i in range(randint(1, 3)):
        if i == randint(1, 3):
            output_names.append(fake.first_name_male() + " " + fake.last_name_male())
        else:
            output_names.append(fake.first_name_female() + " " + fake.last_name_female())
    return output_names


def to_json_file(obj_data: dict, output_file: str) -> None:
    """
    Функция для записи сгенерированных элементов в файл output.json. Файл может быть создан с нуля.
    :param obj_data: словарь сгенерированных данных, который необходимо записать;
    :param output_file: название файла, в которое предстоит произвести запись;
    :return: None
    """
    with open(output_file, "a", encoding="utf-8") as f:
        json.dump(obj_data, f, indent=4, ensure_ascii=False)


def clear_json(output_file: str) -> None:
    """
    Функция для очистки файла типа json
    :param output_file: название файла, который необходимо очистить;
    :return: None
    """
    open(output_file, "w")


def main() -> None:
    """
    Функция для генерации 100 различных массивов данных типа dict, содержащих: модель, счётчик, поля.
    В словаре "поля" прописаны: название книги, год, количество страниц, номер ISBN13, рейтинг, цена, автор.
    Использует функцию clear_json для очистки файла json и to_json_file для записи в файл json.
    :return: None
    """
    output_file = "output.json"
    clear_json(output_file)
    pk = gen_counter()
    fields = ({"title": title(),
               "year": year(),
               "pages": pages(),
               "isbn13": isbn13(),
               "rating": rating(),
               "price": price(),
               "author": author()} for a in count())
    data = ({"model": MODEL, "pk": next(pk), "fields": next(fields)} for b in count())
    for c in range(100):
        to_json_file(next(data), output_file)


if __name__ == '__main__':
    main()
