"""#EXERCICIO 1
idade = float(input("Digite sua idade: "))

if idade <= 12:
    print("Criança")
elif idade >= 13 and idade <= 17:
    print("Adolescente")
elif idade >= 18 and idade <= 59:
    print("Adulto")
else:
    print("Idoso", end = "\n")

#EXERCICIO 2
l1 = float(input("Primeiro lado: "))
l2 = float(input("Segundo lado: "))
l3 = float(input("Terceiro lado: "))

if l1 == l2 and l1 == l3:
    print("Equilátero")
elif l1 == l2 or l1 == l3 or l2 == l3:
    print("Isósceles")
else:
    print("Escaleno")

#EXERCICIO 3
valor_original = float(input("Valor da compra: "))
print(f"Valor original: {valor_original}")
if valor_original <= 100:
    print("Desconto: sem desconto")
elif valor_original > 100 and valor_original <= 300:
    valor_desconto = round(valor_original*5/100,2)
    valor_final = round(valor_original - valor_desconto,2)
    print("Desconto: 5%")
    print(f"Valor do desconto: {valor_desconto}")
    print(f"Valor final: {valor_final}")
elif valor_original > 300 and valor_original <= 500:
    valor_desconto = round(valor_original*10/100,2)
    valor_final = round(valor_original - valor_desconto,2)
    print("Desconto: 10%")
    print(f"Valor do desconto: {valor_desconto}")
    print(f"Valor final: {valor_final}")
elif valor_original > 500:
    valor_desconto = round(valor_original*15/100,2)
    valor_final = round(valor_original - valor_desconto,2)
    print("Desconto: 15%")
    print(f"Valor do desconto: {valor_desconto}")
    print(f"Valor final: {valor_final}")

#EXERCICIO 4
nota = float(input("Digite sua nota: "))
frequencia = float(input("Digite sua frequência: "))
if frequencia < 75:
    print("Reprovado por frequência")
elif nota >= 7:
    print("Aprovado")
elif nota >= 5 and nota < 7:
    print("Recuperação")
else:
    print("Reprovado")

#EXERCICIO 5
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura**2)
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc > 18.5 and imc <= 25:
    print("Classificação: Peso normal")
elif imc > 25 and imc <= 30:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")

#EXERCICIO 6
numero = float(input("Digite um número: "))
if numero % 2 == 0:
    print("Número par")
else:
    print("Número ímpar")

#EXERCICIO 7
nivel = float(input("Digitel seu nível: "))
espada = str(input("Possui espada? "))
cajado = str(input("Possui cajado? "))
espada = espada.upper()
cajado = cajado.upper()
if nivel >= 10 and (espada == "SIM" or cajado == "SIM"):
    print("Apto para jogar")
else:
    print("Jogador inapto")"""

#DESAFIO - PEDRA, PAPEL OU TESOURA
import random
computador = random.randint(0,2)
print("0 = Pedra")
print("1 = Papel")
print("2 = Tesoura")
jogador = int(input("Sua vez: "))
print(f"Computador: {computador}")

if computador == 0 and jogador == 1 or computador == 2 and jogador == 0 or computador == 1 and jogador == 2:
    print("Você ganhou!")
elif computador == 1 and jogador == 0 or computador == 0 and jogador == 2 or computador == 2 and jogador == 1:
    print("Você perdeu.")
else:
    print("Empatou")

#DESAFIO EXTRA - SISTEMA DE LOGIN
usuario_correto = input("Usuário: ")
senha_correta = input("Senha: ")
if usuario_correto == "admin" and senha_correta == "1234":
    print ("Login realizado com sucesso")
elif usuario_correto != "admin" and senha_correta == "1234":
    print ("Usuário incorreto")
elif usuario_correto == "admin" and senha_correta != "1234":
    print ("Senha incorreta")
else:
    print ("Usuário e Senha incorretos")

