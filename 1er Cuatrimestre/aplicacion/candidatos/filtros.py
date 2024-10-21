
def filtrar_por_requisitos():
    import mysql.connector
    postulantes_cba = None
    conexion = mysql.connector.connect(user='root',
                                    password='123456',
                                    host='localhost',
                                    database="data_human´s"
                                    )

    cursor = conexion.cursor()

    
    while True:
        print('\nFiltrar por:\n')

        print("1. Residencia en Cordoba")
        print("2. Nivel academico")
        print("3. Puesto deseado")
        print("4. Volver al menú principal")
        print("\n\n")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            cursor.execute("SELECT * FROM postulante WHERE Residencia = 'Cordoba'")
            postulantes_cba = cursor.fetchall()

            for postulante in postulantes_cba:
                print("\n")
                print(f"Nombre y apellido: {postulante[2]}, {postulante[3]}")
                print(f"Nivel academico: {postulante[6]}")
                print(f"Puesto deseado: {postulante[8]}")
                print("-"*50)
            input("PRESIONE UNA TECLA PARA CONTINUAR...")

        elif opcion == "2":
            print("""\nSelecciona el nivel académico
                    \n1. Secundarios
                    \n2. Universitarios""")
            
            nvl_academico = int(input("Ingresa opción: "))
            
            if nvl_academico == 1:
                cursor.execute("SELECT * FROM postulante WHERE Nivelacademico = 'Secundarios'")
                postulantes_cba = cursor.fetchall()

            elif nvl_academico == 2:
                cursor.execute("SELECT * FROM postulante WHERE Nivelacademico = 'Universitarios'")
                postulantes_cba = cursor.fetchall()

            for postulante in postulantes_cba:
                print("\n")
                print(f"Nombre y apellido: {postulante[2]}, {postulante[3]}")
                print(f"Nivel academico: {postulante[6]}")
                print(f"Puesto deseado: {postulante[8]}")
                print("-"*50)
            input("PRESIONE UNA TECLA PARA CONTINUAR...")

        elif opcion == "3":
            print("""\nSelecciona tipo de puesto
                    \n1. Vendedor
                    \n2. Maestranza
                    \n3. Administrativo
                    \n4. Productor""")
            
            puesto = int(input("Ingresa opción: "))
            
            if puesto == 1:
                cursor.execute("SELECT * FROM postulante WHERE Puestodeseado = 'Vendedor'")
                postulantes_cba = cursor.fetchall()

            elif puesto == 2:
                cursor.execute("SELECT * FROM postulante WHERE Puestodeseado = 'Maestranza'")
                postulantes_cba = cursor.fetchall()
            
            elif puesto == 3:
                cursor.execute("SELECT * FROM postulante WHERE Puestodeseado = 'Administrativo'")
                postulantes_cba = cursor.fetchall()
            
            elif puesto == 4:
                cursor.execute("SELECT * FROM postulante WHERE Puestodeseado = 'Productor'")
                postulantes_cba = cursor.fetchall()

            for postulante in postulantes_cba:
                print("\n")
                print(f"Nombre y apellido: {postulante[2]}, {postulante[3]}")
                print(f"Nivel academico: {postulante[6]}")
                print(f"Puesto deseado: {postulante[8]}")
                print("-"*50)
            input("PRESIONE UNA TECLA PARA CONTINUAR...")
    
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intentá nuevamente.")

    conexion.close()