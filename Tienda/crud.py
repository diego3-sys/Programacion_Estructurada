import funciones

def insertar(album, artista, genero, anio, precio, stock, conexionBD):
    try:
        if conexionBD and conexionBD.is_connected():
            cursor = conexionBD.cursor()
            sql = """INSERT INTO vinilos (album, artista, genero, anio, precio, stock)
                     VALUES (%s, %s, %s, %s, %s, %s)"""
            valores = (album, artista, genero, anio, precio, stock)
            cursor.execute(sql, valores)
            conexionBD.commit()
            cursor.close()
            return True
        return False
    except Exception as e:
        print(f"\n[Error MySQL en Insertar]: {e}")
        return False

def consultar(conexionBD):
    try:
        if conexionBD and conexionBD.is_connected():
            cursor = conexionBD.cursor()
            # Se quitó 'codigo' de los campos a consultar
            cursor.execute("SELECT id, album, artista, genero, anio, precio, stock FROM vinilos")
            resultado = cursor.fetchall()
            cursor.close()
            return resultado
        return []
    except Exception as e:
        print(f"\n[Error MySQL en Consultar]: {e}")
        return []

def buscar(album, conexionBD):
    try:
        if conexionBD and conexionBD.is_connected():
            cursor = conexionBD.cursor()
            # Se quitó 'codigo' de la consulta
            query = "SELECT id, album, artista, genero, anio, precio, stock FROM vinilos WHERE album LIKE %s"
            cursor.execute(query, (f"%{album}%",))
            resultado = cursor.fetchall()
            cursor.close()
            return resultado
        return []
    except Exception as e:
        print(f"\n[Error MySQL en Buscar]: {e}")
        return []

def borrar(album, conexionBD):
    try:
        if conexionBD and conexionBD.is_connected():
            cursor = conexionBD.cursor()
            cursor.execute("DELETE FROM vinilos WHERE album = %s", (album,))
            conexionBD.commit()
            filas_afectadas = cursor.rowcount
            cursor.close()
            return filas_afectadas > 0
        return False
    except Exception as e:
        print(f"\n[Error MySQL en Borrar]: {e}")
        return False

def modificar(codigo, album, artista, genero, anio, precio, stock, idvinilo, conexionBD):
    try:
        if conexionBD and conexionBD.is_connected():
            cursor = conexionBD.cursor()
            sql = """
            UPDATE vinilos
            SET codigo=%s,
                album=%s,
                artista=%s,
                genero=%s,
                anio=%s,
                precio=%s,
                stock=%s
            WHERE id=%s
            """
            valores = (codigo, album, artista, genero, anio, precio, stock, idvinilo)
            cursor.execute(sql, valores)
            conexionBD.commit()
            cursor.close()
            return True
        return False
    except Exception as e:
        print(f"\n[Error MySQL en Modificar]: {e}")
        return False

def vaciar(conexionBD):
    try:
        if conexionBD and conexionBD.is_connected():
            cursor = conexionBD.cursor()
            cursor.execute("TRUNCATE TABLE vinilos")
            conexionBD.commit()
            cursor.close()
            return True
        return False
    except Exception as e:
        print(f"\n[Error MySQL en Vaciar]: {e}")
        return False

def vender(idvinilo, cantidad, conexionBD):
    try:
        if conexionBD and conexionBD.is_connected():
            cursor = conexionBD.cursor()
            cursor.execute("SELECT precio, stock FROM vinilos WHERE id=%s", (idvinilo,))
            dato = cursor.fetchone()

            if dato:
                precio, stock = dato[0], dato[1]

                if cantidad <= stock:
                    nuevo_stock = stock - cantidad
                    cursor.execute("UPDATE vinilos SET stock=%s WHERE id=%s", (nuevo_stock, idvinilo))
                    conexionBD.commit()
                    cursor.close()

                    subtotal = precio * cantidad
                    iva = subtotal * getattr(funciones, 'IVA', 0.16)
                    descuento = subtotal * getattr(funciones, 'DESCUENTO', 0.0)
                    total = subtotal + iva - descuento

                    return subtotal, iva, descuento, total
            cursor.close()
        return None
    except Exception as e:
        print(f"\n[Error MySQL en Vender]: {e}")
        return None

def descontarStock(id_vinilo, cantidad, conexionBD):
    try:
        if conexionBD and conexionBD.is_connected():
            cursor = conexionBD.cursor()
            
            cursor.execute("SELECT stock FROM vinilos WHERE id = %s", (id_vinilo,))
            resultado = cursor.fetchone()
            
            if resultado:
                stock_actual = resultado[0]
    
                if cantidad <= stock_actual:
                    nuevo_stock = stock_actual - cantidad
                    cursor.execute(
                        "UPDATE vinilos SET stock = %s WHERE id = %s",
                        (nuevo_stock, id_vinilo)
                    )
                    conexionBD.commit()
                    cursor.close()
                    return True, "Stock actualizado correctamente."
                else:
                    cursor.close()
                    return False, f"Stock insuficiente. Solo quedan {stock_actual} unidades."
            else:
                cursor.close()
                return False, "El ID del vinilo no existe."
        return False, "Error de conexión con la base de datos."
    except Exception as e:
        print(f"\n[Error MySQL en Descontar Stock]: {e}")
        return False, str(e)