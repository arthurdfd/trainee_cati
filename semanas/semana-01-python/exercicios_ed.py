# ## 📌 Tópico 1: Listas
# 
# Este tópico aborda criação, acesso, manipulação, iteração e listas aninhadas.
# 
# ---

# ### Exercício 1.1 - Criando e Acessando Listas
# 
# Crie uma lista chamada `frutas` com os seguintes elementos: 'maçã', 'banana', 'laranja', 'uva', 'morango'.
# 
# Em seguida:
# 1. Exiba o primeiro elemento usando índice positivo
# 2. Exiba o último elemento usando índice negativo
# 3. Exiba o terceiro elemento usando índice positivo
# 4. Verifique se 'banana' está na lista usando o operador `in`
# 5. Modifique o segundo elemento para 'abacaxi'
# 
# **Saída esperada** (após todas as operações):
# ```
# Primeiro elemento: maçã
# Último elemento: morango
# Terceiro elemento: laranja
# banana está na lista: True
# Lista após modificação: ['maçã', 'abacaxi', 'laranja', 'uva', 'morango']

frutas = ['maçã', 'banana', 'laranja', 'uva', 'morango']
print(f'Primeiro elemento: {frutas[0]}')
print(f'Último elemento: {frutas[-1]}')
print(f'Terceiro elemento: {frutas[2]}')
print(f"banana está na lista: {'banana' in frutas}")
frutas[1] = 'abacaxi'
print(f'Lista após modificação: {frutas}')

# ### Exercício 1.2 - Manipulando Listas com Métodos
# 
# Você tem uma lista inicial de compras: `['arroz', 'feijão', 'macarrão']`
# 
# Realize as seguintes operações:
# 1. Adicione 'açúcar' ao final da lista usando `append()`
# 2. Insira 'óleo' na posição 1 usando `insert()`
# 3. Crie outra lista `outros_itens = ['sal', 'pimenta']` e adicione todos os elementos à lista principal usando `extend()`
# 4. Remova 'macarrão' usando `remove()`
# 5. Remova o último elemento usando `pop()` e armazene em uma variável
# 6. Exiba o tamanho da lista usando `len()`
# 
# **Saída esperada** (após todas as operações):
# ```
# Lista final: ['arroz', 'óleo', 'feijão', 'açúcar', 'sal', 'pimenta']
# Item removido com pop: pimenta
# Tamanho da lista: 5

compras = ['arroz', 'feijão', 'macarrão']
compras.append('açúcar')
compras.insert(1, 'óleo')
outros_itens = ['sal', 'pimenta']
compras.extend(outros_itens)
compras.remove('macarrão')
print(f'Lista final: {compras}')
removido = compras.pop()
print(f'Item removido com pop: {removido}')
print(f'Tamanho da lista: {len(compras)}')

# ### Exercício 1.3 - Percorrendo e Fatiando Listas
# 
# Dada a lista: `notas = [7.5, 8.0, 6.5, 9.0, 7.0, 8.5, 6.0, 9.5]`
# 
# Realize as seguintes tarefas:
# 1. Percorra a lista usando `for item in lista` e exiba cada nota
# 2. Percorra a lista usando `for x in range(len(lista))` e exiba cada nota com seu índice
# 3. Use fatiamento para obter os 3 primeiros elementos
# 4. Use fatiamento para obter os 3 últimos elementos
# 5. Use fatiamento com passo para obter elementos de 2 em 2 (índices pares)
# 6. Use fatiamento reverso para inverter a lista
# 
# **Saída esperada** (exemplos):
# ```
# Nota: 7.5
# Nota: 8.0
# ...
# Índice 0: 7.5
# Índice 1: 8.0
# ...
# 3 primeiros: [7.5, 8.0, 6.5]
# 3 últimos: [6.0, 8.5, 9.5]
# Elementos de 2 em 2: [7.5, 6.5, 7.0, 6.0]
# Lista invertida: [9.5, 6.0, 8.5, 7.0, 9.0, 6.5, 8.0, 7.5]

notas = [7.5, 8.0, 6.5, 9.0, 7.0, 8.5, 6.0, 9.5]
for item in notas:
    print('Nota:', item)
for x in range(len(notas)):
    print(f'Índice {x}: {notas[x]}')
print(f'3 primeiros: {notas[3:]}')
print(f'3 últimos: {notas[-3:]}')
print(f'Elementos de 2 em 2: {notas[0:-1:2]}')
print(f'Lista invertida: {notas[-1::-1]}')

# ### Exercício 1.4 - Trabalhando com Listas Aninhadas
# 
# Crie uma lista aninhada chamada `alunos` que representa uma turma com as seguintes informações:
# ```python
# alunos = [
#     ['Nome', 'Idade', 'Nota'],
#     ['Ana', 20, 8.5],
#     ['Bruno', 19, 7.0],
#     ['Carla', 21, 9.0],
#     ['Diego', 20, 6.5]
# ]
# ```
# 
# Realize as seguintes operações:
# 1. Acesse e exiba a idade de Bruno (usando índices)
# 2. Acesse e exiba a nota de Carla usando índices negativos
# 3. Modifique a nota de Diego para 7.5
# 4. Percorra a lista aninhada usando laços aninhados e exiba todos os dados formatados
# 5. Percorra apenas os dados dos alunos (pule o cabeçalho) e exiba: "[Nome] tem [Idade] anos e nota [Nota]"
# 6. Adicione um novo aluno: ['Elena', 22, 8.0] à lista
# 
# **Saída esperada** (exemplos):
# ```
# Idade de Bruno: 19
# Nota de Carla: 9.0
# Ana tem 20 anos e nota 8.5
# Bruno tem 19 anos e nota 7.0

alunos = [
    ['Nome', 'Idade', 'Nota'],
    ['Ana', 20, 8.5],
    ['Bruno', 19, 7.0],
    ['Carla', 21, 9.0],
    ['Diego', 20, 6.5]
]

print(f'Idade de Bruno: {alunos[2][1]}') #1.
print(f'Nota de Carla: {alunos[-2][-1]}') #2.
alunos[-1][-1] = 7.5 #3.
for lista in alunos: #4.
    for dados in lista:
        print(dados)
for dados in alunos[1:]: #5.
    nome, idade, nota = dados
    print(f'{nome} tem {idade} anos e nota {nota}')
alunos.append(['Elena', 22, 8.0]) #6.


# ## 📌 Tópico 2: Tuplas
# 
# Este tópico aborda criação, acesso, imutabilidade, conversão e operações com tuplas.
# 
# ---

# ### Exercício 2.1 - Criando e Acessando Tuplas
# 
# Crie uma tupla chamada `coordenadas` com os valores: (10, 20, 30)
# 
# Realize as seguintes operações:
# 1. Exiba a tupla completa
# 2. Verifique o tipo da variável usando `type()`
# 3. Acesse e exiba o primeiro elemento usando índice positivo
# 4. Acesse e exiba o último elemento usando índice negativo
# 5. Verifique se o valor 20 está na tupla usando `in`
# 6. Exiba o tamanho da tupla usando `len()`
# 
# **Saída esperada**:
# ```
# Tupla: (10, 20, 30)
# Tipo: <class 'tuple'>
# Primeiro elemento: 10
# Último elemento: 30
# 20 está na tupla: True
# Tamanho: 3

coordenadas = (10, 20, 30) 

print(f'Tupla: {coordenadas}') #1.
print(f'Tipo: {type(coordenadas)}') #2.
print(f"Primeiro elemento: {coordenadas[0]}") #3.
print(f'Último elemento: {coordenadas[-1]}') #4.
print(f'20 está na tupla: {20 in coordenadas}') #5.
print(f'Tamanho: {len(coordenadas)}') #6.

# ---

# ### Exercício 2.2 - Modificando Tuplas e Desempacotamento
# 
# Você tem uma tupla: `cores = ('vermelho', 'azul', 'verde', 'amarelo')`
# 
# Realize as seguintes operações:
# 1. Tente modificar diretamente o primeiro elemento (isso deve gerar um erro - comente o código após testar)
# 2. Converta a tupla para lista, modifique o segundo elemento para 'roxo', e converta de volta para tupla
# 3. Desempacote a tupla original em 4 variáveis: `cor1, cor2, cor3, cor4`
# 4. Crie uma nova tupla com mais elementos: `cores_extras = ('laranja', 'rosa', 'preto', 'branco', 'cinza')`
# 5. Desempacote `cores_extras` usando `*` para capturar os elementos restantes: `(c1, c2, *resto)`
# 
# **Saída esperada** (após modificação):
# ```
# Tupla modificada: ('vermelho', 'roxo', 'verde', 'amarelo')
# Desempacotamento: cor1=vermelho, cor2=azul, cor3=verde, cor4=amarelo
# Desempacotamento com *: c1=laranja, c2=rosa, resto=['preto', 'branco', 'cinza']

cores = ('vermelho', 'azul', 'verde', 'amarelo')

#1. Código para demonstrar a imutabilidade de uma tupla. 'cores[0] = 'prata''

cores_lista = list(cores)
cores_lista[1] = 'roxo'
cores = tuple(cores_lista)
print(f'Tupla modificada: {cores}')
(cor1, cor2, cor3, cor4) = cores
print(f'Desempacotamento: cor1={cor1}, cor2={cor2}, cor3={cor3}, cor4={cor4}')
cores_extras = ('laranja', 'rosa', 'preto', 'branco', 'cinza')
(c1, c2, *resto) = cores_extras
print(f'Desempacotamento com *: c1={c1}, c2={c2}, resto={resto}')



# ---

# ### Exercício 2.3 - Operações com Tuplas
# 
# Você tem duas tuplas:
# - `frutas1 = ('maçã', 'banana', 'laranja')`
# - `frutas2 = ('uva', 'morango', 'abacaxi', 'kiwi')`
# 
# Realize as seguintes operações:
# 1. Concatene as duas tuplas usando o operador `+` e armazene em `todas_frutas`
# 2. Percorra a tupla `todas_frutas` usando `for` e exiba cada fruta
# 3. Crie uma tupla com elementos duplicados: `numeros = (1, 2, 3, 2, 4, 2, 5)`
# 4. Use `count()` para contar quantas vezes o número 2 aparece
# 5. Use `index()` para encontrar a posição (índice) do primeiro 'abacaxi' em `todas_frutas`
# 6. Verifique o tamanho de `todas_frutas` usando `len()`
# 
# **Saída esperada**:
# ```
# Tupla concatenada: ('maçã', 'banana', 'laranja', 'uva', 'morango', 'abacaxi', 'kiwi')
# Frutas na tupla:
# maçã
# banana
# ...
# Quantidade de 2: 3
# Índice de 'abacaxi': 5
# Tamanho: 7

frutas1 = ('maçã', 'banana', 'laranja')
frutas2 = ('uva', 'morango', 'abacaxi', 'kiwi')

todas_frutas = frutas1 + frutas2
print(f'Tupla concatenada: {todas_frutas}')
numeros = (1, 2, 3, 2, 4, 2, 5)
print(f'Quantindade de 2: {numeros.count(2)}')
print(f"Índice de 'abacaxi': {todas_frutas.index('abacaxi')}")
print(f'Tamanho: {len(todas_frutas)}')

# ---

# ## 📌 Tópico 3: Dicionários
# 
# Este tópico aborda criação, acesso, manipulação, iteração e dicionários aninhados.
# 
# ---

# ### Exercício 3.1 - Criando e Acessando Dicionários
# 
# Crie um dicionário chamado `pessoa` com as seguintes informações:
# - nome: 'Maria Silva'
# - idade: 28
# - altura: 1.65
# - habilitado: True
# 
# Realize as seguintes operações:
# 1. Exiba o dicionário completo
# 2. Verifique o tipo usando `type()`
# 3. Acesse e exiba cada valor individualmente usando colchetes
# 4. Modifique a idade para 29
# 5. Adicione uma nova chave 'cidade' com valor 'São Paulo'
# 6. Exiba o tamanho do dicionário usando `len()`
# 
# **Saída esperada** (após modificações):
# ```
# Dicionário: {'nome': 'Maria Silva', 'idade': 29, 'altura': 1.65, 'habilitado': True, 'cidade': 'São Paulo'}
# Tipo: <class 'dict'>
# Nome: Maria Silva
# Idade: 29
# Altura: 1.65
# Habilitado: True
# Cidade: São Paulo
# Tamanho: 5

pessoa = {
    'nome' : 'Maria da Silva',
    'idade' : 28, 
    'altura' : 1.65,
    'habilitado' : True
}

print(f'Dicionário: {pessoa}')
print(f'Tipo: {type(pessoa)}')
print(f'Nome: {pessoa['nome']}')
print(f'Idade: {pessoa['idade']}')
print(f'Altura: {pessoa['altura']}')
print(f'Habilitado: {pessoa['habilitado']}')
pessoa['idade'] = 29
pessoa['cidade'] = 'São Paulo'
print(f'Cidade: {pessoa['cidade']}')
print(f'Tamanho: {len(pessoa)}')

# ---

# ### Exercício 3.2 - Manipulando Dicionários
# 
# Você tem um dicionário inicial:
# ```python
# produto = {
#     'nome': 'Notebook',
#     'preco': 2500.00,
#     'estoque': 10
# }
# ```
# 
# Realize as seguintes operações:
# 1. Use `get('preco')` para acessar o preço (método seguro)
# 2. Use `get('desconto')` para tentar acessar uma chave que não existe (deve retornar None)
# 3. Verifique se 'estoque' existe no dicionário usando `in`
# 4. Use `update()` para atualizar o preço para 2200.00 e adicionar 'categoria': 'Eletrônicos'
# 5. Use `pop('estoque')` para remover e retornar o valor de estoque
# 6. Use `popitem()` para remover o último item inserido
# 
# **Saída esperada** (após operações):
# ```
# Preço (get): 2500.0
# Desconto (get): None
# 'estoque' existe: True
# Estoque removido: 10
# Dicionário final: {'nome': 'Notebook', 'preco': 2200.0, 'categoria': 'Eletrônicos'}

produto = {
    'nome': 'Notebook',
    'preco': 2500.00,
    'estoque': 10
}

print(f'Preço (get): {produto.get('preco')}')
print(f'Desconto (get): {produto.get('desconto')}')
print(f"'estoque' existe: {'estoque' in produto}")
produto.update({'preco':2200.0})
produto.update({'categoria':'Eletronicos'})
print(f'Estoque removido: {produto.pop('estoque')}')
produto.popitem()
print(f'Dicionário final: {produto}')

# ---

# ### Exercício 3.4 - Trabalhando com Dicionários Aninhados
# 
# Crie um dicionário aninhado chamado `clientes` com a seguinte estrutura:
# ```python
# clientes = {
#     'cliente1': {
#         'nome': 'Ana Paula',
#         'idade': 32,
#         'email': 'ana@email.com',
#         'cidade': 'São Paulo'
#     },
#     'cliente2': {
#         'nome': 'Roberto Lima',
#         'idade': 45,
#         'email': 'roberto@email.com',
#         'cidade': 'Rio de Janeiro'
#     },
#     'cliente3': {
#         'nome': 'Mariana Rocha',
#         'idade': 28,
#         'email': 'mariana@email.com',
#         'cidade': 'Curitiba'
#     }
# }
# ```
# 
# Realize as seguintes operações:
# 1. Acesse e exiba a idade do cliente1 usando múltiplas chaves
# 2. Acesse e exiba o email do cliente2
# 3. Modifique a idade do cliente1 para 33
# 4. Adicione um novo cliente 'cliente4' com nome 'Diego Costa', idade 35, email 'diego@email.com' e cidade 'Belo Horizonte'
# 5. Percorra o dicionário aninhado usando laços aninhados e exiba todas as informações de cada cliente
# 6. Remova o cliente2 usando `del`
# 
# **Saída esperada** (exemplos):
# ```
# Idade do cliente1: 32
# Email do cliente2: roberto@email.com
# cliente1
#   nome: Ana Paula
#   idade: 33
#   email: ana@email.com
#   cidade: São Paulo

clientes = {
    'cliente1': {
        'nome': 'Ana Paula',
        'idade': 32,
        'email': 'ana@email.com',
        'cidade': 'São Paulo'
    },
    'cliente2': {
        'nome': 'Roberto Lima',
        'idade': 45,
        'email': 'roberto@email.com',
        'cidade': 'Rio de Janeiro'
    },
    'cliente3': {
        'nome': 'Mariana Rocha',
        'idade': 28,
        'email': 'mariana@email.com',
        'cidade': 'Curitiba'
    }
}

print(f'Idade do cliente1: {clientes['cliente1']['idade']}')
print(f'Email do cliente2: {clientes['cliente2']['email']}')
clientes['cliente1']['idade'] = 33
clientes['cliente4'] = {
    'nome':'Diego Costa', 
    'idade':35, 
    'email':'diego@email.com',
    'cidade':'Belo Horizonte'
}
for chave, valor in clientes.items():
    print(chave)
    for chave2, valor2 in valor.items():
        print(f'{chave2}: {valor2}')
    print()
del clientes['cliente2']
print(f'Dicionário final: {clientes}')
# ---

# ## 📌 Tópico 4: Conjuntos
# 
# Este tópico aborda criação, manipulação e operações de teoria de conjuntos.

# ### Exercício 4.2 - Operações Básicas com Conjuntos
# 
# Você tem dois conjuntos:
# - `conjunto1 = {'a', 'b', 'c'}`
# - `conjunto2 = {'c', 'd', 'e'}`
# 
# Realize as seguintes operações:
# 1. Use `update()` para adicionar os elementos de `conjunto2` em `conjunto1`
# 2. Crie um novo conjunto `conjunto3 = {'f', 'g'}` e adicione usando `update()`
# 3. Remova 'a' usando `remove()`
# 4. Use `discard()` para tentar remover 'z' (que não existe)
# 5. Crie uma cópia de `conjunto1` usando `copy()`
# 6. Limpe o conjunto original usando `clear()` e verifique que a cópia não foi afetada
# 
# **Saída esperada** (após operações):
# ```
# Conjunto1 após update: {'b', 'c', 'd', 'e', 'f', 'g'}
# Conjunto1 após remoções: {'b', 'c', 'd', 'e', 'f', 'g'}
# Cópia: {'b', 'c', 'd', 'e', 'f', 'g'}
# Original após clear: set()
# Cópia (não afetada): {'b', 'c', 'd', 'e', 'f', 'g'}

conjunto1 = {'a', 'b', 'c'}
conjunto2 = {'c', 'd', 'e'}

conjunto1.update(conjunto2)
print(f'Conjunto1 após update: {conjunto1}')
conjunto3 = {'f', 'g'}
conjunto1.update(conjunto3)
conjunto1.remove('a')
print(f'Conjunto1 após remoções: {conjunto1}')
conjunto1.discard('z')
aux = conjunto1.copy()
print(f'Cópia: {aux}')
conjunto1.clear()
print(f'Conjunto1 após clear: {conjunto1}')
print(f'Cópia (não afetada): {aux}')