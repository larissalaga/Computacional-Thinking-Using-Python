meu_dict = dict()
meudict = {}
meudict["nome"] = "arnaldo"
meudict["idade"] = 10
meudict["sexo"] = "masculino"
print(meudict)

meudict["sexo"]="feminino"
print(meudict)

#meudict[sobrenome] = "alves viana"
print(meudict)

print(len(meudict))
print("******")
print(meudict.values())
print(meudict.keys())
print("****************")

#for qualquercoisa in meudict.keys():  
#        print("nossa")
    #print(qualquercoisa)

for var in meudict.items():
    print(var)

for minha_chave, meu_valor in meudict.items():
    print(f"a chave é: {minha_chave} e o valor é: {meu_valor}")


print("###COMPRAS###")
    
produtos = [
    {"nome": "camiseta", "preço": 29.99, "estoque": 100},
    {"nome": "calça", "preço": 59.99, "estoque": 50},
    {"nome": "tênis", "preço": 129.99, "estoque": 25},
]
for produto in produtos:
    print(produto["nome"], "-", produto["preço"])

novo_produto = {"nome": "boné", "preço": 19.99, "estoque":30}
produtos.append(novo_produto)

for produto in produtos:
    if produto["preço"] > 50:
        produto["preço"] = produto["preço"]*0.8
    print(produto["nome"], "-", produto["preço"])






