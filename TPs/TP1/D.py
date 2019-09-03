def leerYContarPalabras(archivoTexto):
  f = open(archivoTexto,"r")
  if f.mode=="r":
    cont = f.read()
    #Convierte los cambios de fila a espacios para que funcione el split
    cont = cont.replace("\n"," ")
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

#El texto es parte de la canción del "Hey Jude" de los Beatles
leerYContarPalabras("textoD.txt")
