print("""
Desafio — Cadastro de Alunos com Funções
      """)

def mostrar_menu():
    print("""
1 - Cadastrar aluno
2 - Listar alunos
3 - Buscar aluno
4 - Remover aluno
5 - Mostrar quantidade de alunos
0 - Sair
          """)
    
def cadastrar_aluno(alunos, nome):
    if nome == "":
        print("Nome vazio!")
        return False #return é praticamente um break
    else:
        for aluno in alunos:
            if aluno == nome:
                print("Este aluno já consta na lista.")
                return False #return é praticamente um break
            else:
                alunos.append(nome)
                print("Aluno incluído na lista.")
                return True

def listar_alunos(alunos):
    if len(alunos) == 0:
        print("Lista de alunos vazia.")
    else:
        for aluno in alunos:
            print("Nome: ", aluno)

def buscar_alunos(alunos, nome):
    for aluno in alunos:
        if aluno == nome:
            return True
    return False

def remover_aluno(alunos, nome):
    if nome in alunos:
        alunos.remove(nome)
        print("Aluno removido.")
        return True
    else:
        print("Aluno não cadastrado.")
        return False
    
alunos = []

while True:
    mostrar_menu()
    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1:
            nome = input("Digite o nome do Aluno: ").strip().lower()
            cadastrar_aluno(alunos, nome)
        case 2:
            listar_alunos(alunos)
        case 3:
            nome = input("Informe o nome do aluno que deseja buscar: ").strip().lower()
            if buscar_alunos(alunos, nome):
                print("O aluno está cadastrado.")
            else:
                print("O aluno não está cadastrado.")
        case 4:
            nome = input("Informe o aluno que deseja remover: ")
            remover_aluno(alunos, nome)
        case 5:
            if len(alunos) == 0:
                print("Lista vazia.")
            else:
                print(f"Quantidade de alunos: {len(alunos)}")
        case 0:
            print("Saindo...")
            break
        case _:
            print("Opção inválida. Tente n")
