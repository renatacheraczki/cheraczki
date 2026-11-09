# print("""
# Exercício 1 — Dias da Semana
#       """)
# print ("""
# Dias da Semana:
#   1 - Segunda-feira
#   2 - Terça-feira
#   3 - Quarta-feira
#   4 - Quinta-feira
#   5 - Sexta-feira
#   6 - Sábado
#   7 - Domingo
#            """)       

# dia = input("Escolha um dia da semana:").strip()

# match dia:
#     case "1":
#         print("Segunda-feira")
#     case "2":
#         print("Terça-feira")
#     case "3":
#         print("Quarta-feira")
#     case "4":
#         print("Quinta-feira")
#     case "5":
#         print("Sexta-feira")
#     case "6":
#         print("Sábado")
#     case "7":
#         print("Domingo")
#     case _:
#         print("Dia inválido.")

# print("""
# Exercício 2 — Comandos de um Assistente
#       """)

# comando = input("Escolha uma opção: ").strip().lower()

# match comando:
#     case "oi" | "olá":
#         print("Eaí, tudo certo?!")
#     case "ajuda" | "?":
#         print("Confira os comandos disponíveis: oi, olá, ajuda, ?, sair, 0")
#     case "sair" | "0":
#         print("Até a próxima!")
#     case _:
#         print("Comando desconhecido.")

# print("""
# Exercício 3 — Menu de Estudos
#       """)

# while True:
#     print("""
# 1 - Mostrar uma dica sobre Python
# 2 - Mostrar uma dica sobre inteligência artificial
# 3 - Mostrar uma mensagem de incentivo
# 0 - Sair
#           """)
#     opcao = input("Escolha uma opção: ").strip()

#     match opcao:
#         case "1":
#             print("Para aplicar comentários em um grupo de código, execute Ctrl + ;")
#         case "2":
#             print("Trate a IA como um estagiário. Faça perguntas sobre como a IA executaria a demanda, antes de executá-la.")
#         case "3":
#             print("Não desista.")
#         case "0":
#             print("Encerrando o programa...")
#             break
#         case _:
#             print("Opção inválida.")

print("""
Exercício 4 — Cadastro de Alunos"""
      )
alunos = []
while True:
    print("""
1 - Cadastrar aluno
2 - Listar alunos
3 - Mostrar quantidade de alunos
0 - Sair
          """)
    opcao = int(input("Escolha uma opção: ").strip())
    cont_alunos = 0
    match opcao:
        case 1:
            cadastro = input("Informe o nome do aluno: ").strip().lower()
            if cadastro == "":
                print("Informe um nome válido.")
            else:
                alunos.append(cadastro)
                print("Aluno cadastrado com sucesso.")
        case 2:
            if len(alunos) == 0:
                print("Nenhum aluno cadastrado.")
            else:
                print("Alunos cadastrados:")
                for aluno in alunos:
                    print(f" - {alunos}")
        case 3:
            print(f"Quantidade de alunos: {len(alunos)}")
        case 0:
            print("Encerrando sistema...")
            break
        case _:


    

# print("""
# Desafio — Central de Análise de Previsões
#       """)

# previsoes = []

# while True:
#     print("""
#     1 - Adicionar classificação
#     2 - Listar classificações
#     3 - Mostrar quantidade de gatos
#     4 - Mostrar quantidade de cachorros
#     5 - Mostrar total de classificações
#     0 - Sair
#           """)
#     opcao = int(input("Selecione uma opção: ").strip())
#     cont_gatos = 0
#     cont_cachorros = 0
#     match opcao:
#         case 1:
#             animal = input("Digite o animal que deseja adicionar [gato, cachorro, pássaro]: ").strip().lower()
#             match animal:
#                 case "gato" | "cachorro" | "pássado":
#                     previsoes.append(animal)
#                 case _:
#                     print("Opção inválida.")
#         case 2:
#             if len(previsoes) == 0:
#                 print("A lista está vazia.")
#             else:
#                 for previsao in previsoes:
#                     print(previsao)
#         case 3:
#             for previsao in previsoes:
#                 if previsao == "gato":
#                     cont_gatos += 1
#             print(f"Quantidade de gatos: {cont_gatos}")
#         case 4:
#             for previsao in previsoes:
#                 if previsao == "cachorro":
#                     cont_cachorros += 1
#             print(f"Quantidade de cachorros: {cont_cachorros}")
#         case 5:
#             # print(f"Classificações: {len(previsoes)}") if len(provisoes) > 0 else print ("Lista Vazia")
#             if len(previsoes) == 0:
#                 print("Lista vazia!")
#             else:
#                 print(f"Total de classificações: {len(previsoes)}")
#         case 0:
#             print ("Saindo...")
#             break
#         case _:
#             print("Opção inválida.")