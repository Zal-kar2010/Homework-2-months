# time = input('введите время суток:').lower()
#
# if time == 'morning'or time == 'утро':
#     print('good morning')
# elif time == 'day' or time == 'день':
#     print('good afternoon')
# elif time == 'evening' or time == 'вечер':
#     print('good evening')
# else:
#     print('Error!😭😭😭')

temp = int(input('Enter temp:'))
if temp >= -30 and temp <= 0:
    print('cold')
elif temp >= 1 and temp <= 15:
    print('cool')
elif temp >= 16 and temp <= 25:
    print('warm')
elif temp >= 26 and temp <= 40:
    print('heat')
else:
    print('СИДЕТЬ ДОМА !!!')