import math
import random

def escolher_intervalo():

    intervalo_num = int(input("Digite o intervalo desejado: \n1 - Intervalo de 0 a 100. \n2 - Intervalo de 0 a 1000.\n"))
    while intervalo_num != 1 and intervalo_num != 2:
        print("Intervalo inválido!")
        intervalo_num = int(input("Digite o intervalo desejado: \n1 - Intervalo de 0 a 100. \n2 - Intervalo de 0 a 1000."))
    return intervalo_num

def definir_palpites(intervalo_num):
    if intervalo_num == 1:
        return 7
    else:
        return 10

def gerar_numero_secreto(intervalo_num):

    if intervalo_num == 1:
        return random.randint(0,100)
    else:
        return (random.randint(0,1000))

def obter_palpite(intervalo_num):
    if intervalo_num == 1:
        palpite = int(input("Digite um número entre 1 e 100: \n"))
        while not (0 <= palpite <= 100):
            palpite = int(input("Digite um número entre 1 e 100: \n"))
    else:
        palpite = int(input("Digite um número entre 1 e 1000: \n"))
        while not (0 <= palpite <= 1000):
            palpite = int(input("Digite um número entre 1 e 1000: \n"))
    return palpite

def avaliar_palpite(palpite, numero_secreto):
    if palpite == numero_secreto:
        print("Acertooou!")
        return True
    elif palpite > numero_secreto:
        print("O número secreto é menor!")
        return False
    else:
        print("O número secreto é maior!")
        return False        
  
def jogar():
    intervalo_num = escolher_intervalo()
    num = definir_palpites(intervalo_num)
    numero_secreto = gerar_numero_secreto(intervalo_num)    
    aux = num
    resultado = False
    while (0 < aux <= num) and (resultado == False):
        print(f"Você tem {aux} palpites.")
        aux -= 1
        palpite = obter_palpite(intervalo_num)
        resultado = avaliar_palpite(palpite, numero_secreto)
    print(f"O número secreto é: {numero_secreto}, você usou {num - aux} palpites!")
   
        
if __name__ == "__main__":
    jogar()