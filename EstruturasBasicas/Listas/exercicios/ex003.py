from FilaImplemetacao2 import Fila

pacientes = Fila()


def menuInicial():
    print('=' * 32)
    print('              Menu inicial ')
    print('=' * 32)
    print('1 - Adicionar paciente')
    print('2 - Remover paciente')
    print('3 - Ver pacientes')
    print('4 - Ver próximo')
    print('0 - Sair')


while True:
    menuInicial()
    opcao = input('Informe uma opcao: ')
    if opcao == '1':
        nome = input('Nome do paciente: ')
        pacientes.enfileirar(nome)
    elif opcao == '2':
        paciente = pacientes.desinfileirar()
        print(f"Paciente {paciente}, entrar na sala")
    elif opcao == '3':
        print(pacientes)
    elif opcao == '4':
        print(pacientes.ver_head())
    elif opcao == '0':
        break
    else:
        print("entrada inválida")
