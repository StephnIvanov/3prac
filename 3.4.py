seconds = int(input('Введите колличество секунд '))
day = seconds // (3600*24)
hours = seconds // 3600
minutes = seconds // 60 
second = seconds % 60
print(day,hours,minutes,second)