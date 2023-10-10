a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
def odinak(a,b,c):
    if a == b == c:
        print('3')
    elif a == b or b == c or a == c:
        print('2')
    else:
        print('3')
        return
c = odinak(a,b,c)
print(c)