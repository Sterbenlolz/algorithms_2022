"""
Задание 2.

Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections

defaultdict(list)
int(, 16)
reduce

2) через ООП

вспомните про перегрузку методов

__mul__
__add__
"""
NUMBER_STR = '0123456789ABCDEF'
NUMBER_DICT = dict(zip(NUMBER_STR, range(16)))
REVERSE_NUMBER_DICT = dict(zip(range(16), NUMBER_STR))


class HexadecimalNumber:
    """Hexadecimal number class"""

    def __init__(self, hex_num: list):
        self.hex_num = hex_num
        self.decimal_num = sum(
            16 ** (len(self.hex_num) - i - 1) *
            NUMBER_DICT[self.hex_num[i]] for i in range(len(self.hex_num)))

    def __add__(self, other) -> list:
        res_num = self.decimal_num + other.decimal_num
        hexa_num_list = []
        while res_num >= 16:
            hexa_num_list.append(REVERSE_NUMBER_DICT[res_num % 16])
            res_num //= 16
        hexa_num_list.append(REVERSE_NUMBER_DICT[res_num])
        return hexa_num_list[::-1]

    def __mul__(self, other) -> list:
        res_num = self.decimal_num * other.decimal_num
        hexa_num_list = []
        while res_num // 16 > 0:
            hexa_num_list.append(REVERSE_NUMBER_DICT[res_num % 16])
            res_num //= 16
        hexa_num_list.append(REVERSE_NUMBER_DICT[res_num])
        return hexa_num_list[::-1]

    def __str__(self):
        return str(self.hex_num)


def input_number() -> list:
    """Inputs a hexadecimal number"""
    number_str = input('Please input a hexadecimal number: ').upper()
    number_list = []
    for digit in number_str:
        if digit not in NUMBER_STR:
            print('Invalid number! Please try again.')
            return input_number()
    for digit in number_str:
        number_list.append(digit)
    return number_list


def main() -> None:
    """Main func"""
    hexa_num_1 = HexadecimalNumber(input_number())
    print(hexa_num_1)
    hexa_num_2 = HexadecimalNumber(input_number())
    print(hexa_num_2)
    print(hexa_num_1 + hexa_num_2)
    print(hexa_num_1 * hexa_num_2)


if __name__ == '__main__':
    main()
