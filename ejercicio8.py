# Define una función llamada es_par que tome un número entero como parámetro y devuelva
# True si el número es par y False si es impar. Invócala con diferentes números y
# muestra los resultados.
# def es_par(numero):
#     if numero % 2 == 0:
#         return True
#     else:
#         return False
#
#
# print(es_par(457))

# Crea una función llamada factorial que calcule el factorial de un número entero no negativo.
# Utiliza un bucle para calcular el factorial y devuelve el resultado.
# Prueba la función con varios valores.

# def factorial():
#     numero = int(input("dime un numero no negativo:\n"))
#     if numero < 0:
#         print("Error: El número tiene que ser positivo.")
#         return
#     resultado = 1
#     for i in range(1, numero + 1):
#         resultado *= i
#     print(resultado)
#
#
# factorial()

#
# Define una función llamada fibonacci que genere una lista con los primeros
# n números de la secuencia de Fibonacci.
# La función debe tomar un parámetro n y devolver la lista correspondiente.
# Invoca la función con diferentes valores de n y muestra los resultados.
# def fibonacci(n):
#     if n <= 0:
#         return []  # Si n es 0 o negativo, devolvemos una lista vacía
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
#
#     secuencia = [0, 1]
#     for i in range(2, n):
#         siguiente = secuencia[-1] + secuencia[-2]
#         secuencia.append(siguiente)
#
#     return secuencia
#
#
# print(fibonacci(9))
#
#
# Crea una función llamada es_palindromo que verifique si una cadena de texto es un palíndromo
# (se lee igual de izquierda a derecha que de derecha a izquierda).
# La función debe ignorar espacios y mayúsculas/minúsculas.
# Prueba la función con varias cadenas.
def es_palindromo(cadena):
    # Eliminamos espacios y convertimos todo a minúsculas
    cadena_limpia = cadena.replace(" ", "").lower()

    # Comprobamos si la cadena es igual a su reverso
    return cadena_limpia == cadena_limpia[::-1]


print(es_palindromo("hghghghgh"))
#
#
# Define una función llamada calcular_area_circulo que tome el radio de un círculo
# como parámetro y devuelva el área del círculo utilizando la fórmula área = π * radio^2.
# Utiliza la constante math.pi para obtener el valor de π.
# Invoca la función con diferentes radios y muestra los resultados.
import math


def calcular_area_circulo(radio):
    if radio < 0:
        return "Error: el radio no puede ser negativo."
    return math.pi * radio ** 2


#
#
# Crea una función llamada contar_vocales que tome una cadena de texto
# como parámetro y devuelva el número de vocales presentes en la cadena.
# La función debe contar tanto vocales mayúsculas como minúsculas.
# Prueba la función con varias cadenas.
def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in cadena:
        if letra in vocales:
            contador += 1
    return contador


#
#
# Define una función llamada ordenar_lista que tome una lista de números como
# parámetro y devuelva una nueva lista con los números ordenados de menor a mayor.
# Utiliza el método de ordenación incorporado de Python. Invoca la función con diferentes
# listas y muestra los resultados.
#
def ordenar_lista(lista_numeros):
    return sorted(lista_numeros)


# Crea un programa que muestre el menú con cinco opciones (del 1 al 5):
# sumar, restar, multiplicar, dividir, y salir. El usuario debe poder seleccionar una opción y
# proporcionar los números necesarios para realizar la operación. Muestra el resultado de la operación
# hasta que se seleccione la opción de salir. Evita el uso de variables globales y utiliza funciones
# para cada operación. Evita los errores en la medida de lo posible.
def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre 0."
    return a / b


def mostrar_menu():
    print("\n--- MENÚ DE OPERACIONES ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")


def obtener_numero(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Debes ingresar un número válido.")


def calculadora():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "5":
            print("¡Hasta luego!")
            break
        elif opcion in ["1", "2", "3", "4"]:
            num1 = obtener_numero("Ingresa el primer número: ")
            num2 = obtener_numero("Ingresa el segundo número: ")

            if opcion == "1":
                resultado = sumar(num1, num2)
            elif opcion == "2":
                resultado = restar(num1, num2)
            elif opcion == "3":
                resultado = multiplicar(num1, num2)
            elif opcion == "4":
                resultado = dividir(num1, num2)

            print(f"El resultado es: {resultado}")
        else:
            print("Opción no válida. Intenta de nuevo.")


# Ejecutar la calculadora
calculadora()
