# 1.
#-------------------------------------------------------------------------------------------------------
print('1.\nСоздайте несколько переменных заканчивающихся и не оканчивающихся на «s».\n'
      'Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s\n'
      '(кроме переменной из одной буквы s) на None.Значения не удаляются, \n'
      'а помещаются в одноимённые переменные без s на конце.\n')


def s_object_replace(**kwargs):
    print('Изначальный словарь kwargs: ')
    print(kwargs)
    kwargs_dict = {}
    for obj, m in kwargs.items():
        if obj.endswith('s') and len(obj) > 1:
            kwargs_dict[obj] = None
            obj_2 = obj[:-1]
            kwargs_dict[obj_2] = m
        else:
            kwargs_dict[obj] = m
    print('\nИтоговый словарь: ')
    return kwargs_dict


print(s_object_replace(wars='wars', calls='calls', nos='nos', s='s', abscence='abscence'))

# 2.
#-------------------------------------------------------------------------------------------------------

print(f'\n2.\nНапишите функцию для транспонирования матрицы: ')


def matrix_transpose(matrix: list[list]):
    print(f'\nПолученная матрица: ')

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            print(matrix[row][col], end='\t')
        print()
    print(f'\n')
    transposed_matrix = []
    for lst in zip(*m):
        transposed_matrix.append(list(lst))
    print('Транспонированная матрица: ')
    for r in range(len(transposed_matrix)):
        for c in range(len(transposed_matrix[0])):
            print(transposed_matrix[r][c], end='\t')
        print()
    return transposed_matrix


m = [[1, 3, 4], [78, 5, 4], [2, 8, 9], [2, 8, 9]]
matrix_transpose(m)

# 3.
#-------------------------------------------------------------------------------------------------------

print(f'\n3.\nНапишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, \n'
      f'где ключ — значение переданного аргумента, а значение — имя аргумента. \nЕсли ключ не хешируем, '
      f'используйте его строковое представление.')


def key_parameters_dictionary(**kwargs) -> dict:
    print(f'\nДан словарь kwargs: ')
    print(f'{kwargs}\n')
    print(f'\nИтоговый словарь: ')
    new_kwargs = {}
    for key, value in kwargs.items():
        if type(value) == list or \
                type(value) == frozenset or \
                type(value) == bytearray or \
                type(value) == dict:
            new_kwargs[str(value)] = key
        else:
            new_kwargs[value] = key

    return new_kwargs


print(key_parameters_dictionary(arg_1=[1, 2], arg_2=234, arg_3='LIST', arg_4={1: 2}))

# 4.
#-------------------------------------------------------------------------------------------------------

print(f'\n4.\nВозьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. \n'
      f'Дополнительно сохраняйте все операции поступления и снятия средств в список.\n')

from decimal import Decimal

CMD_DEPOSIT = 'п'
CMD_WITHDRAW = 'с'
CMD_EXIT = 'в'
LOGGING = 'л'
MULTIPLICITY = 50
PERCENT_REMOVAL = Decimal(15) / Decimal(1000)
MIN_REMOVAL = Decimal(30)
MAX_REMOVAL = Decimal(600)
PERCENT_DEPOSIT = Decimal(3) / Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = Decimal(10) / Decimal(100)
RICHNESS_SUM = Decimal(10_000_000)

logging = []
number = 0
global draft_dict
count = 0


def main():
    global draft_dict
    bank_account = Decimal(0)
    global count
    while True:
        draft_dict = {'amount': 0, 'bank_account': Decimal(0),
                      'percent': Decimal(0), 'sum_percent': Decimal(0), 'transaction': 1}
        action = input(f'\nПополнить - "{CMD_DEPOSIT}", снять - "{CMD_WITHDRAW}", '
                       f'вывести логи - "{LOGGING}", выйти - "{CMD_EXIT}": \n')
        if action == CMD_EXIT:
            print(f'Возьмите карту на которой {int(bank_account)} у.е.')
            break
        elif action == LOGGING:
            print(*logging, sep="\n")
            continue

        elif action == CMD_DEPOSIT:
            if bank_account > RICHNESS_SUM:
                rich_perc_dict, bank_account = on_the_rich_tax(bank_account, draft_dict)
                replenish_withdrawal_logging(rich_perc_dict)
            replenish_dict, bank_account = cmd_deposit_replenish(bank_account, draft_dict)
            replenish_withdrawal_logging(replenish_dict)
            if count % COUNTER4PERCENTAGES == 0:
                perc_per3_dict, bank_account = percent_per3_op(bank_account, draft_dict)
                replenish_withdrawal_logging(perc_per3_dict)


        elif action == CMD_WITHDRAW:
            if bank_account > RICHNESS_SUM:
                perc_rich_dict, bank_account = on_the_rich_tax(bank_account, draft_dict)
                replenish_withdrawal_logging(perc_rich_dict)
            withdrawal_dict, bank_account = cmd_deposit_withdrawal(bank_account, draft_dict)
            replenish_withdrawal_logging(withdrawal_dict)
            if count % COUNTER4PERCENTAGES == 0:
                dict_per3_perc, bank_account = percent_per3_op(bank_account, draft_dict)
                replenish_withdrawal_logging(dict_per3_perc)

        else:
            print(f'Неверное действие для карты на которой {round(bank_account)} у.е.')


# =================================================


# Ф-я пополнения денег
def cmd_deposit_replenish(bank_acc: Decimal, d_dict: dict) -> tuple:
    global count
    count += 1
    amount = 1
    while (amount % MULTIPLICITY) != 0:
        amount = Decimal(input(f'Введите сумму кратную {MULTIPLICITY} у.е. '))
    bank_acc += amount
    print(f'\nПополнение карты на {amount} у.е. Итого {int(bank_acc)} у.е.')
    d_dict['amount'] = amount
    d_dict['bank_account'] = bank_acc
    return d_dict, bank_acc


# Ф-я снятия денег

def cmd_deposit_withdrawal(bank_acc: Decimal, d_dict: dict) -> tuple:
    global count
    amount = 1
    while (amount % MULTIPLICITY) != 0:
        amount = Decimal(input(f'Введите сумму кратную {MULTIPLICITY} у.е. '))
    d_dict['percent'] = -PERCENT_REMOVAL
    percent = amount * PERCENT_REMOVAL
    percent = MIN_REMOVAL if percent < MIN_REMOVAL else MAX_REMOVAL if percent > MAX_REMOVAL else percent
    if bank_acc >= amount + percent:
        count += 1
        bank_acc = bank_acc - amount - percent
        print(f'\nСнятие с карты {amount} у.е. Процент за снятие {round(PERCENT_REMOVAL, 2)}%. '
              f'Сумма {round(percent, 2)} у.е. Итого {int(bank_acc)} у.е.')
        d_dict['amount'] = -amount
        d_dict['bank_account'] = bank_acc
        d_dict['sum_percent'] = -percent
    else:
        print(f'Недостаточно средств. Сумма с комиссией {round(PERCENT_REMOVAL, 2)}% - {round(amount + percent)} у.е. '
              f'На карте {round(bank_acc)} у.е.')
        d_dict['amount'] = -amount
        d_dict['bank_account'] = bank_acc
        d_dict['sum_percent'] = -percent
        d_dict['transaction'] = 0
    return d_dict, bank_acc


def on_the_rich_tax(bank_acc: Decimal, d_dict: dict) -> tuple:
    d_dict['percent'] = -RICHNESS_PERCENT
    percent = bank_acc * RICHNESS_PERCENT
    bank_acc -= percent
    print(f'\nВычтен налог на богатство {RICHNESS_PERCENT}% в сумме {round(percent, 2)} у.е. '
          f'Итого {int(bank_acc)} у.е.\n')
    d_dict['amount'] = 0
    d_dict['bank_account'] = bank_acc
    d_dict['sum_percent'] = percent
    return d_dict, bank_acc


def percent_per3_op(bank_acc: Decimal, data_dict: dict) -> tuple:
    data_dict['percent'] = PERCENT_DEPOSIT
    amount_percent = round(bank_acc * PERCENT_DEPOSIT, 2)
    bank_acc += amount_percent
    print(f'\nНачислено {PERCENT_DEPOSIT}% за {COUNTER4PERCENTAGES} '
          f'операций в сумме {round(amount_percent, 2)} у.е. Итого {int(bank_acc)} у.е.')
    data_dict['amount'] = 0
    data_dict['sum_percent'] = amount_percent
    data_dict['bank_account'] = bank_acc
    return data_dict, bank_acc


# Ф-я логгирования
def replenish_withdrawal_logging(data_dict: dict) -> list:
    global logging
    global number
    number += 1
    logging.append(f"{number}. Снятие/пополнение: {round(data_dict['amount'], 2)} у.е. "
                   f"Сумма на счету: {round(data_dict['bank_account'], 2)} у.е."
                   f" Процент комиссии: {round(data_dict['percent'], 2)}%"
                   f' Сумма комиссии: {round(data_dict["sum_percent"], 2)} у.е.'
                   f" Изменение счета: {data_dict['transaction']}")
    return logging


# =================================================


if __name__ == "__main__":
    main()
