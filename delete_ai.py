# deletar nomes em uma lista
# lista
cidades = ['gama', 'taguatinga', 'sobradinho', 'sudoeste']

# informar a posição do item a ser deletado
indice = int(input('informe a posição do item a ser deletado: '))

# evita que ousuario apague o ultimo item da lista caso indice = 0
if indice > 0:
    indice -= 1
else:
    indice = ''

# deleta item da lista
try:
    del(cidades[indice])
except:
    print('Não foi possível deletar. ')

# exibe a lista
for cidade in cidades:
    print(cidade)
