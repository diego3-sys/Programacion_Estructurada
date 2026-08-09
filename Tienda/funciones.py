import mysql.connector


IVA = 0.16
DESCUENTO = 0.10


def borrarPantalla():
    print("\033c")


def espereTecla():
    input("...¡Oprima cualquier tecla para continuar!...")


def accionExitosa():
    input("...¡Acción realizada con éxito!...")


def accionNOExitosa():
    input("...¡No fue posible realizar esta acción, inténtalo nuevamente!...")


def terminarSistema():
    input("....:::: GRACIAS POR UTILIZAR EL SISTEMA DE TIENDA DE VINILOS ::::\n\nVuelve pronto...")


def opcionInvalida():
    input("\n\t.... ¡Opción inválida, vuelve a intentarlo!.... ")


def conectar():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_vinilos"
        )
        return conexion
    except:
        borrarPantalla()
        input("No fue posible conectar con la base de datos.")
        return None

