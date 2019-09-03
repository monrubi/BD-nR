# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:04:11 2019

@author: sdist
"""

#Inciso e
def contarTipos(dic):
    #declara diccionario para almacenar tipos
    tipos={}
    for key in dic.keys():
      #si existe aumenta el contador
      if type(dic[key]) in tipos:
        tipos[type(dic[key])]+= 1
      #si el tipo no existe en el diccionario lo agrega
      else:
        tipos[type(dic[key])]= 1
    return len(tipos)
      

#codigo para probar funcionalidad      
dict={
 "dir":"rio 32",
 3: 7,
 "telefonos":["2356",456],
 4:9.0,
 6: 'y',
}

#imprime resultado
print(contarTipos(dict))