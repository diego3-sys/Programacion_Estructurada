import funciones
import crud


def agregarVinilo(conexionBD):
    print("\t\t....:::: AGREGAR VINILO ::::...\n")
  
    album=input("Álbum: ").upper().strip()
    artista=input("Artista: ").upper().strip()
    genero=input("Género: ").upper().strip()
    año=int(input("Año: "))
    precio=float(input("Precio: "))
    stock=int(input("Stock: "))

    respuesta=crud.insertar(
        
        album,
        artista,
        genero,
        año,
        precio,
        stock,
        conexionBD
    )

    if respuesta:
        funciones.accionExitosa()
    else:
        funciones.accionNOExitosa()


def mostrarVinilos(conexionBD):

    print("\t\t....:::: INVENTARIO ::::...\n")

    vinilos=crud.consultar(conexionBD)

    if len(vinilos) > 0:

        print("ID\tALBUM\tARTISTA\tGENERO\tAÑO\tPRECIO\tSTOCK")

        for v in vinilos:
            print(f"{v[1]}\t{v[2]}\t{v[3]}\t{v[4]}\t{v[5]}\t${v[6]}\t{v[7]}")

    else:
        print("No hay vinilos registrados.")

    funciones.espereTecla()


def buscarVinilo(conexionBD):
    print("\t\t....:::: BUSCAR VINILO ::::...\n")
    album = input("Nombre del álbum: ").upper().strip()
    vinilos = crud.buscar(album, conexionBD)
    if len(vinilos) > 0:
        print("\tALBUM\tARTISTA\tGENERO\tAÑO\tPRECIO\tSTOCK")
        for v in vinilos:
            print(f"{v[1]}\t{v[2]}\t{v[3]}\t{v[4]}\t{v[5]}\t${v[6]}\t{v[7]}")
    else:
        print("No existe ese álbum.")
    funciones.espereTecla()


def eliminarVinilo(conexionBD):
    print("\t\t....:::: ELIMINAR VINILO ::::...\n")
    album=input("Álbum a eliminar: ").upper().strip()
    vinilos=crud.buscar(album, conexionBD)

    if len(vinilos) > 0:
        for v in vinilos:
            print(v)
        opc=input("¿Eliminar? (si/no): ").lower().strip()
        if opc=="si":
            respuesta=crud.borrar(album, conexionBD)
            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNOExitosa()
    else:
        print("No existe el álbum.")

    funciones.espereTecla()


def modificarVinilo(conexionBD):
    print("\t\t....:::: MODIFICAR VINILO ::::...\n")
    album=input("Álbum a modificar: ").upper().strip()
    vinilos=crud.buscar(album, conexionBD)
    if len(vinilos) > 0:
        v=vinilos[0]
        print("Deja vacío si no deseas modificar un dato.\n")
        albumNuevo=input(f"Álbum [{v[1]}]: ").upper().strip() or v[1]
        artista=input(f"Artista [{v[2]}]: ").upper().strip() or v[2]
        genero=input(f"Género [{v[3]}]: ").upper().strip() or v[3]

        año=input(f"Año [{v[4]}]: ").strip()
        if año=="":
            año=v[4]
        else:
            año=int(año)

        precio=input(f"Precio [{v[5]}]: ").strip()
        if precio=="":
            precio=v[5]
        else:
            precio=float(precio)

        stock=input(f"Stock [{v[6]}]: ").strip()
        if stock=="":
            stock=v[6]
        else:
            stock=int(stock)
        respuesta=crud.modificar(
            albumNuevo,
            artista,
            genero,
            año,
            precio,
            stock,
            v[0],
            conexionBD
        )
        if respuesta:
            funciones.accionExitosa()
        else:
            funciones.accionNOExitosa()
    else:
        print("No existe ese álbum.")
    funciones.espereTecla()

def limpiarVinilos(conexionBD):
    print("\t\t....:::: LIMPIAR INVENTARIO ::::...\n")
    opc=input("¿Deseas borrar TODOS los registros? (si/no): ").lower().strip()
    if opc=="si":
        respuesta = crud.vaciar(conexionBD)
        if respuesta:
            funciones.accionExitosa()
        else:
            funciones.accionNOExitosa()
    funciones.espereTecla()