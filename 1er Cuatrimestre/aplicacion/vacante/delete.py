
def eliminar_vacante():
    
    import mysql.connector

    print('\nEliminar vacante por ID\n')
    
    id = int(input("Ingresá el ID de la vacante que querés eliminar: "))

    conexion = mysql.connector.connect(user='root',
                                    password='123456',
                                    host='localhost',
                                    database="data_human´s"
                                    )

    cursor = conexion.cursor()

    # BORRA DATOS SEGúN CONDICIÓN, SI NO SE PONE CONDICIÓN BORRA TODA LA TABLA
    cursor.execute(f"DELETE FROM vacantes WHERE Id_vacantes = {id}")
    cursor.execute(f"DELETE FROM caracteristicaspuesto WHERE Id_caractpuesto = {id}")

    conexion.commit()

    conexion.close()
