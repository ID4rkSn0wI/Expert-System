import csv


def get_person_info(name):
    with open("data/data.csv", 'r', encoding="utf-8") as f:
        text = csv.reader(f, delimiter=',')
        for line in text:
            if line[0] == name:
                answer = (f"\nКритик/Не критик - {line[1]}\n"
                          f"Бюджетная способность клиента - {line[2]}\n"
                          f"Процентное соотношения чека и чаевых - {line[3]}\n"
                          f"Стоит ли предлагать алкогольные напитки - {line[4]}\n"
                          f"Влияет ли алкоголь на поведение клиента - {line[5]}\n")
                return answer


name = input("Введите имя клиента: ")
print(get_person_info(name))