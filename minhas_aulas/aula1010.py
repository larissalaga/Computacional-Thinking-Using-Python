""""
o sistema vai ter as funções

adicionar contato
listar contato
editar contato
excluir contato
buscar contato

a estrutura da agenda será um dicionario de dicionarios para cada contato.


"""
agenda = {
    "pedro":{
        "telefone":"22258-6998",
        "email": "pedro@email.com",
        "endeço": "rua pedro, 123"
    },
    "renato":{
        "telefone":"22258-6998",
        "email": "pedro@email.com",
        "endeço": "rua pedro, 123"
    } 
}


def adicionar_contato(agenda,nome,tel,email,end):
  novo_contato = {}
  novo_contato["telefone"] = tel
  novo_contato["email"] = email
  novo_contato["endereço"] = end

  agenda[nome] = novo_contato
  print(f"\n Contato {nome} adicionado com sucesso!!!")

def listar_contato(agenda):
  print(f"agenda possui {len(agenda)} contatos.")
  for nome, contato in agenda.items():
    print(nome)
    for tipo, valor in contato.items():
      print(f"{tipo} - {valor}")

def editar_contato(agenda,nome,tel,email,end):
  novo_contato = {}
  novo_contato["telefone"] = tel
  novo_contato["email"] = email
  novo_contato["endereço"] = end
  agenda[nome] = novo_contato
  print(f"\n Contato {nome} editado com sucesso!!!")
  

def excluir_contato(agenda, nome):
  #forma 1
  if nome in agenda:
    del agenda[nome]
  else:
    print(f"Contato {nome} não existe!")
  #forma 2
  #print(agenda.get(nome, "não existe"))

def buscar_contato(agenda, nome):
  print(agenda.get(nome, "contato não existe"))
  
  

def menu():
  while True:
    print("\n_agenda de contatos_\n")
    print(" 1. - adicionar contato")
    print(" 2. - listar contato")
    print(" 3. - editar contato")
    print(" 4. - excluir contato")
    print(" 5. - buscar contato")
    print(" 6. - sair\n")

    user_op = input("Escolha uma opção: ")

    if user_op == "1":
      user_name = input("Nome do contato:")
      if user_name not in agenda:
        user_tel = input("Tel do contato:")
        user_email = input("Email do contato:")
        user_end = input("endereço do contato:")
        adicionar_contato(agenda,user_name,user_tel,user_email,user_end)
      else:
        print(f"\nContato {user_name} já existe")
      
    elif user_op == "2":
      listar_contato(agenda)

    elif user_op == "3":
      user_name = input("Nome do contato:")
      if user_name in agenda:
        user_tel = input("Tel do contato:")
        user_email = input("Email do contato:")
        user_end = input("endereço do contato:")
        editar_contato(agenda,user_name,user_tel,user_email,user_end)
      else:
        print(f"\nContato {user_name} não existe")
  
    elif user_op == "4":
      user_name = input("Escolha o contato para excluir: ")
      excluir_contato(agenda,user_name)

    elif user_op == "5":
      user_name = input("Encontre o contato:")
      buscar_contato(agenda,user_name)

    elif user_op == "6":
      print("Obrigado, fechando o programa!!")
      break

    else:
      print(f"Opção {user_op} inválida! Escolha uma opção válida.")


if__name__ == "__main__":
menu()


