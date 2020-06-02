conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2)
print('Uniao: {}'.format(conjunto_uniao))
conjunto_interseccao = conjunto.intersection(conjunto2)
print('Intersecção: {}'.format(conjunto_interseccao))
conj_dif = conjunto.difference(conjunto2)
conj_dif2 = conjunto2.difference(conjunto)
print('Diferença entre 1 e 2: {}'.format(conj_dif))
print('Diferença entre 2 e 1: {}'.format(conj_dif2))
conj_dif_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença Simétrica: {}'.format(conj_dif_simetrica))

conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}
conj_subset = conjunto_a.issubset(conjunto_b)
print('A é subconjunto de B: {}'.format(conj_subset))
conj_superset = conjunto_b.issuperset(conjunto_a)
print('B é um superconjunto de A: {}'.format(conj_superset))
lista = ['cachorro','cachorro', 'gato','gato','elefante']
print(lista)
conj_animais = set(lista)
print(conj_animais)
lista_animais = list(conj_animais)
print(lista_animais)


# conjunto = {1, 2, 3, 4, 4, 2}
# conjunto.add(5)
# conjunto.discard(2)
# print(conjunto)

conjunto = {10, 20, 30, 40, 50}
conjunto.discard (40)
print(conjunto)