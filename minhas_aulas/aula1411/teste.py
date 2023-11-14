class Pessoa:
  def _init_(self, nome, idade=None):  
    print('Construtor chamado')
    self.nome = nome 
    self.idade = idade
    self.cor = 'Branco'

p1 = Pessoa()
p1.nome = 'Carlos'
