import funciones
import vinilos
import menu

opc="1"
conexionBD=funciones.conectar()

while opc != "7":
    funciones.borrarPantalla()
    opc=menu.menuPrincipal()

    match opc:
        case "1":
            funciones.borrarPantalla()
            vinilos.agregarVinilo(conexionBD)

        case "2":
            funciones.borrarPantalla()
            vinilos.eliminarVinilo(conexionBD)

        case "3":
            funciones.borrarPantalla()
            vinilos.modificarVinilo(conexionBD)

        case "4":
            funciones.borrarPantalla()
            vinilos.mostrarVinilos(conexionBD)

        case "5":
            funciones.borrarPantalla()
            vinilos.buscarVinilo(conexionBD)

        case "6":
            funciones.borrarPantalla()
            vinilos.limpiarVinilos(conexionBD)

        case "7":
            funciones.borrarPantalla()
            funciones.terminarSistema()

        case _:
            funciones.opcionInvalida()



