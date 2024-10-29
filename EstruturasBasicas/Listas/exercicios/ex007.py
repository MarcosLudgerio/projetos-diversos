# FILA - Clínica de antedimento automatico
from Fila import Fila

impressoes = Fila()


def cabecalho():
    print('=' * 32)
    print('              MENU INICIAL ')
    print('=' * 32)
    print('1 - Adicionar novo documento')
    print('2 - Imprimir')
    print('3 - Mostrar próximo documento')
    print('4 - Exibir quantos documentos')
    print('0 - Sair')


cabecalho()
while True:
    opcao = input('Informe uma opcao: ')
    if opcao == '1':
        nome = input('Informe o nome do documento: ')
        impressoes.enfileirar(nome)
    elif opcao == '2':
        if impressoes.tamanho == 0:
            print("Não há impressões ainda!")
        else:
            documento = impressoes.desenfileirar()
            print(f"Imprindo {documento}...")
    elif opcao == '3':
        if impressoes.tamanho == 0:
            print("Não há impressões ainda!")
        else:
            print(f"O proximo documento será {impressoes.mostrar_cabeca()}")
    elif opcao == '4':
      print(f"Faltam {impressoes.tamanho} documento(s)")

    elif opcao == '0':
        break
    else:
        print("entrada inválida")
