"""
Задание 1.

Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего

Подсказка:
Для решения задачи обязательно примените коллекцию из модуля collections
Для лучшего освоения материала можете сделать
несколько варианто решения этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
"""

from typing import NamedTuple


class AverageCompanyRevenue(NamedTuple):
    """NamedTuple type class for main function"""
    comp_name: str
    avg_revenue: float


def input_company() -> AverageCompanyRevenue:
    """calculates average revenue for a company"""
    comp_name = input('Введите название предприятия: ')
    revenues = input('Через пробел введите прибыль данного предприятия '
                     'за каждый квартал(Всего 4 квартала): ')
    if len(revenues.split(' ')) == 4:
        revenues_list = [float(x) for x in revenues.split(' ')]
        return AverageCompanyRevenue(comp_name, sum(revenues_list) / len(revenues_list))
    print('Вы указали неподходящее количество квартальных прибылей, их должно быть 4!')
    return input_company()


def main() -> None:
    """inputs companies and their revenues, outputs average revenue over all of them"""
    companies_num = int(input('Введите количество предприятий для расчета прибыли: '))
    companies_revenues = []
    above_avg = []
    below_avg = []
    for _ in range(companies_num):
        companies_revenues.append(input_company())
    overall_avg = sum(rev for comp, rev in companies_revenues) / companies_num
    companies_revenues.append(AverageCompanyRevenue('Average', overall_avg))
    print(f'Средняя годовая прибыль всех предприятий: {companies_revenues[-1].avg_revenue}')
    for revenue in companies_revenues[:-1]:
        if revenue.avg_revenue >= companies_revenues[-1].avg_revenue:
            above_avg.append(revenue.comp_name)
        else:
            below_avg.append(revenue.comp_name)
    print(f'Предприятия с прибылью выше среднего значения: {", ".join(above_avg)}')
    print(f'Предприятия с прибылью ниже среднего значения: {", ".join(below_avg)}')


if __name__ == '__main__':
    main()
