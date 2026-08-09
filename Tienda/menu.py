import mysql.connector
import funciones
import vinilos

conexionBD = funciones.conectar()
opc_bienvenida = ""


def menuBienvenida():
    print("\t\t....:::: B I E N V E N I D O ::::...\n")
    opcion = input(
        "\n\t1.- Ver Tienda (Gestión de Vinilos)"
        "\n\t2.- Tu Carrito de Vinilos"
        "\n\t3.- Salir"
        "\n\n\tEscribe una opción: "
    ).strip()
    return opcion

def menuPrincipal(conexion):
    clave = ""
    while clave != "1234":  
        clave = input("Ingresa la contraseña para acceder al sistema: ")
        if clave != "1234":
            print("Contraseña incorrecta. Inténtalo de nuevo.\n")

    print("\n¡Acceso concedido! Bienvenido al sistema.\n")
    funciones.espereTecla()
    opc = ""
    while opc != "7":
        funciones.borrarPantalla()
        print("\t\t....:::: T I E N D A ::::...\n")
        opc = input(
            "\n\t1.- Agregar Vinilo"
            "\n\t2.- Eliminar Vinilo"
            "\n\t3.- Modificar Vinilo"
            "\n\t4.- Mostrar Inventario"
            "\n\t5.- Buscar Vinilo"
            "\n\t6.- Limpiar Inventario"
            "\n\t7.- Volver al Menú Principal"
            "\n\n\tEscribe una opción: "
        ).strip()

        match opc:
            case "1":
                vinilos.agregarVinilo(conexion)
            case "2":
                vinilos.eliminarVinilo(conexion)
            case "3":
                vinilos.modificarVinilo(conexion)
            case "4":
                vinilos.mostrarVinilos(conexion)
            case "5":
                vinilos.buscarVinilo(conexion)
            case "6":
                vinilos.limpiarVinilos(conexion)
            case "7":
                print("Regresando...")
            case _:
                funciones.opcionInvalida()

def menuCarro(conexionBD):
    opc=""
    while opc!="7":
        funciones.borrarPantalla()
        print("\t\t....:::: TU CARRITO ::::...\n")
        opc = input(
            "\n\t1.- Agregar al Carrito"
            "\n\t2.- Eliminar del Carrito"
            "\n\t3.- Modificar Cantidad"
            "\n\t4.- Mostrar Carrito"
            "\n\t5.- Buscar en Carrito"
            "\n\t6.- Vaciar Carrito"
            "\n\t7.- Volver al Menú Principal"
            "\n\n\tEscribe una opción: "
        ).strip()

        match opc:
            case "1":
                funciones.borrarPantalla()
                vinilos.agregarAlCarrito(conexionBD) 
            case "2":
                funciones.borrarPantalla()
                vinilos.eliminarDelCarrito(...)
            case "3":
                funciones.borrarPantalla()
                vinilos.modificarCantidadCarrito(...)
            case "4":
                funciones.borrarPantalla()
                vinilos.mostrarCarrito(...)
            case "5":
                funciones.borrarPantalla()
                vinilos.buscarEnCarrito(...)
            case "6":
                funciones.borrarPantalla()
                vinilos.vaciarCarrito(...)
            case "7":
                print("Regresando...")
            case _:
                funciones.opcionInvalida()
import reporte  

def menuCarro(conexionBD):
    opc=""
    while opc!="8":
        funciones.borrarPantalla()
        print("\t\t....:::: TU CARRITO ::::...\n")
        opc=input(
            "\n\t1.- Agregar al Carrito"
            "\n\t2.- Eliminar del Carrito"
            "\n\t3.- Modificar Cantidad"
            "\n\t4.- Mostrar Carrito"
            "\n\t5.- Buscar en Carrito"
            "\n\t6.- Vaciar Carrito"
            "\n\t7.- Generar Reporte Word (.docx)"
            "\n\t8.- Volver al Menú Principal"
            "\n\n\tEscribe una opción: "
        ).strip()

        match opc:
            case "1":
                funciones.borrarPantalla()
                vinilos.agregarAlCarrito(conexionBD)
            case "2":
                funciones.borrarPantalla()
                vinilos.eliminarDelCarrito()
            case "3":
                funciones.borrarPantalla()
                vinilos.modificarCantidadCarrito()
            case "4":
                funciones.borrarPantalla()
                vinilos.mostrarCarrito(conexionBD)
            case "5":
                funciones.borrarPantalla()
                vinilos.buscarEnCarrito()
            case "6":
                funciones.borrarPantalla()
                vinilos.vaciarCarrito()
            case "7":
                funciones.borrarPantalla()
                reporte.generarReporteVentas(conexionBD)  
            case "8":
                print("Regresando...")
            case _:
                funciones.opcionInvalida()
while opc_bienvenida != "3":
    funciones.borrarPantalla()
    opc_bienvenida = menuBienvenida()

    match opc_bienvenida:
        case "1":
            menuPrincipal(conexionBD)
        case "2":
            menuCarro(conexionBD)
        case "3":
            print("\n¡Gracias por visitar la tienda! Hasta luego.")
        case _:
            funciones.opcionInvalida()