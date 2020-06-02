
lista = [1, 10]

try:
    arquivo = open('Notas.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]
except ZeroDivisionError:
    print('Não é possível realizar divisão por zero(0)')
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritmética')
except IndexError:
    print('Erro ao acessao um índice inválido da lista!!!')
except Exception as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print("Executa quando não ocorre exceção!")
finally:
    print('Sempre executa')
    print('fechando arquivo')
    arquivo.close()


