Algoritmo seleccion_personal
	Definir edad, residencia, estudios Como Entero
	
    Escribir "Bienvenido al sistema de selecci�n de personal."
    Escribir "Por favor, ingrese la siguiente informaci�n:"
	
    Escribir "1) Edad (en años):"
    Leer edad
	
    Escribir "2) Residencia (1 si es en la Ciudad de Córdoba, 0 si no lo es):"
    Leer residencia
	
    Escribir "3) Estudios secundarios completos (1 si s�, 0 si no):"
    Leer estudios
	
    Si (edad >= 18) Y (residencia = 1) Y (estudios = 1) Entonces
        Escribir "�Felicidades! Cumple con los requisitos para el puesto."
    Sino
        Escribir "Lo sentimos, no cumple con los requisitos para el puesto."
    FinSi
	
FinAlgoritmo
