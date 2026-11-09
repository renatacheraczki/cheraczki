print ("""
EXERCÍCIO 1: Simulação de Treinamento
       """)
for epoca in range(1,11):
    print (f"Treinando {epoca}")

print("""
EXERCÍCIO 2: Dados de Sensores
      """)
temperaturas = [22.5,24.8,27.1,23.9,26.5]
for temperatura in temperaturas:
    print(f"Temperatura registrada: {temperatura}ºC")

print("""
EXERCÍCIO 3: Detectando Temperaturas Altas
    """)
temperaturas = [22, 25, 31, 28, 35, 24]
for temperatura in temperaturas:  
    if temperatura > 30:
        print(f"Temperatura registrada: {temperatura} -> ALERTA: temperatura elevada!")
    else:
        print(f"Temperatura registrada: {temperatura}ºC")

print("""
EXERCÍCIO 4: Classificação de Confiança
      """)
confiancas = [0.95,0.65,0.34,0.82,0.71]
for confianca in confiancas:
    if confianca >= 0.8:
        print(f"{confianca} -> Alta confiança")
    elif confianca >= 0.5 and confianca <= 0.79:
        print(f"{confianca} -> Confiança média")
    else:
        print(f"{confianca} -> Baixa confiança")

print("""
EXERCICÍ0 5: Contando Classificações
      """)
previsoes = [
    "gato",
    "cachorro",
    "gato",
    "pássaro",
    "gato",
    "cachorro"
]
gatos = 0
for previsao in previsoes:
    if previsao == "gato":
        gatos += 1
print(f"Gatos detectados: {gatos}")

print("""
EXERCÍCIO 6: Média dos Dados
      """)
dados = [10,15,20,25,30]
print(f"Dados: {dados}")
soma = 0
for dado in dados:
    soma += dado
media = soma / len(dados)
print(f"Soma dos dados: {media}")

print("""
EXERCÍCIO 7: Processamento de Texto
      """)
frase = "Inteligencia Artificial"
quantidade = 0
for letra in frase:
    if letra.upper() == "A":
        quantidade += 1
print(f"Quantidade de letras 'a': {quantidade}")

print("""
EXERCÍCIO 8: Ignorando Dados Inválidos
      """)
dados = [12,15,None,18,None,21]
print(f"Dados:{dados}")
for dado in dados:
    if dado is None:
        continue
    print(dado)

print("""
DESAFIO - ANALISANDO PREVISÕES:
      """)
previsoes = [
    0.92,
    0.84,
    0.35,
    0.76,
    0.28,
    0.95
]

print("""
DESAFIO - MATRIZ DE PIXELS
      """)
imagem = [
    [0,255,0],
    [255,255,0],
    [0,0,255]
]
for linha in imagem:
    for pixel in linha:
        print(pixel, end= " ")
    print()

print("""
DESAFIO - CONTADOR DE CLASSES:
      """)
previsoes = [
    "gato",
    "cachorro",
    "gato",
    "gato",
    "cachorro",
    "pássaro",
    "gato",
]
gatos = 0
for previsao in previsoes:
    if previsao == "gato":
        gatos += 1
print(f"Gatos: {gatos}")
cachorro = 0
for previsao in previsoes:
    if previsao == "cachorro":
        cachorro += 1
print(f"Cachorros: {cachorro}")
pássaro = 0
for previsao in previsoes:
    if previsao == "pássaro":
        pássaro += 1
print(f"Pássaros: {pássaro}")

print("""
DESAFIO - SISTEMA SIMPLES DE DETECÇÃO
      """)
objetos = [
    "pessoa",
    "carro",
    "pessoa",
    "bicicleta",
    "carro",
    "pessoa"
]
pessoa = 0
for objeto in objetos:
    print(f"Objeto detectado: {objeto}")
    if objeto == "pessoa":
        pessoa += 1
print()
print (f"Total de pessoas detectadas: {pessoa}")
