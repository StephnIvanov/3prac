n = int(input("Введите сколько прошло минут с начала суток:"))
ch = (n // 60) % 24
minutes = n % 60
if n > 1440:
    print('Error')
else:
    print(ch,':',minutes)