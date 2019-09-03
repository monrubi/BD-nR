# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

#inciso A
#Programa para multiplicar matrices

#Para leer archivos
import csv

#aquí se pone la direccion del archivo a leer
def csvMatriz(archivoTexto):
    
    #abre el archivo de txto que se ha anexado a la carpeta con los polinomios
    archivo = open(archivoTexto,"r")
    leerCSV = csv.reader(archivo, delimiter=',')
    matrix=[list(map(int, row)) for row in leerCSV]
    return matrix



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
#se deja el codigo de la matriz por si no se tiene acceso al archivo csv
#matx1= [[10, 20, 30], [5, 6, 7], [15, 26, 89]]
matx1=csvMatriz('ejemplo.csv')
matx2 = [[1,2,1],[3,4,3],[5,6,5]]


mult=multMtx(matx1,matx2)
print(mult)
