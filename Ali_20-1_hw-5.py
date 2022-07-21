"""

написать валидацию на Номера Транспартов
будет класс ValidCarNumber —> будет метод is_valid(self, number)
который принимает 1 аргумент number и проверяет на валидность то есть:

Input:

    01KG777BAD
    hhh777hhh

Output:

    Номер валидный!
    Номер не валидный!

"""
import re


class ValidCarNumber:
    def __init__(self, number):
        self.number = number
    def is_valid(self):
        is_valid = re.search(r"0([0-9]{1})KG([0-9]{3})([A-Z]{3})", self.number)
        try:
            if self.number[is_valid.start():is_valid.end()] == self.number:
                print("Valid number")
        except:
            print("Invalid number")

number = input('Пример: 01KG777BAD \nВведите номер транспарта: ')
BMW = ValidCarNumber(number)
BMW.is_valid()