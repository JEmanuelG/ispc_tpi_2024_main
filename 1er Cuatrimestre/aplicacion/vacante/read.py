
def ver_vacantes():
    
    import mysql.connector

    print('\nListado de vacantes:\n')

    conexion = mysql.connector.connect(user='root',
                                    password='123456',
                                    host='localhost',
                                    database="data_human´s"
                                    )

    cursor = conexion.cursor()

    cursor.execute(f'SELECT * FROM vacantes')

    vacantes = cursor.fetchall()


    #print(vacantes)

    for vac in vacantes:
        cursor.execute(f'SELECT Descripcion, Condicioncontratacion, Seconsidera FROM caracteristicaspuesto WHERE Id_caractpuesto = {vac[4]}')
        caracteristica_puesto = cursor.fetchall()   

        print("ID:", vac[0])
        print("Titulo:", vac[3])
        print("Descripción:", caracteristica_puesto[0][0])
        print("Condición de Contratación:", caracteristica_puesto[0][1])
        print("Se considera:", caracteristica_puesto[0][2])
        print("-" * 20, "\n")

    conexion.close()
