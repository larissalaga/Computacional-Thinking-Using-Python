def calc_pontos(pontos):
  if pontos > 90:
    return "Ótimo!"
  elif pontos > 80:
    return "Muito bom!"
  elif pontos > 70:
    return "Bom!"
  else:
    return "Tente novamente"

nota = float(input("digite um valor: "))
pontos = calc_pontos(nota)
print(pontos)