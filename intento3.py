def calcular_promedio():
    print("Calcula el promedio de una serie de números")
    numeros = []
    print("Ingresa números (ingresa -1 para terminar):")
    
    while True:
        num = float(input("Número: "))
        if num == -1:
            break
        numeros.append(num)
    
    if len(numeros) == 0:
        print("\nNo se ingresaron números")
        return
    
    promedio = sum(numeros) / len(numeros)
    print(f"\nSe ingresaron {len(numeros)} números")
    print(f"El promedio es: {promedio}")