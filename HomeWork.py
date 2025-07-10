monday = float(input('введите сумму за понедельник:' ))
tuesday = float(input('введите сумму за вторник:'))
wednesday = float(input('введите сумму за среду:'))
thursday = float(input('введите сумму за четверг:'))
friday = float(input('введите сумму за пятницу:'))
saturday = float(input('введите сумму за субботу:'))
sunday = float(input('введите сумму за воскресенье:'))

summ = monday + tuesday + wednesday + thursday + friday + saturday + sunday
print(f"Общяя сумма: {summ}")

average = summ / 7
average_round = round(average, 1)
print(f"Среднее арифметическое: {average_round}")

if average_round >= 1 and average_round <= 20:
    print('низкий разход')
elif average_round >= 21 and average_round <= 40:
    print('средний разход')
elif average_round >= 41 :
    print('высокий разход')
else:
    print('ничего не потрачено')
напиши с маль ошиб