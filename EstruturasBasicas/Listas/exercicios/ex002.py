# Sistema de Atendimento em Clínica Médica
from Fila import Fila

pacientes = Fila()


def menuInicial():
    print("=" * 32)
    print("          MENU INICIAL        ")
    print("=" * 32)
    print("[1] - Adicionar paciente")
    print("[2] - Chamar paciente")
    print("[3] - Exinir pacientes")
    print("[0] - Sair")


while True:
    menuInicial()
    opcao = input("Informe uma opção: ")
    if opcao == "1":
        nome = input("Informe o nome do paciente: ")
        idade = input("Informe a idade: ")
        paciente = {"nome": nome, "idade": idade}
        pacientes.enqueue(paciente)
        print("*" * 32)
        print("Paciente adicionado com sucesso!")
        print("*" * 32)
    elif opcao == "2":
        paciente = pacientes.dequeue()
        if not paciente:
            print("*" * 32)
            print("Todos os pacientes já foram atendidos!")
            print("*" * 32)
        else:
            print("*" * 32)
            print(f"Paciente {paciente['nome']}, por favor entrar na sala!")
            print("*" * 32)
    elif opcao == "3":
        if pacientes.ver_tamanho() == 0:
            print("*" * 32)
            print("Não há ninguém na fila ainda!")
            print("*" * 32)
        else:
            pacientes.exibe_fila()
    elif opcao == "0":
        print("*" * 32)
        print("Obrigado por usar, volte sempre!")
        print("*" * 32)
        break
    else:
        print("*" * 32)
        print("Entrada inválida, tente novamente!")
        print("*" * 32)
