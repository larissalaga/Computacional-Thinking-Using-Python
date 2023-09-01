dep_inic= float (input("Qual é o valor do depósito inicial? "))
taxa_anual= float (input("Qual é a taxa anual? "))
tempo= float (input("Qual é o tempo, em anos de investimento? "))

total = dep_inic * (1 + ((taxa_anual/100) / 12)) ** (12*tempo)
print(total)