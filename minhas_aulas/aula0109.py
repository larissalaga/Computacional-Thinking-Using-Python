temperatura = 25

#if temperatura == 25:
#   temperatura = 40
#   print (temperatura)

pontos = 50
if pontos > 90:
    print("Excelente!")
elif pontos > 80:
    print("Muito bom!")
elif pontos > 70:
    print("Bom!")
else:
    print("Tente novamente")


idade =  int(input("digite idade"))
acompanhado = bool(input("Está acompanhado? true or false "))


if idade < 18:
    if acompanhado:
        print("Menor de idade, mas está acompanhado.")
    else:
        print("Menor de idade e desacompanhado.")
else:
    print("Maior de idade.")