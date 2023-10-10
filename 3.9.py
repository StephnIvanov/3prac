n = int(input('Длина шоколадки) долек'))
m = int(input('Колличество (ширину шоколадки) долек'))
k = int(input('Должно остаться (отломить можно только пополам, по ширине)'))
def choko(n,m,k):
    if ((m // 2) * n) == k:
        print('Да')
    else:
        print('Нет')
        return
c = choko(n,m,k)
print(c)