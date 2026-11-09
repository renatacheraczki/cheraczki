print ("""
Exercício 1 — Contagem Regressiva
       """)

numero = int(input("Digite um número: "))
print()

while numero >= 0:
    print(numero)
    numero -= 1

print ("""
Exercício 2 — Validação de Preço
       """)

while True:
    preco = float(input("Informe o preço do produto: "))
    if preco > 0:
        break
    print("Preço inválido! Informe o preço novamente: ")
    
print("Produto cadastrado com sucesso.")

print ("""
Exercício 3 — Lista de Jogos
       """)
jogos = [
    "Minecraft",
    "Terraria",
    "Stardew Valley"
]
print(jogos)
print("Agora, liste dois jogos que não estão na lista: ")

jogo1 = input("Jogo 1: ")
jogo2 = input("Jogo 2: ")

jogos.append(jogo1)
jogos.append(jogo2)

print("Lista atualizada: ")
print(jogos)
quantidade = len(jogos)
print("Quantidade de jogos:" , quantidade)
print("Primeiro jogo: ", (jogos[0]))
print("Último jogo: ", (jogos[-1]))


print ("""
Exercício 4 — Controle de Estoque
       """)
print("Cadastre os produtos para o estoque, e quando acabar, digite fim: ")
produtos = []

while True:
    produto = input("Produto: ")
    if produto == "fim":
        break
    produtos.append(produto)
    print("Produtos em estoque: ", produtos)

print("Listagem encerrada.")

print ("""
Exercício 5 — Estatísticas de Notas
       """)
notas = [7.5, 8.0, 5.5, 9.0, 6.5, 10.0]
quantidade = len(notas)
soma = sum(notas)
media = soma / quantidade
maior = max(notas)
menor = min(notas)
print(notas)
print()
print("Quantidade de notas: ", quantidade)
print("Soma das notas: ", soma)
print("Média das notas: ", media)
print("Maior nota: ", maior)
print("Menor nota: ", menor)

print ("""
Exercício 6 — Busca em Lista
       """)

usuarios = [
    "admin",
    "maria",
    "joao",
    "pedro"
]

nome = input("Digite o nome de usuário: ")

indice = 0

while indice < len(usuarios): # enquanto indice for menor que a quantidade 4
    if nome == usuarios[indice]: # se o nome == indice (aqui ele converte o indice em string e compara com o nome preenchido)
        print("Usuário encontrado.")
        break # se nome == a um dos usuários da lista, ele para.

    indice += 1 # se o nome não for igual ao dos usuários da lista, ele prossegue com o while, soma 1 ao indice até que encontre o usuário na lista, ou encontre indice igual a 4 (considerando que tenho indices de 0 a 3))

if indice == len(usuarios): # se indice for igual a 4:
    print("Usuário não encontrado.") # exibe Usuário não encontrado


print("""
Exercício 7 — Carrinho de Compras""")

produtos = []
precos = []

while True:
    produto = input("Produto: ")
    if produto == "sair":
        break
    preco = float(input("Preço: "))
    produtos.append(produto)
    precos.append(preco)
    print(produtos)
    print(precos)

quantidade = len(produtos)
total = sum(precos)
barato = min(precos)
caro = max(precos)

print("Quantidade de produtos: ", quantidade)
print("Valor total da compra: ", total)
print("Produto mais barato: ", barato)
print("Produto mais caro: ", caro)

print("""
# Exercício 8 — Sistema de Tarefas""")

menu = [
    "1 - Adicionar tarefa",
    "2 - Listar tarefas",
    "3 - Remover tarefa",
    "4 - Mostrar quantidade de tarefas",
    "0 - Sair"
]

for i in menu:
    print (i)

tarefas = []

while True:
    opcao = input("Escolha uma opção: ")
    if opcao == "0":
        break
    elif opcao == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso.")
    elif opcao == "2":
        for tarefa in tarefas:
            print(tarefa)
    elif opcao == "3":
        remover = input("Escolha a tarefa que deseja remover: ")
        tarefas.remove(remover)
        print("Tarefa removida.")
    else:
        quantidade = len(tarefas)
        print("Quantidade de tarefas:", quantidade)