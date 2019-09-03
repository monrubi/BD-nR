#Esto imprime la cantidad de diferentes palabras en el archivo de texto dado
def leerYContarPalabras(archivoTexto):
  f = open(archivoTexto,"r")
  if f.mode=="r":
    cont = f.read()
    #Esta parte convierte a los cambios de fila, los comas y los puntos a espacios
    cont = cont.replace("\n"," ")
    cont = cont.replace(", "," ")
    cont = cont.replace(".","")
    
    lCont = cont.split(" ")
    dic = dict()
    #revisa todas las palabras del texto y la agrega al dictionario si no existen o le suma a la cuenta si sí existen.
    for word in lCont:
      if word in dic:
        dic[word] += 1
      else:
        dic[word] = 1
    count =0
    #Cuenta todas las diferentes palabras en el dictionario
    for word in dic:
      count+=1
    print(count)

#El texto es parte de la canción del "Let it be" de los Beatles
leerYContarPalabras("textoD.txt")
