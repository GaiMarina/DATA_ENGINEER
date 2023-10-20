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
"""
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
"""
# =====================================================

amount = 0
op_count = 1


def main():
    global amount
    global op_count
    while True:
        s = input('Выберите операцию (1 - пополнить; 2 - снять; 3 - выход) : ')
        if s not in ('1', '2', '3'):
            continue
        if amount > 5 * 10 ** 6:
            amount = amount * 0.9
        if s == '1':
            fill()
        elif s == '2':
            withdraw()
        else:
            print_amount()
            break
        print_amount()


def print_amount():
    global amount
    print(f'На счете {amount} ед.')


def fill():
    # Пополнение
    # баланса

    global amount
    global op_count
    while True:
        v = input('Укажиет сумму пополнения кратная 50 ед :')
        # if v == 'q':
        #     break
        try:
            s = int(v)
        except ValueError:
            continue
        if not s % 50 == 0:
            print(f'Сумма пополнения должна быть кратна 50 ед.')
            continue
        amount += s
        amount = amount + (percent(0.03) if op_count % 3 == 0 else 0)
        op_count += 1
        break


def withdraw():
    # Снятие

    global amount
    global op_count
    while True:
        v = input('Укажите сумму снятия кратная 50 ед :')
        # if v == 'q':
        #     break
        try:
            s = int(v)
        except ValueError:
            continue
        if not s % 50 == 0:
            print(f'Сумма пополнения должна быть кратна 50 ед.')
            continue
        p = percent(0.015)
        # но не менее 30 и не более 600 у.е
        if p < 30:
            p = 30
        if p > 600:
            p = 600
        if amount < s + p:
            print(f'Недостаточно средств на счете.')
            break
        amount = amount - s - p
        amount = amount + (percent(0.03) if op_count % 3 == 0 else 0)
        op_count += 1
        break


def percent(procent):
    global amount
    return round(amount * procent, 2)


if __name__ == 'main':
    main()


def deposit(balance: float, amount: float) -> float:
    balance += amount
    return balance


def withdraw(balance: float, amount: float) -> float:
    if amount > balance:
        print("Ошибка: недостаточно средств на счете")
        return balance

    withdrawal_fee = max(30, min(amount * 0.015, 600))
    balance -= amount + withdrawal_fee
    return balance


def calculate_interest(balance: float) -> float:
    interest = balance * 0.03
    balance += interest
    return balance


def calculate_wealth_tax(balance: float) -> float:
    wealth_tax = balance * 0.1
    balance -= wealth_tax
    return balance


def main():
    balance = 0
    action_count = 0

    while True:
        action = input("Введите действие (пополнить, снять, выйти): ")

        if action == "пополнить":
            amount = int(input("Введите сумму для пополнения: "))
            if amount % 50 != 0:
                print("Ошибка: некорректная сумма пополнения, надо число кратное 50ти")
                continue

            balance = deposit(balance, amount)
            action_count += 1

        elif action == "снять":
            amount = int(input("Введите сумму для снятия: "))
            if amount % 50 != 0:
                print("Ошибка: некорректная сумма снятия")
                continue

            if balance >= 5_000_000:
                balance = calculate_wealth_tax(balance)

            balance = withdraw(balance, amount)
            action_count += 1

        elif action == "выйти":
            break

        else:
            print("Ошибка: некорректное действие")
            continue

        if action_count % 3 == 0:
            balance = calculate_interest(balance)

        print(f"Текущий баланс: {balance}")


if __name__ == "main":
    main()
