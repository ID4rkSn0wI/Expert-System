import csv
import random

import pandas as pd
from pandas.core.construction import ensure_wrapped_if_datetimelike

ALCOHOL = \
[
'Вино красное'
'Джин',
'Мохито',
'Виски' ,
'Шапманское',
'Вино белое',
'Апероль',
'Бренди',
'Текила',
'Мартини'
]


# def get_person_info(name):
#     """
#     По ФИО клиента ищет выводы из ЭС
#
#     :param name: ФИО клиента
#     :return: Данные по клиенту
#     """
#
#     with open("data/data.csv", 'r', encoding="utf-8") as f:
#         text = csv.reader(f, delimiter=',')
#         for line in text:
#             if line[0] == name:
#                 answer = (f"\nКритик/Не критик - {line[1]}\n"
#                           f"Бюджетная способность клиента - {line[2]}\n"
#                           f"Процентное соотношения чека и чаевых - {line[3]}\n"
#                           f"Стоит ли предлагать алкогольные напитки - {line[4]}\n"
#                           f"Влияет ли алкоголь на поведение клиента - {line[5]}\n")
#                 return answer


def get_rate_of_critic(restaurant):
    """

    Получает оценку критиком ресторана

    :param restaurant: Ретсоран
    :return:
    """

    with open("data/restaurants.csv", 'r', encoding="utf-8") as f:
        text = csv.reader(f, delimiter=',')
        for line in text:
            if line[0] == restaurant:
                return float(line[-1])


def calculate_sr_summ(name):
    """

    Считает среднюю сумму чека

    :param name: ФИО клиента
    :return:
    """

    with open("data/cheque.csv", 'r', encoding="utf-8") as f:
        text = csv.reader(f, delimiter=',')
        cnt, summ = 0, 0
        for line in text:
            if line[0] == name:
                cnt += 1
                summ += float(line[-3])
    return summ / cnt


def calculate_sr_rate(name):
    """

    Считает среднюю оценку ретсорана клиента

    :param name: ФИО клиента
    :return:
    """

    with open("data/clients.csv", 'r', encoding="utf-8") as f:
        text = csv.reader(f, delimiter=',')
        cnt, summ = 0, 0
        for line in text:
            if line[0] == name:
                cnt += 1
                summ += float(line[-1])
    return summ / cnt


def calculate_sr_behavior(name):
    """

    Считает среднее поведение клиента

    :param name: ФИО клиента
    :return:
    """

    with open("data/clients.csv", 'r', encoding="utf-8") as f:
        text = csv.reader(f, delimiter=',')
        cnt, summ = 0, 0
        for line in text:
            if line[0] == name:
                cnt += 1
                summ += float(line[-3])
    return summ / cnt


def calculate_sr_percent_of_alcohol(name):
    """

    Считает соотношение заказов с алкоголя ко всем заказам

    :param name: ФИО клиента
    :return:
    """

    with open("data/cheque.csv", 'r', encoding="utf-8") as f:
        text = csv.reader(f, delimiter=',')
        cnt, summ = 0, 0
        for line in text:
            if line[0] == name:
                cnt += 1
                summ += float(line[-1])
    return summ / cnt


def calculate_sr_sootn_cheka_and_summ(name):
    """

    Считает соотношение чаевых и суммы чека

    :param name: ФИО клиента
    :return:
    """

    with open("data/cheque.csv", 'r', encoding="utf-8") as f:
        text = csv.reader(f, delimiter=',')
        cnt, summ = 0, 0
        for line in text:
            if line[0] == name:
                cnt += 1
                summ += float(line[-2]) / float(line[-3])
    return summ / cnt


def check_restaurant(restaurant):
    """

    Проверяет наличие ресторана

    :param restaurant: Ресторан
    :return:
    """

    with open("data/restaurants.csv", 'r', encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=',')
        is_found = False
        for rest in reader:
            if rest[0] == restaurant:
                is_found = True
    with open("data/restaurants.csv", 'a', encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=',')
        if not is_found:
            writer.writerow([restaurant, random.randint(0, 10)])

def calculate_sr_otkl_from_critics(name):
    """

    Считает среднее отклонение оценки клиента от оценки критика

    :param name: ФИО клиента
    :return:
    """

    with open("data/clients.csv", 'r', encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=',')
        cnt, summ = 0, 0
        for line in reader:
            if line[0] == name:
                critics_rate = get_rate_of_critic(line[1])
                summ += abs(float(line[-3]) - float(critics_rate))
                cnt += 1
    return summ / cnt


def probability_of_being_critic(name):
    """

    Считает вероятность, что клиент - критик

    :param name: ФИО клиента
    :return:
    """

    sr_rate = calculate_sr_otkl_from_critics(name)

    if sr_rate <= 0.2:
        return "Высокая"
    elif sr_rate <= 0.5:
        return "Низкая"
    else:
        return "Не критик"


def rate_of_clients_budget(name):
    """

    Оценивает бюджетную способность клиента

    :param name: ФИО клиента
    :return:
    """

    sr_summ = calculate_sr_summ(name)

    if sr_summ >= 5000:
        return "Высокая"
    elif sr_summ >= 2000:
        return "Выше среднего"
    elif sr_summ >= 1000:
        return "Средняя"
    else:
        return "Бюджетная"


def shedrost_of_client(name):
    """

    Оценивает щедрость клиента

    :param name: ФИО клиента
    :return:
    """

    sootn = calculate_sr_sootn_cheka_and_summ(name)

    if sootn >= 0.2:
        return "Щедрый"
    elif sootn >= 0.1:
        return "Средняя щедрость"
    else:
        return "Скупой"


def should_ask_for_alcohol(name):
    """

    Стоит ли предлагать алкоголь клиенту

    :param name: ФИО клиента
    :return:
    """

    percent = calculate_sr_percent_of_alcohol(name)

    if percent >= 0.5:
        return "Стоит"
    else:
        return "Не стоит"


def is_alchogol_affects_clients_behavior(name):
    """

    Влияет ли алкоголь на клиента

    :param name: ФИО клиента
    :return:
    """

    percent = calculate_sr_percent_of_alcohol(name)
    sr_behavior = calculate_sr_behavior(name)

    if percent >= 0.5 and sr_behavior <= 6:
        return "Влияет"
    else:
        return "Не влияет"


def rate_of_clients_behavior(name):
    """

    Оценка поведения клиента

    :param name: ФИО клиента
    :return:
    """

    sr_behavior = calculate_sr_behavior(name)

    if sr_behavior >= 7:
        return "Хорошее"
    elif sr_behavior >= 4:
        return "Среднее"
    else:
        return "Плохое"

print(
    "\nКакое действие вы хотите совершить?\n"
    "1) Создать анкету клиента\n"
    "2) Создать анкету сотрудника\n"
    "3) Создать чек\n"
    "4) Вывести информацию\n"
)

answer = input("")

if answer == "1":
    data = []

    print("\nВведите ФИО клиента через пробел\n")
    answer = input("")
    while not(len(answer.split()) == 3 and all(isinstance(a, str) for a in answer)):
        answer = input("")
    data.append(answer)

    print("\nВведите название ресторана\n")
    answer = input("")
    while not(all(isinstance(a, str) for a in answer)):
        answer = input("")
    data.append(answer)

    print("\nВведите оценку вкуса еды\n")
    answer = input("")
    while not answer.isdigit():
        answer = input("")
    data.append(int(answer))

    print("\nВведите оценку ценовой политики\n")
    answer = input("")
    while not answer.isdigit():
        answer = input("")
    data.append(int(answer))

    print("\nВведите цель визита\n")
    answer = input("")
    while not all(isinstance(a, str) for a in answer):
        answer = input("")
    data.append(answer)

    check_restaurant(data[1])

    with open("data/clients.csv", 'a', encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(data)

elif answer == '2':
    data = []

    print("\nВведите ФИО сотрудника через пробел\n")
    answer = input("")
    while not (len(answer.split()) == 3 and all(isinstance(a, str) for a in answer)):
        answer = input("")
    data.append(answer)

    print("\nВведите ФИО клиента через пробел\n")
    answer = input("")
    while not (len(answer.split()) == 3 and all(isinstance(a, str) for a in answer)):
        answer = input("")
    data.append(answer)

    print("\nВведите название ресторана\n")
    answer = input("")
    while not (all(isinstance(a, str) for a in answer)):
        answer = input("")
    data.append(answer)

    print("\nВведите оценку поведения клиента\n")
    answer = input("")
    while not answer.isdigit():
        answer = input("")
    data.append(int(answer))

    print("\nВведите количество персон за столом\n")
    answer = input("")
    while not answer.isdigit():
        answer = input("")
    data.append(int(answer))

    print("\nВведите оценку отзывчивости клиента\n")
    answer = input("")
    while not answer.isdigit():
        answer = input("")
    data.append(int(answer))

    check_restaurant(data[1])

    with open("data/employees.csv", 'a', encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(data)

elif answer == "3":
    data = []

    print("\nВведите ФИО клиента через пробел\n")
    answer = input("")
    while not (len(answer.split()) == 3 and all(isinstance(a, str) for a in answer)):
        answer = input("")
    data.append(answer)

    print("\nВведите название ресторана\n")
    answer = input("")
    while not (all(isinstance(a, str) for a in answer)):
        answer = input("")
    data.append(answer)

    print("\nВведите блюда\n")
    answer = input("")
    while not all(isinstance(a, str) for a in answer):
        answer = input("")
    data.append(answer)

    print("\nВведите напитки\n")
    answer = input("")
    while not answer.isdigit():
        answer = input("")
    data.append(int(answer))

    print("\nВведите размер чаевых\n")
    answer = input("")
    while not answer.isdigit():
        answer = input("")
    data.append(int(answer))

    if any([alc in data[-2] for alc in ALCOHOL]):
        data.append(1)
    else:
        data.append(0)

    check_restaurant(data[1])

    with open("data/cheque.csv", 'a', encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(data)

elif answer == "4":
    print("\nВведите ФИО клиента через пробел\n")
    answer = input("")
    while not (len(answer.split()) == 3 and all(isinstance(a, str) for a in answer)):
        answer = input("")
    name = answer

    print(f"Вероятность, что клиент - критик - {probability_of_being_critic(name)}")
    print(f"Оценка бюджетной способности клиента - {rate_of_clients_budget(name)}")
    print(f"Щедрость клиента - {shedrost_of_client(name)}")
    print(f"Стоит ли предлагать алкогольные напитки - {should_ask_for_alcohol(name)}")
    print(f"Оценка поведения клиента - {rate_of_clients_behavior(name)}")
    print(f"Влияет ли алкоголь на поведение клиента - {is_alchogol_affects_clients_behavior(name)}")
