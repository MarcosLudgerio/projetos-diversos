# FILA - Clínica de antedimento automatico
from Fila import Fila

pacientes = Fila()


def menuInicial():
    print('=' * 32)
    print('              MENU INICIAL ')
    print('=' * 32)
    print('1 - Adicionar paciente')
    print('2 - Remover paciente')
    print('3 - Ver pacientes')
    print('4 - Ver próximo')
    print('0 - Sair')


menuInicial()
while True:
    opcao = input('Informe uma opcao: ')
    if opcao == '1':
        nome = input('Nome do paciente: ')
        pacientes.enfileirar(nome)
    elif opcao == '2':
        if pacientes.tamanho == 0:
            print("FILA VAZIA!")
        else:
            paciente = pacientes.desenfileirar()
            print(f"Paciente {paciente}, entrar na sala")
    elif opcao == '3':
        if pacientes.tamanho == 0:
            print("FILA VAZIA!")
        else:
            print(pacientes)
    elif opcao == '4':
        if pacientes.tamanho == 0:
            print("FILA VAZIA!")
        else:
            print(pacientes.mostrar_cabeca())
    elif opcao == '0':
        break
    else:
        print("entrada inválida")
