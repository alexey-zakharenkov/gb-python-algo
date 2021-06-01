"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 числа) для каждого предприятия. Программа должна
определить среднюю прибыль (за год для всех предприятий) и отдельно
вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""

from collections import defaultdict, deque

firm_names = list()
profits = defaultdict(deque)

n = int(input("Введите количество предприятий: "))

for i in range(1, n+1):
    firm_name = input(f"Введите имя {i}-го предприятия: ")
    firm_names.append(firm_name)

    for j in range(1, 4+1):
        profit = float(input(f"Введите прибыль {i}-го предприятия за {j}-й квартал: "))
        profits[firm_name].append(profit)

overall_profit = 0.0

for firm_name, quarter_profits in profits.items():
    for profit in quarter_profits:
        overall_profit += profit

average_profit = overall_profit / len(profits)

print(f"Средняя прибыль за год по предприятиям = {average_profit:0.2f}")

low_profit_firms = deque()
high_profit_firms = deque()

for firm_name, quarter_profits in profits.items():
    year_profit = 0
    for profit in quarter_profits:
        year_profit += profit
    firm_container = low_profit_firms if year_profit < average_profit else high_profit_firms
    firm_container.append(firm_name)

print("Предприятия с прибылью ниже среднего:")
for firm_name in low_profit_firms:
    print(firm_name)

print("Предприятия с прибылью выше среднего:")
for firm_name in high_profit_firms:
    print(firm_name)

""" Пример входных данных:
3
Рога
352.35
398.8
400
350.01
Копыта
600
658.1
705
499
ИнПромТорг
102
304
405.1
149.8
"""
