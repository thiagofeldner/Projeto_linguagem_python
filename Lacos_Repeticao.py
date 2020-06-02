
a = int(input('Primeiro bimestre: '))
while a  > 10:
    a = int(input('Voçê digitou errado. Primeiro Bimestre: '))
b = int(input('Segundo bimestre: '))
while b  > 10:
    b = int(input('Voçê digitou errado. Segundo Bimestre: '))
c = int(input('Terceiro bimestre: '))
while c  > 10:
    c = int(input('Voçê digitou errado. Terceiro Bimestre: '))
d = int(input('Quarto bimestre: '))
while d  > 10:
    d = int(input('Voçê digitou errado. Quarto Bimestre: '))
media = (a + b + c + d) / 4
print('Média: {}'.format(media))


a = int(input('Entre com um valor: '))
for num in range(a+1):
    div = 0
    for x in range (1, num+1):
        resto = num % x
       # print(x, resto)
        if resto == 0:
            div += 1
    if div == 2:
        print(num)


# a = int(input('Digite um número: '))
#
# div = 0
# for x in range (1, a + 1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print('Número {} é Primo!!'.format(a))
# else:
#     print('Número {} não é Primo'.format(a))

