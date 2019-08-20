# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import random

def muevete(k, lista):
    aux = [0]*abs(k)
    if k > 0:
        lista = aux + lista
        del lista[len(lista)-k:len(lista)]
    elif k<0:
        lista = lista + aux
        del lista[0:abs(k)]
    return lista
  
def sum_mat(A,B):
    suma = []
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        for i in range(len(A)):
            suma.append([])
            for j in range(len(A[0])):
                suma[i].append(A[i][j]+B[i][j])
    return suma
  
a = [1,2,3,4,5,6]

#num alumnos
n=5
califs=[]
#genera las califs
for i in range(n):
  califs.append(float(random.randint(5,10)))#randint tiene intervalo cerrado

por = [0.1, 0.2, 0.23, 0.3, 0.17]

prom =0
for i in range(n):
  prom += califs[i]*por[1]

print("Promedio con decimales: {}".format(prom))

promedio = [c*p for c,p in zip(califs, por)]
prom = round(sum(promedio),1)
print(prom)

def tuplaPares(tupla):
  resp = ()
  for i in range(0,len(tupla),2):
    resp += (t[i],)
  return tuple(resp)

def tuplaPar(tupla):
  return tupla[0:len(tupla):2]

eje= ('Yo', 1, 'mi', 4.5, 7)

print(tuplaPar(eje))


