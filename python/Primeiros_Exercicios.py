print("\nEXERCICIO 1")
print ("Olá!")
print ("Meu nome é Renata")
print ("Estou aprendendo Python")

print("\nEXERCICIO 2")
print ("Senac", "TIA", "Python é legal", sep= (" | "))

print("\nEXERCICIO 3")
print ("04", "09", "2026", sep="/")

print("\nEXERCICIO 4")
print ("Python", end=" ")
print ("é", end=" ")
print ("muito legal!")

print("\nEXERCICIO 5")
nome = "Renata"
idade = 25
cidade = "São Leopoldo"
curso = "TIA"
print (nome, idade, cidade, curso)

print("\nEXERCICIO 6")
nome= "Renata"
idade= 25
altura= 1.48
matriculado = "sim"
print(type(nome))
print(type(idade))
print(type(altura))
print(type(matriculado))

print("\nEXERCICIO 7")
nome = "Renata"
classe = "Ninja"
nivel = 8
possui_equipamento = "sim"
print("Nome:",nome)
print("Nome:",classe)
print("Nome:",nivel)
print("Nome:",possui_equipamento)

print("\nEXERCICIO 8")
nome = input("Qual é o seu nome? ")
cidade = input("Qual é a sua cidade? ")
jogo = input("Qual é o seu jogo favorito? ")
print (f"\nOlá, {nome}! Você mora em {cidade} e o seu jogo favorito é {jogo}.")

print("\nEXERCICIO 9")
nome = input("Nome do aluno: ")
curso = input("Nome do curso: ")
unidade = input("Unidade: ")
turno = input("Turno: ")
print(f"Aluno: {nome}", end = "\n")
print(f"Curso: {curso}", end = "\n")
print(f"Unidade: {unidade}", end = "\n")
print(f"Turno: {turno}")

print("\nDESAFIO - FICHA DE AVENTUREIRO")
nome = input("Nome do personagem: ")
raca = input("Raça: ")
classe = input("Classe: ")
local = input("Local de origem: ")
arma = input("Arma principal: ")
print("=========================================")
print("          FICHA DO AVENTUREIRO")
print("=========================================")
print(f"\nNome: {nome}")
print(f"Raça: {raca}")
print(f"Classe: {classe}")
print(f"Origem: {local}")
print(f"Arma: {arma}")
print()
print("=========================================")


print("\nDESAFIO EXTRA")
nome = input("\nDigite seu nome: ")
personagem = input("Digite o nome do personagem: ")
classe = input("Digite sua classe: ")

print("\n=========================================")
print("       AS CRÔNICAS DA TERRA MÉDIA")
print("=========================================")
print(f"\nBem-vindo, {nome}!")
print(f"\nSeu personagem é {personagem}.")
print(f"Classe escolhida: {classe}")
print("\nA aventura está prestes a começar", end = "...")