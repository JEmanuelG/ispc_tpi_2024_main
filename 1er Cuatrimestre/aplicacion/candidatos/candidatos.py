

def ver_candidatos():

    import mysql.connector
    postulantes_cba = None
    conexion = mysql.connector.connect(user='root',
                                    password='123456',
                                    host='localhost',
                                    database="data_human´s"
                                    )

    cursor = conexion.cursor()
    
    cursor.execute("SELECT * FROM postulante")
    postulantes = cursor.fetchall()
    
    print('\nLista de candidatos:\n')
    for postulante in postulantes:
        print("\n")
        print(f"Nombre y apellido: {postulante[2]}, {postulante[3]}")
        print(f"Nivel academico: {postulante[6]}")
        print(f"Puesto deseado: {postulante[8]}")
        print("-"*50)
    