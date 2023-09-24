def jogo_adivinhacao (intervalo, palpite):

  num = 23
  if intervalo == 1:
    jogadas = 7

    while (0 < jogadas <= 7) and (num != palpite):
      jogadas -= 1
      
      if palpite < num:
        print(f"{palpite} é menor!")
      elif palpite > num:
        print(f"{palpite} é maior!")
      else:
        return "Acertou"
      palpite = int (input("Digite seu palpite: "))
    return "Errou"
  else:
    jogadas = 14

    while (0 < jogadas <= 14) and (num != palpite):
      jogadas -= 1
      
      if palpite < num:
        return "Menor!"
        palpite = int (input("Digite seu palpite: "))
      elif palpite > num:
        return "Maior!"
        palpite = int (input("Digite seu palpite: "))
      else:
        return "Acertou"
    
    
intervalo = int(input("Digite o intervalo: \n 1 - Entre 1 e 100 \n 2 - Entre 1 e 200: \n"))
palpite = int (input("Digite seu palpite: "))

print(f"{palpite} é {jogo_adivinhacao(intervalo, palpite)}")
