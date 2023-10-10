year = int(input('Введите год: '))
def vis(year):
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        print('Да')
    else:
        print('Нет')
        return
c = vis(year)
print(c)