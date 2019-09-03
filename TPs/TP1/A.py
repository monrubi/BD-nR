# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

#Programa para multiplicar matrices

#Para leer archivos
import csv

#aquí se pone la direccion del archivo a leer
#se dejó comentado para evitar el error del archivo no encontrado

#with open('matriz.csv') as csvfile:
#readCSV = csv.reader(csvfile, delimiter=',')
#matrix=[list(map(int, row)) for row in readCSV]



#Para multiplicar las matrices
#No se agregaron filtros para evitar errores ya que no se especifica
#en el ejercicio


def multMtx(mtx1, mtx2):
    resp=[]
    for i in range(len(mtx1)):
        row=[]
        for j in range(len(mtx1)):
            cont=0
            for k in range(len(mtx2)):
                cont+=mtx1[i][k]*mtx2[k][j]
            row.append(cont)
        resp.append(row)
    return resp

#pruebas
matx1= [[10, 20, 30], [5, 6, 7], [15, 26, 89]]
matx2 = [[1,2,1],[3,4,3],[5,6,5]]

mult=multMtx(matx1,matx2)
print(mult)

    