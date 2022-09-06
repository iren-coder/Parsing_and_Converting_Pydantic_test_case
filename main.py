import json
import converter


def read_data(filename):
    '''
    Считывание данных из json файла.
    :param filename: путь до файла.
    :return: словарь (dict).
    '''
    with open(filename, "r", encoding='utf-8') as file:
        data = json.load(file)
        return data


def write_data(filename, data):
    '''
    Запись данных в json файл.
    :param filename: путь до файла.
    :param data: данные в виде словаря (dict).
    '''
    with open(filename, "w", encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4, separators=(',', ': '))


def main():
    rd = read_data("input.json")  # Данные прочитанные из файла
    data = converter.converting(rd)  # Конвертируем, прочитанные данные, в другую структуру
    write_data("output.json", data.dict())  # Запись, конвертируемых данных, в файл


if __name__ == '__main__':
    main()
