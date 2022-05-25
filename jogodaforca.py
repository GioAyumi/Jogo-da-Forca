import random

#Váriaveis
palavras=["yasuo","lulu","janna","irelia","karma","samira","kaisa","ashe","nami"]
print("Vamos jogar forca!")
#função que escolhe uma palavra aleatória da lista
def selectrandom(palavras):
  return random.choice(palavras)
palavra=random.choice(palavras)
estrela="*"
for i in range (len(palavra)):
    descobrir=(i*estrela)+estrela
tentativas=10
erros=0
descobrir=list(descobrir)
dica=input("Você vai querer uma dica para começar, se sim digite 1 e caso contrário digite 2? ")
if dica=="1":
    if palavras[0]==palavra:
        print("A dica é: É doente!")
    elif palavras[1]==palavra:
        print("A dica é: Melhor campeão do jogo")
    elif palavras[2]==palavra:
        print("A dica é: É muito bom, mas ta meio bosta")
    elif palavras[3]==palavra:
        print("A dica é: Bonecasso")
    elif palavras[4]==palavra:
        print("A dica é: ninguém corre de...")
    elif palavras[5]==palavra:
        print("A dica é: Bonecão")
    elif palavras[6]==palavra:
        print("A dica é: Faça mid ap")
    elif palavras[7]==palavra:
        print("A dica é: A rainha do mandato")
    elif palavras[8]==palavra:
        print("A dica é: sushi")
print("vamos começar!")
print("A palavra é ",descobrir)
while (descobrir!=palavra):
    letra=input("Digite uma letra: ")
    if letra==palavra[0]:
        descobrir[0]=letra
        print(descobrir)

    elif letra==palavra[1]:
        posiçao=palavra.find(letra)
        descobrir[posiçao]=letra
        print("Parabéns você achou a letra ",letra)
        print(descobrir)
    elif letra==palavra[2]:
        posiçao=palavra.find(letra)
        descobrir[posiçao]=letra
        print("Parabéns você achou a letra ",letra)
        print(descobrir)
    elif letra==palavra[3]:
        posiçao=palavra.find(letra)
        descobrir[posiçao]=letra
        print("Parabéns você achou a letra ",letra)
        print(descobrir)
    elif letra==palavra[4]:
        posiçao=palavra.find(letra)
        descobrir[posiçao]=letra
        print("Parabéns você achou a letra ",letra)
        print(descobrir)
    elif letra==palavra[5]:
        posiçao=palavra.find(letra)
        descobrir[posiçao]=letra
        print("Parabéns você achou a letra ",letra)
        print(descobrir)
    
    else:
        tentativas=tentativas-1
        print("você ainda tem ",tentativas,"tentativas")
    if tentativas==0:
        print("Acabou suas tentativas :(")
        break


        
    




