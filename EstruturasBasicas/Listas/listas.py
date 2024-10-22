# Entradas: respostas que a pessoa fornecer
perguntas = [
    "Telefonou para a vítima? ",
    "Esteve no local do crime? ",
    "Mora perto da vítima? ",
    "Devia para a vitima? ",
    "Já trabalhou com vítima? "
]

# processamento: a pessoa é o quê? vamos contar quantas respostas positivas obtivemos

'''
    Objeto de respostas
'''
respostas = []
for pergunta in perguntas:
    resposta = str(input(pergunta)).lower()
    respostas.append(resposta)

cont = 0
for resposta in respostas:
    if resposta == 's' or resposta == 'sim':
        cont += 1
# Saídas
mensagem = ""
if cont == 5:
    mensagem = "Você é assassina (o)!"
elif cont >= 3:
    mensagem = "Você é cúmplice!"
elif cont >= 2:
    mensagem = "Você é suspeito (a)!"
else:
    mensagem = "Você é inocente! :3"

print(mensagem)






