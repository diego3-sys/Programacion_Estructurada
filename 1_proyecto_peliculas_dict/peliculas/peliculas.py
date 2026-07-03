import funciones

    
def menuPrincipal():
    print("\t\t....:::: M E N U  P R I N C I P A L ::::...\n")
    opcion=input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Buscar\n\t6.- Limpiar\n\t7.- Salir\n\t\tEscribe una opción: ").strip()
    return opcion
     
def agregarPeliculas(pelis):
    print("\t\t....:::: AGREGAR CARACTERISTICAS A UNA PELICULA ::::...\n")
    caracteristicas=input("Ingresa la caracteristicas: ").upper().strip()
    valor=input("Ingresa el valor de la caracteristicas: ").upper().strip
    pelis[caracteristicas]=valor
    funciones.accionExitosa()
    
def mostrarPeliculas(pelis):
    print("\t\t....:::: MOSTRAR LAS CARACTERISTICAS DE LA PELICULA ::::...\n")
    if len(pelis)>0:
         print("\tCaracteristica\t\tValor")
         for i in pelis
          print(f"\t{i}\t\t{pelis[i]}")
         funciones.espereTecla()
    else:
        input("...¡No exuste ninguna caracteristica en la Pelicula, verofique!...")
   
def limpiarPeliculas(pelis):
     print("\t\t....:::: BORRRAS TODAS LAS CARACTERISTICAS DE LA PELICULA ::::...\n") 
     if len(pelis)>0:
         opc=""
         while opc!="si" and opc!="no":
             opc=input("¿Deseas borrar TODAS las caracteristicas de la pelicula (Si/No)? ").lower().strip()
         if opc=="si":
             pelis=pelis.clear()
             funciones.accionExitosa()
     else:
         input("\n\t...¡No existen caracteristas que borrar, verifique! ....")
    
def buscarPeliculas(pelis):
    print("\t\t....:::: BUSCAR CARACTERISTICAS DE LA PELICULA ::::...\n")   
    caracteristicas=input("Escribe el nombre de la caracteristica: ").upper().strip()
    print("\tCaracteristica\t\tValor")
    noencontro=False
    for i in pelis:
      if caracteristicas==i:
       print(f"\t{i}\t\t{pelis[i]}")
       noencontro=True
      funciones.espereTecla()
    if not(noencontro):
        input("\n\t...¡No existe esta caracteristica que andas buscando!...")

def borrarPeliculas(pelis):
    print("\t\t....:::: BORRAR LA CARCTERISTICAS PELICULAS ::::...\n")   
    caracteristicas=input("Escribe el nombre de la caracteristicas: ").upper().strip()
    noencontro=True
    for i in pelis:
            if caracteristicas==i:
              opc=""
              while opc!="si" and opc!="no":
                opc=input("¿Deseas borrar la caracteristicas (Si/No)? ").lower().strip()
              if opc=="si":
                pelis.pop(caracteristicas)
                funciones.accionExitosa()
                noencontro=False
    if noencontro:
        input("\n\t...¡No existe la caracteristica que andas buscando!...")

def modificarPeliculas(pelis):
    print("\t\t....:::: MODIFICAR LA CARACTERISTICA DE UNA PELICULA ::::...\n")   
    caracteristicas=input("Escribe el nombre de la caracteristica: ").upper().strip()
    noencontro=True
    for i in pelis:
            if caracteristicas==1:
              opc=""
              while opc!="si" and opc!="no":
                opc=input("¿Deseas mofificar la caracteristicas (Si/No)? ").lower().strip()
              if opc=="si":
                pelis[i]=input("Escribe el nuevo nombre: ").upper().strip()
                funciones.accionExitosa()
    if noencontro:
        input("\n\t...¡No existe la caracteristica que andas buscando!...")
 

def buscarPeliculas2(pelis):
    print("Buscar la caracteristica")
    caracteristicas=input("Escribe la caracteristica").upper().strip()
    noencontro=True
    for i in pelis:
           print("\tCaracteristicas\t\Valor")
           if caracteristicas==i:
              print(f"\t{i}\t\t{pelis}")
              noencontro=False
              funciones.espereTecla()
           elif caracteristicas!=i:
            if noencontro:
              input("\n\t..¡No existe esa caracteristica que andas buscando!..")
