"""Функция принимает на вход три списка одинаковой длины:
имена str,
ставка int,
премия str с указанием процентов вида «10.25%».
Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии. """


names = ['Марина', 'Александра', 'Максим', 'Рома']
salary_rate = [34_000, 50_000, 80_000, 132_000]
award = ['10.25%', '1.3%', '2.4%', '0.3%']


def awards_dict(nms: [str], rate: [int], awrd: [str]) -> dict:
    award = list(map(lambda n: float(n.replace("%", "")) / 100.0, [num for num in awrd]))
    dict_awards = {nms: int(rate * award) for nms, rate, award in zip(nms, rate, award)}
    return dict_awards


print(awards_dict(names, salary_rate, award))



