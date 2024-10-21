from candidatos.candidatos import ver_candidatos
from candidatos.filtros import filtrar_por_requisitos
from vacante.create import cargar_vacante
from vacante.update import modificar_vacante
from vacante.delete import eliminar_vacante
from vacante.read import ver_vacantes


def seleccion_personal():
    while True:
        print("\n--- MENÚ DE SELECCIÓN DE PERSONAL ---")
        print("1. Ver todos los candidatos")
        print("2. Ver coincidencias")
        print("3. Cargar vacante")
        print("4. Modificar vacante")
        print("5. Eliminar vacante")
        print("6. Ver todas las vacantes")
        print("7. Salir")

        opcion = input("Seleccione una opción (1-7): ")

        if opcion == "1":
            ver_candidatos()
            input("Presiona una tecla para continuar...")
        elif opcion == "2":
            filtrar_por_requisitos()
            input("Presiona una tecla para continuar...")
        elif opcion == "3":
            cargar_vacante()
            input("Presiona una tecla para continuar...")
        elif opcion == "4":
            modificar_vacante()
            input("Presiona una tecla para continuar...")
        elif opcion == "5":
            eliminar_vacante()
            input("Presiona una tecla para continuar...")
        elif opcion == "6":
            ver_vacantes()
            input("Presiona una tecla para continuar...")
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intentá nuevamente.")


if __name__ == "__main__":
    seleccion_personal()


# MODULARIZAR CONEXION CON BASE DE DATOS
# HACER VALIDACIONES DE DATOS, SI EXISTEN, SI SON LOS DATOS ESPERADOS, ETC
# corregir script sql id unique