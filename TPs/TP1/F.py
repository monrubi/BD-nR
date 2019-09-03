# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:46:01 2019

@author: sdist
"""

#inciso F

def getRango():
  print("Dame la primera cadena")
  cad1=input()
  while len(cad1) > 7:
    print("La cadena no debe medir mas de 7 caracteres")
    cad1=input()
  print("Dame la segunda cadena")
  cad2=input()
  while len(cad2) > 7 or cad2 < cad1:
    print("La cadena no debe medir mas de 7 caracteres y debe ser mayor a la primera")
    cad2=input()
  return(cad1, cad2)
  
def funcionRara(lectura, escritura):
  rango = getRango()
  archivo = open(lectura,'r')
  resp = open(escritura,'w')
  for row in archivo:
    if len(row)in range(7,41):
      if row[0:7] >= rango[0] and row[0:7] <= rango[1]:
        resp.write(row+"\n")
  archivo.close()
  resp.close()
  print("Proceso terminado")
  
  
#texto de generador de lorem ipsum version gatuna

funcionRara('lorem_ipsum.txt','resp.txt')
        
      
  