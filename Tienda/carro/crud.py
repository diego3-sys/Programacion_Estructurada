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