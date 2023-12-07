#Создать телефонный справочник с возможностью импорта и экспорта данных в формате csv
#Фамилия, имя, отчество, номер телефона - данные, которые должны находится в файле
#1. Программа должна выводить данные 
#2. Программа должна сохранять данные в файл
#3. Пользователь может ввести одну их характеристик для поиска определнной записи (имя или фамилия)
#4. Использование функций. Программа не должна быть линейной

from os.path import exists
from csv import DictReader, DictWriter

class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt

class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt

def get_info():

    is_valid_name = False
    while not is_valid_name:
        try:
            first_name = input("Введите имя: ")
            if len(first_name) < 2:
                raise NameError("Невалидное имя")
            else:
                is_valid_name = True

        except NameError as err:
            print(err)
            continue

    last_name = "222"

    is_valid_phone = False
    while not is_valid_phone:
        try:
            phone_number = int(input("Введите номер: "))
            if len(str(phone_number)) != 11:
                raise LenNumberError("Неверная длина номера")
            else:
                is_valid_phone = True
        except ValueError:
            print("Невалидный номер")
            continue
            
        except LenNumberError as err:
            print(err)
            continue

    return [first_name, last_name, phone_number]

def create_file(file_name):
    # with - менеджер контекста
    with open(file_name, "w", encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()

def read_file(file_name):
    with open(file_name, "r", encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)
    
def write_file(file_name, lst):
    res = read_file(file_name)

    for el in res:
        if el["Телефон"] == str(lst[2]):
            print("Такой телефон уже существует")
            return

    obj = {"Имя": lst[0], "Фамилия": lst[1], "Телефон": lst[2]}
    res.append(obj)
    with open(file_name, "w", encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)

def copy_file(file_name, new_file_name, row):

    if not exists(new_file_name):
        create_file(new_file_name)

    res = read_file(file_name)
    result = list(res[row-1].values())

    print(result)

    write_file(new_file_name, result)


file_name = "phone.csv"
new_file_name = "new_phone.csv"


def main():
    while True:
        command = input("Введите команду: ")
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == 'r':
            if not exists(file_name):
                print("Файл отсутствует - создайте его")
                continue
            print(*read_file(file_name))
        elif command == 'c':
            copy_file(file_name, new_file_name, 2)

main()