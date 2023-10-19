from random import randint

computador = randint(0,10) 

print("Sou o seu adversário, acabei de pensar em um número entre 0 e 10. ")
print("Será que vc consegue adivinhar qual foi? ")
acertou = False
palpites = 0

while not acertou:
    jogador = int(input("Informe seu palpite: "))
    palpites +=1
    if jogador == computador:
        acertou = True
print(f"Acertou com {palpites} palpites!")



