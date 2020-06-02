a = int(input('Entre com o primeiro valor:  '))
b = int(input('Entre com o segundo valor:  '))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

resultado = ('Soma: {soma} '
      '\nSubtracao: {sub} '
      '\nMultiplicacao: {mult}'
      '\nDivisao: {div}'
      '\nResto: {resto}'.format(soma=soma,
                                sub=subtracao,
                                mult=multiplicacao,
                                div=divisao,
                                resto=resto))
print(resultado)


