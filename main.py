money = int(input())
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
for value in per_cent.values():
       value =(money * value) / 100
       deposit.append(value)
print('Список депозитов в различных банках', deposit)
print(max(deposit), "Максимальный депозит из спика депозитов")