
def modificar_vacante():
    
    import mysql.connector

    print('\nModificar vacante por ID:\n')
    id = int(input("Ingresá el ID de la vacante que querés modificar: "))

    conexion = mysql.connector.connect(user='root',
                                    password='123456',
                                    host='localhost',
                                    database="data_human´s"
                                    )

    cursor = conexion.cursor()

    cursor.execute(f'SELECT * FROM vacantes WHERE Id_vacantes = {id}')
    vac = cursor.fetchall()
    vac = vac[0]

    cursor.execute(f'SELECT Descripcion, Condicioncontratacion, Seconsidera FROM caracteristicaspuesto WHERE Id_caractpuesto = {vac[4]}')
    caracteristica_puesto = cursor.fetchall()

    print("Datos actuales:")
    print("ID:", vac[0])
    print("Titulo:", vac[3])
    print("Descripción:", caracteristica_puesto[0][0])
    print("Condición de Contratación:", caracteristica_puesto[0][1])
    print("Se considera:", caracteristica_puesto[0][2])
    print("-" * 20, "\n\n")

    print("Ingresa los nuevos datos de la vacante")
    nvo_titulo = input("Ingresá el nuevo título: ")
    nva_desc = input("Ingresá la nueva descripción: ")
    nva_condicion = input("Ingresá la nueva condición de contratación: ")
    nvo_seconsidera = input("Ingresá otros datos de la vacante: ") 


    cursor.execute(f"UPDATE vacantes SET Titulopuesto = '{nvo_titulo}' WHERE Id_vacantes = {vac[0]}")
    conexion.commit()

    cursor.execute(f"""UPDATE caracteristicaspuesto SET Descripcion = '{nva_desc}', Condicioncontratacion = '{nva_condicion}', Seconsidera = '{nvo_seconsidera}' 
                   WHERE Id_caractpuesto = {vac[4]}""")
    conexion.commit()



    # if id in vacantes:
    #     print("Datos actuales:", vacantes[id])
    #     modificar = input("¿Desea modificar los datos de esta vacante? (si/no): ")
    #     if modificar.lower() == "si":
    #         vacantes[id]["titulo"] = input("Ingresá el nuevo título (dejalo vacío para no modificar): ") or vacantes[id]["titulo"]
    #         vacantes[id]["descripcion"] = input("Ingresá la nueva descripción (dejalo vacío para no modificar): ") or vacantes[id]["descripcion"]
    #         vacantes[id]["condicion_contratacion"] = input("Ingresá la nueva condición de contratación (dejalo vacío para no modificar): ") or vacantes[id]["condicion_contratacion"]
    #         vacantes[id]["se_considera"] = input("Ingresá otros datos de la vacante (dejalo vacío para no modificar): ") or vacantes[id]["se_considera"]
    #         print("Vacante modificada correctamente.")
    #     else:
    #         print("No se han realizado modificaciones.")
    # else:
    #     print("La vacante con ese ID no existe en la base de datos.")

    


#    while True:
#        
#        print("\nQUE DATOS DESEA MODIFICAR? Elija una opción:")
#        print("1. Título")
#        print("2. Descripción")
#        print("3. Condición de contratación")
#        print("4. Consideraciones para la vacante")
#        print("5. Terminar modificación")
#
#        opcion = input("Seleccione una opción (1-5): ")
#
#        if opcion == "1" and flag_uno:
#            nvo_titulo = input("Ingresá el nuevo título: ")
#    
#        elif opcion == "2":
#            nva_desc = input("Ingresá la nueva descripción: ")
#
#        elif opcion == "3":
#            nva_condicion = input("Ingresá la nueva condición de contratación: ")
#
#        elif opcion == "4":
#            nvo_seconsidera = input("Ingresá otros datos de la vacante: ") 
#
#        elif opcion == "5":
#            break
#        else:
#            print("Opción no válida. Intentá nuevamente. Es posible que ya modificaste ese dato")
    