import math
import random

def escolher_intervalo():

    intervalo_num = int(input("Digite o intervalo desejado: \n1 - Intervalo de 0 a 100. \n2 - Intervalo de 0 a 200.\n"))
    while intervalo_num != 1 and intervalo_num != 2:
        print("Intervalo inválido!")
        intervalo_num = int(input("Digite o intervalo desejado: \n1 - Intervalo de 0 a 100. \n2 - Intervalo de 0 a 200."))
    return intervalo_num

def definir_palpites(intervalo_num):
    if intervalo_num == 1:
        return 7
    else:
        return 10

def gerar_numero_secreto(intervalo_num):

    if intervalo_num == 1:
        return (random.randint(0,100))
    elif:
        return (random.randint(0,100))

def obter_palpite(intervalo_num):

    if intervalo_num == 1:
        palpite = int(input("Digite um número entre 1 e 100: \n"))
        while not (0 <= palpite <= 100):
            palpite = int(input("Digite um número entre 1 e 100: \n"))
    else:
        palpite = int(input("Digite um número entre 1 e 1000: \n"))
        while not (0 <= palpite <= 100):
            palpite = int(input("Digite um número entre 1 e 1000: \n"))
    return palpite

def avaliar_palpite(palpite, numero_secreto):
    if intervalo_num == 1:
        while 0 < num <= 7:
            num -= 1
            if palpite == numero_secreto:
                return "acertou!"
            else:
                palpite = int(input("Errou! Digite um número entre 1 e 100: \n"))
    elif:
        while 0 < num <= 10:
            num -= 1
            if palpite == numero_secreto:
                return "Acertou!"
            else:
                palpite = int(input("Errou! Digite um número entre 1 e 100: \n"))
    else:
        return "errou!"        

  
def jogar():
    intervalo_num = escolher_intervalo()
    num = definir_palpites(intervalo_num)
    numero_secreto = gerar_numero_secreto(intervalo_num)
    palpite = obter_palpite(intervalo_num)
    print(f"Você {avaliar_palpite(palpite, numero_secreto)} O número secreto é: {numero_secreto}")
   
    while True:
        pass
        
if __name__ == "__main__":
    jogar()