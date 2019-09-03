# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 00:04:10 2019

@author: wunde
"""

#Inciso B


#abre el archivo de txto que se ha anexado a la carpeta con los polinomios
with open('numeros.txt') as archivo:
    #el código se entiende de atrás hacia adelante
    #abre cada fila del archivo de texto
    #separa los caracteres en la opracion agrupando los que estan entre espacios
    #el map aplica una funcion a todos los elementos agrupados
    #en este caso la funcion "float" vuelve el texto un decimal para operarlos
    #el mapa regresa direcciones por lo que se aplica list para volverlo un arreglo
    #se asigna a la variable polinomios para poder aplicarle la funcion
    polinomios = [list(map(float, row.split(' '))) for row in archivo]
    
    
#en caso de que no se tenga acceso al archivo se puede probar el codigo con:
#polinomios = [[2.5, 3.0, -4.0, 2.0, 6.5, 1.0, 3.0, 4.0, -1.0, -1.0], [-2.0, 2.0, -3.0, 4.0, 9.1, 1.0, 6.9, 8.0, -1.0, -1.0]]
    

#lo resuelve con un diccionario, si existe el exponente opera su coeficiente
    #si no existe lo agrega
def sumarPolinomios(polinomios):
    dic={}
    for row in polinomios:
        #como ya se vacio en una lista no hace falta while, iteramos todo menos
        #los dos ultimos indices que contiene los -1
        for i in range(0,len(row)-2,2):
            if row[i+1] in dic:
                dic[row[i+1]] += row[i]
            else:
                dic[row[i+1]] = row[i]
    #la respuesta concatena + para los terminos positivoa
    #en los negativos no hace falta pues el float ya lleva su signo
    #se eliminan los terminos cuyo coeficiente sea 0
    resp =""
    for key in sorted(dic.keys(), reverse=True):
        if dic[key] != 0:
            if dic[key]>0:
                resp+="+"
            resp= resp+str(dic[key])+"X^"+str(int(key))
    #se imprime la respuesta 
    print(resp)
    
sumarPolinomios(polinomios)
