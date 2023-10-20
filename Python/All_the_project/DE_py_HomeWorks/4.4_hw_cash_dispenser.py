"""Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.
"""
"""
Напишите программу банкомат.
Начальная сумма равна нулю
Допустимые действия: пополнить, снять, выйти
Сумма пополнения и снятия кратны 50 у.е.
Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
После каждой третей операции пополнения или снятия начисляются проценты - 3%
Нельзя снять больше, чем на счёте
При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
Любое действие выводит сумму денег
"""

#=================================================================

import decimal

CMD_DEPOSIT = 'п'
CMD_WITHDRAW = 'с'
CMD_EXIT = 'в'
MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

bank_account = decimal.Decimal(0)
count = 0

while True:
    action = input(f'Пополнить - "{CMD_DEPOSIT}", снять - "{CMD_WITHDRAW}", выйти - "{CMD_EXIT}": ')
    if action == CMD_EXIT:
        print(f'Возьмите карту на которой {round(bank_account)} у.е.')
        break

    if bank_account > RICHNESS_SUM:
        percent = bank_account * RICHNESS_PERCENT
        bank_account -= percent
        print(f'Вычтен налог на богатство {RICHNESS_PERCENT}% в сумме {round(percent)} у.е. Итого {round(bank_account)} у.е.')

    if action in (CMD_DEPOSIT, CMD_WITHDRAW):
        amount = 1
        while (amount % MULTIPLICITY) != 0:
            amount = decimal.Decimal(input(f'Введите сумму кратную {MULTIPLICITY} у.е. '))

    if action == CMD_DEPOSIT:
        count += 1
        bank_account += amount  # noqa
        result = f'Пополнение карты на {amount} у.е. Итого {round(bank_account)} у.е.'

    elif action == CMD_WITHDRAW:
        percent = amount * PERCENT_REMOVAL
        percent = MIN_REMOVAL if percent < MIN_REMOVAL else MAX_REMOVAL if percent > MAX_REMOVAL else percent
        if bank_account >= amount + percent:
            count += 1
            bank_account = bank_account - amount - percent
            result = f'Снятие с карты {amount} у.е. Процент за снятие {round(percent)}. Итого {round(bank_account)} у.е.'
        else:
            result = f'Недостаточно средств. Сумма с комиссией {round(amount + percent)} у.е. На карте {round(bank_account)} у.е.'

    else:
        result = f'Неверное действие для карты на которой {round(bank_account)} у.е.'

    if count % COUNTER4PERCENTAGES == 0:
        amount_percent = bank_account * PERCENT_DEPOSIT
        bank_account += amount_percent
        result = f'{result}\nНачислено {PERCENT_DEPOSIT}% за {COUNTER4PERCENTAGES} ' \
                 f'операций в сумме {amount_percent} у.е. Итого {round(bank_account)} у.е.'

    print(result)