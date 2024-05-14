from datetime import datetime
import random

print('Hello, Bem vindo a nossa Empresa')
nome = input('Digite seu nome: ')
idade= int(input('Digite sua idade: '))
data_cadastro = datetime.now()
cartoes = ['R$50,00','R$250,00','R$120,00']
cartao = random.choice(cartoes)
aniversario = datetime.strptime(input('Digite sua data de aniversario no formato dd/mm/aaaa: '), '%d/%m/%Y')

print(f"OLA {nome}, seu registro foi concluido com sucesso no dia {data_cadastro.day}/{data_cadastro.month}/{data_cadastro.year}.\nParabens, houve um sorteio e voce ganhou um cartao de compras no valor de {cartao}")