"""Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
имена str, ставка int, премия str с указанием процентов вида «10.25%».
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии
"""


names = ['Иван', 'Николай', 'Алексей', 'Марк']
salary_rate = [25_000, 80_500, 32_000, 32_000]
awards = ['10.25%', '0.25%', '13.0%', '9.9%']
generator = {name: rate * float(award.strip('%')) / 100 for name, rate, award in zip(names, salary_rate, awards)}
print(*generator.items(), type(generator), sep='\n')