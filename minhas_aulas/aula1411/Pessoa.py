
class Pessoa:
  def __init__(self, nome=None, idade=None):  ##construtor da classe
    ## pode ser usado (self, nome= none, idade = none):
    print('Construtor chamado')
    self.nome = nome #o self relaciona a variavel ao objeto- ele existe fora da função
    self.idade = idade
    self.cor = 'Branco'

  def comer(self):
    print(f'{self.nome} está comento')
      
class Estudante(Pessoa):
  def _init_(self, nome=None, curso=None): ## construtor da classe
    self.curso = curso
    super()._init_(nome,idade)


p1 = Pessoa("Glenda",20)
p1.nome = "Carlos"
p1.comer()

p2 = Pessoa()

p2.nome = 'Maria'
p2.idade = 30
p2.comer()
print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
