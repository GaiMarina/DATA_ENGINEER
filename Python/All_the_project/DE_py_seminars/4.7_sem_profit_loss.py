"""Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
Вычислите итоговую прибыль или убыток каждой компании.
Если все компании прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
"""

import random


def profit_loss_companies(comp_s: list[str], min_num: int, max_num: int, min_sum: int, max_sum: int) -> dict:
    # Создаем список названий компаний
    # companies = ["Company A", "Company B", "Company C", "Company D", "Company E"]

    print("\nThe list of companies: \n")
    # Генерируем словарь с доходами и расходами для каждой компании
    company_finances = {}

    for company in comp_s:
        # Генерируем случайное количество доходов и расходов (от 3 до 10)
        num_transactions = random.randint(min_num, max_num)

        # Генерируем список доходов и расходов
        transactions = [random.randint(min_sum, max_sum) for _ in range(num_transactions)]

        # Добавляем компанию и ее финансовую информацию в словарь
        company_finances[company] = transactions

    # Выводим получившийся словарь
    for company, finances in company_finances.items():
        print(f"{company}: {finances}")

    return company_finances


def if_all_profitable(companies_list: dict):
    print(f"\nCompanies' profit/loss: \n")
    companies_sum_profit = []
    for company in companies_list.items():
        print(f'{company[0]} = {sum(company[1])}')
        companies_sum_profit.append(sum(company[1]))
    print('\nIf all the companies are profitable:\n')
    return all(map(lambda s: s > 0, companies_sum_profit))


companies = ['Digital', 'Commerce', 'Vanis', 'Navis']
companies_dict = profit_loss_companies(companies, 3, 10, -100_000, 100_000)

print(if_all_profitable(companies_dict))
