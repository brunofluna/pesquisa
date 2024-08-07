# lista de cidades para pesquisar 
cidades = ['Brasília', 'Taguatinga', 'Planaltina', 'Ceilândia', 'Samambaia', 'Riacho fundo', 'Candangolândia', 'Núcleo bandeirante', 'Gama', 'Santa maria', 'Sobradinho', 'Planaltina', 'Recanto das emas', 'Guará', 'Valparaiso', 'Novo gama', 'Céu azul', 'Lago azul', 'Formosa', 'Sol nascente', 'Estrutural', 'Águas claras', 'Arniqueira', 'Areal', 'Sol nascente', 'Dvo', 'São Sebastião', 'Dvo']

# usuário informa valor a ser pesquisado
cidade_pesquisa = input('Informe o nome da cidade a ser pesquisada: ').capitalize()
# verifica se a cidade existe
if cidade_pesquisa in cidades:
    print(f'\nCidade {cidade_pesquisa} achada com sucesso!\n')
else:
    print('Não Localizada!!!')
