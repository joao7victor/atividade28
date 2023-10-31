# Exercício Python 28 : Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
from datetime import date 

today = date.today() 
anoAtual = today.year 
idadeMaior= []
idadeMenor= []

for i in range (8):
    AnoDeNascimento= int(input(" ano de nascimento"))
    if anoAtual - AnoDeNascimento >= 18
    idadeMaior.append(AnoDeNascimento)
else:
    idadeMenor.append(AnoDeNascimento)
print(idadeMaior)
print(idadeMenor)


