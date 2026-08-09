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

    respuesta = crud.insertar(
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
    vinilos = crud.consultar(conexionBD)

    if len(vinilos) > 0:
   
        print(f"{'ID':<5} {'ÁLBUM':<20} {'ARTISTA':<20} {'GÉNERO':<12} {'AÑO':<6} {'PRECIO':<10} {'STOCK':<6}")
        print("-" * 80)
        for v in vinilos:
       
            print(f"{v[0]:<5} {v[1]:<20} {v[2]:<20} {v[3]:<12} {v[4]:<6} ${v[5]:<9.2f} {v[6]:<6}")
    else:
        print("No hay vinilos registrados.")

    funciones.espereTecla()


def buscarVinilo(conexionBD):
    print("\t\t....:::: BUSCAR VINILO ::::...\n")
    album=input("Nombre del álbum: ").upper().strip()
    vinilos=crud.buscar(album, conexionBD)

    if len(vinilos) > 0:
        print(f"{'ID':<5} {'ÁLBUM':<20} {'ARTISTA':<20} {'GÉNERO':<12} {'AÑO':<6} {'PRECIO':<10} {'STOCK':<6}")
        print("-" * 80)
        for v in vinilos:
            print(f"{v[0]:<5} {v[1]:<20} {v[2]:<20} {v[3]:<12} {v[4]:<6} ${v[5]:<9.2f} {v[6]:<6}")
    else:
        print("No existe ese álbum.")

    funciones.espereTecla()

def eliminarVinilo(conexionBD):
    print("\t\t....:::: ELIMINAR VINILO ::::...\n")
    album=input("Álbum a eliminar: ").upper().strip()
    vinilos=crud.buscar(album, conexionBD)

    if len(vinilos) > 0:
        for v in vinilos:
            print(f"ID: {v[0]} | Código: {v[1]} | Álbum: {v[2]} | Artista: {v[3]}")
        
        opc=input("\n¿Seguro que deseas eliminarlo? (si/no): ").lower().strip()
        if opc=="si":
            respuesta = crud.borrar(album, conexionBD)
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
        print("Presiona Enter en blanco si no deseas modificar el dato.\n")
        
        codigo=input(f"Código [{v[1]}]: ").upper().strip() or v[1]
        albumNuevo=input(f"Álbum [{v[2]}]: ").upper().strip() or v[2]
        artista=input(f"Artista [{v[3]}]: ").upper().strip() or v[3]
        genero=input(f"Género [{v[4]}]: ").upper().strip() or v[4]

        try:
            año_in=input(f"Año [{v[5]}]: ").strip()
            año=int(año_in) if año_in != "" else v[5]

            precio_in=input(f"Precio [{v[6]}]: ").strip()
            precio=float(precio_in) if precio_in != "" else v[6]

            stock_in=input(f"Stock [{v[7]}]: ").strip()
            stock=int(stock_in) if stock_in != "" else v[7]
        except ValueError:
            print("\n Error: Los campos numéricos contienen valores inválidos.")
            funciones.accionNOExitosa()
            funciones.espereTecla()
            return

        respuesta=crud.modificar(
            codigo, albumNuevo, artista, genero, año, precio, stock, v[0], conexionBD
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
    opc=input("¿Deseas borrar TODOS los registros del inventario? (si/no): ").lower().strip()
    if opc=="si":
        respuesta=crud.vaciar(conexionBD)
        if respuesta:
            funciones.accionExitosa()
        else:
            funciones.accionNOExitosa()
    funciones.espereTecla()
carrito = []

def agregarAlCarrito(conexionBD):
    print("\t\t....:::: AGREGAR AL CARRITO ::::...\n")
    mostrarVinilos(conexionBD)
    
    try:
        id_vinilo = int(input("\nIngresa el ID del vinilo que deseas agregar: "))
        cantidad = int(input("Ingresa la cantidad: "))
        
        if cantidad <= 0:
            print("\nLa cantidad debe ser mayor a 0.")
            funciones.espereTecla()
            return

        exito, mensaje = crud.descontarStock(id_vinilo, cantidad, conexionBD)
        
        if exito:
            
            carrito.append({
                "id": id_vinilo,
                "cantidad": cantidad
            })
            print(f"\n¡Éxito! {mensaje}")
            funciones.accionExitosa()
        else:
            print(f"\nNo se pudo agregar: {mensaje}")
            funciones.accionNOExitosa()

    except ValueError:
        print("\nError: Debes ingresar números válidos.")
        funciones.accionNOExitosa()
        
    funciones.espereTecla()


def mostrarCarrito(conexionBD):
    print("\t\t....:::: TU CARRITO ::::...\n")
    if len(carrito) == 0:
        print("El carrito está vacío.")
    else:
        print(f"{'POSICIÓN':<10} {'ID VINILO':<12} {'CANTIDAD':<10}")
        print("-" * 40)
        for idx, item in enumerate(carrito, start=1):
            print(f"{idx:<10} {item['id']:<12} {item['cantidad']:<10}")
    funciones.espereTecla()


def eliminarDelCarrito():
    print("\t\t....:::: ELIMINAR DEL CARRITO ::::...\n")
    if len(carrito) == 0:
        print("El carrito está vacío.")
    else:
        for idx, item in enumerate(carrito, start=1):
            print(f"{idx}.- ID Vinilo: {item['id']} | Cantidad: {item['cantidad']}")
        try:
            pos = int(input("\nIngresa el número de ítem a eliminar: ")) - 1
            if 0 <= pos < len(carrito):
                eliminado = carrito.pop(pos)
                print(f"\nSe eliminó el registro del carrito.")
                funciones.accionExitosa()
            else:
                print("\nNúmero fuera de rango.")
        except ValueError:
            print("\nIngresa un número válido.")
    funciones.espereTecla()


def modificarCantidadCarrito():
    print("\t\t....:::: MODIFICAR CANTIDAD ::::...\n")
    if len(carrito) == 0:
        print("El carrito está vacío.")
    else:
        for idx, item in enumerate(carrito, start=1):
            print(f"{idx}.- ID Vinilo: {item['id']} | Cantidad actual: {item['cantidad']}")
        try:
            pos = int(input("\nSelecciona el número de ítem: ")) - 1
            if 0 <= pos < len(carrito):
                nueva_cant = int(input("Ingresa la nueva cantidad: "))
                if nueva_cant > 0:
                    carrito[pos]['cantidad'] = nueva_cant
                    funciones.accionExitosa()
                else:
                    print("\nLa cantidad debe ser mayor a 0.")
            else:
                print("\nNúmero fuera de rango.")
        except ValueError:
            print("\nIngresa un valor numérico válido.")
    funciones.espereTecla()


def buscarEnCarrito():
    print("\t\t....:::: BUSCAR EN CARRITO ::::...\n")
    if len(carrito) == 0:
        print("El carrito está vacío.")
    else:
        try:
            id_b = int(input("Ingresa el ID del vinilo a buscar en el carrito: "))
            encontrados = [item for item in carrito if item['id'] == id_b]
            if encontrados:
                for item in encontrados:
                    print(f"\n-> Encontrado: ID Vinilo {item['id']} - Cantidad: {item['cantidad']}")
            else:
                print("\nEse vinilo no está en tu carrito.")
        except ValueError:
            print("\nID inválido.")
    funciones.espereTecla()


def vaciarCarrito():
    print("\t\t....:::: VACIAS CARRITO ::::...\n")
    if len(carrito) == 0:
        print("El carrito ya está vacío.")
    else:
        opc = input("¿Seguro que deseas vaciar todo el carrito? (si/no): ").lower().strip()
        if opc == "si":
            carrito.clear()
            funciones.accionExitosa()
    funciones.espereTecla()


def procesarCompra(conexionBD):
    print("\t\t....:::: PROCESAR COMPRA / VENTA ::::...\n")
    if len(carrito) == 0:
        print("El carrito está vacío.")
        funciones.espereTecla()
        return

    total_compra = 0
    print("Procesando los ítems de tu carrito...\n")
    for item in carrito:
        res = crud.vender(item['id'], item['cantidad'], conexionBD)
        if res:
            subtotal, iva, descuento, total = res
            total_compra += total
            print(f"ID {item['id']}: Subtotal=${subtotal:.2f} | IVA=${iva:.2f} | Total=${total:.2f}")
        else:
            print(f"No se pudo procesar el ID {item['id']} (Stock insuficiente o ID no existe).")
    
    print(f"\n-------------------------------------")
    print(f"TOTAL COBRADO: ${total_compra:.2f}")
    carrito.clear() 
    funciones.espereTecla()

    

