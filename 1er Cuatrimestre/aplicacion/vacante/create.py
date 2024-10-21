

# contador_id = 1 # Generador manual de IDs

# el id se puedo configurar directamente en SQL como AUTO_INCREMENT y a medida que hacemos registros le asigna el id siguiente

def cargar_vacante():
    import mysql.connector
    
    print('\nDatos de la nueva vacante:\n')

    cuit = int(input("Ingresa el CUIT de tu empresa (Sin puntos ni guiones 11 digitos): "))
    titulo_puesto = input("\nIngresá el título del puesto vacante: ")
    descripcion = (input("Ingresá una descripción: "))
    condicion_contratacion = input("Ingresá las condiciones de contratación (Temporal/Permanente): ")
    experiencia = input("Se requiere experiencia?")
    excluyente = input("Condiciones excluyentes:")
    se_considera = str(input("Otras consideraciones del puesto:"))
    cant_vacantes = int(input("Cuantas vacantes hay disponibles?:"))
    fecha = input("Ingresa la fecha actual (Formato AAAA-MM-DD):")


    # global contador_id
    # id = contador_id
    # contador_id += 1 # Incrementar el ID para la próxima vacante a agregar
    # vacantes[id] = {"titulo": titulo, "descripcion": descripcion, "id": id,
    #                 "condicion_contratacion": condicion_contratacion, "se_considera": se_considera}
    # print("Vacante agregada correctamente.")

    # consultamos DB para sacar el ultimo id de vacante

# ------------------------------- CONECTAR CON DB ---------------------------------------

    conexion = mysql.connector.connect(user='root',
                                    password='123456',
                                    host='localhost',
                                    database="data_human´s"
                                    )

    cursor = conexion.cursor()

    cursor.execute(f"SELECT Id_empresa FROM empresa WHERE Cuit = {cuit}")    

    id_empresa = cursor.fetchall()

    id_empresa = id_empresa[0][0]


    cursor.execute(f"SELECT MAX(Id_vacantes) FROM vacantes") # CONSULTA EL ULTIMO ID DE VACANTE CARGADO

    ultimo_id_vacante = cursor.fetchall()   

    nuevo_id_vacante = ultimo_id_vacante[0][0]

    nuevo_id_vacante += 1 # LE SUMA UNA UNIDAD AL ULTIMO ID DE VACANTE PARA GENERAR ID PARA LA NUEVA CARGA


    cursor.execute(f'''INSERT INTO vacantes (Id_vacantes,
                                            Id_empresa,
                                            Cantvacantes,
                                            Titulopuesto,
                                            Id_caractpuesto,
                                            Fechavacantes,
                                            Id_formulario) 
                                    VALUES ({nuevo_id_vacante},
                                            {id_empresa},
                                            {cant_vacantes},
                                            '{titulo_puesto}',
                                            {nuevo_id_vacante},
                                            '{fecha}', 
                                            {nuevo_id_vacante})''')


    conexion.commit()
# POR ALGUNA RAZON NO LE PUEDO PASAR EL PARAMETRO titulo_puesto y fecha, ME LANZA ERROR, por ahora pongo los datos dirctamente en el cod

    cursor.execute(f'''INSERT INTO caracteristicaspuesto (Id_caractpuesto,
                                                        Id_vacantes,
                                                        Descripcion,
                                                        Condicioncontratacion,
                                                        Experiencia,
                                                        Excluyente,
                                                        Seconsidera) 
                                                VALUES ({nuevo_id_vacante},
                                                        {nuevo_id_vacante},
                                                        '{descripcion}',
                                                        '{condicion_contratacion}',
                                                        '{experiencia}',
                                                        '{excluyente}', 
                                                        '{se_considera}')''')

# carga datos pero da error al pasar variables como parametro, probar con comillas


    conexion.commit()

    conexion.close()