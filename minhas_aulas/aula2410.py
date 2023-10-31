"""from aula2410_auxiliar import *

print (soma(2,3))
print (subtrai(2,3))"""

"""import aula2410_auxiliar

print(aula2410_auxiliar.soma(2,3))
print(aula2410_auxiliar.subtrai(2,3))"""

"""def soma(a,b,c=0):
  return a+b+c

print(soma(2,3))
print(soma(1,2,3))"""

from aula2410_auxiliar import soma as s

def somar(*args):
  res = 0
  for i in args:
    print(i)
    res +=1
  return res

print(somar())
print(somar(1,2,3))

res = s(1,2)
res2 = s(res,3)
print(res2)

