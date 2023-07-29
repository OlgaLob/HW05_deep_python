# Напишите функцию, которая принимает на вход строку — абсолютный путь до
# файла. Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os


def file_info(file_path):
    path, filename = os.path.split(file_path)
    name, extension = os.path.splitext(filename)
    return path, name, extension


file_path = 'C:\\Python\\PycharmProjects\\scrum_run\\scrumboard\\board\\admin.py'

print(file_info(file_path))
