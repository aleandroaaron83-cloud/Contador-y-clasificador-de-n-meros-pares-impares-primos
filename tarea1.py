# Contador y clasificador de números
# Clasifica una lista de números como pares, impares o primos
# Función para verificar si un número es primo
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Función principal para clasificar los números
def clasificar_numeros(lista_numeros):
    pares = []
    impares = []
    primos = []

    for num in lista_numeros:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

        if es_primo(num):
            primos.append(num)

    return {
        "pares": pares,
        "impares": impares,
        "primos": primos
    }

# Programa principal
if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17]
    resultado = clasificar_numeros(numeros)

    print("Números ingresados:", numeros)
    print("Números pares:", resultado["pares"])
    print("Números impares:", resultado["impares"])
    print("Números primos:", resultado["primos"])