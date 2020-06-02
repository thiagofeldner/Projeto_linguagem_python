a = int(input('Primeiro bimestre: '))
if a  > 10:
    a = int(input('Voçê digitou errado. Primeiro Bimestre: '))
b = int(input('Segundo bimestre: '))
if b  > 10:
    b = int(input('Voçê digitou errado. Segundo Bimestre: '))
c = int(input('Terceiro bimestre: '))
if c  > 10:
    c = int(input('Voçê digitou errado. Terceiro Bimestre: '))
d = int(input('Quarto bimestre: '))
if d  > 10:
    d = int(input('Voçê digitou errado. Quarto Bimestre: '))
media = (a + b + c + d) / 4
print('Média: {}'.format(media))


a = int(input('Entre com o primeir valor: '))
b = int(input('Entre com o segundo valor: '))
resto_a = a % 2
resto_b = b % 2

if resto_a == 0 or not resto_b > 0:
    print('Foi digitado um número par!!')
else:
    print('Nenhum número e par!!')

a = int(input('Primeiro Valor: '))
b = int(input('Segundo Valor: '))
c = int(input('Terceiro Valor: '))

if a > b and a > c:
    print('O maior número é {}'.format(a))
elif b > a and b > c:
    print('O maior número é: {}'.format(b))
else:
    print('O maior número é: {}'.format(c))

print('Final do programa')


