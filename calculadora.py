def mostrar_menu():
    print("\n" + "="*50)
    print("          PROGRAMA DE OPERACIONES MATEMÁTICAS")
    print("="*50)
    print("1. Suma de 'n' números (positivos y negativos)")
    print("2. Producto entre 'n' números")
    print("3. División entre 2 números")
    print("4. Calcular factorial (n!)")
    print("5. Tablas de multiplicar (del 1 al 10)")
    print("6. Calcular cuadrado y cubo de un número")
    print("7. Calcular promedio de una serie de números")
    print("8. Encontrar máximo y mínimo de 'n' números")
    print("9. Salir del programa")
    print("="*50)

def suma_n_numeros():
    print("\n--- SUMA DE 'N' NÚMEROS ---")
    try:
        n = int(input("¿Cuántos números desea sumar?: "))
        if n <= 0:
            print("Debe ingresar un número positivo mayor que cero.")
            return
        
        suma = 0
        for i in range(1, n + 1):
            numero = float(input(f"Ingrese el número {i}: "))
            suma += numero
        
        print(f"\nLa suma de los {n} números es: {suma}")
    except ValueError:
        print("Error: Debe ingresar un número válido.")

def producto_n_numeros():
    print("\n--- PRODUCTO DE 'N' NÚMEROS ---")
    try:
        n = int(input("¿Cuántos números desea multiplicar?: "))
        if n <= 0:
            print("Debe ingresar un número positivo mayor que cero.")
            return
        
        producto = 1
        for i in range(1, n + 1):
            numero = float(input(f"Ingrese el número {i}: "))
            producto *= numero
        
        print(f"\nEl producto de los {n} números es: {producto}")
    except ValueError:
        print("Error: Debe ingresar un número válido.")

def division_dos_numeros():
    print("\n--- DIVISIÓN ENTRE DOS NÚMEROS ---")
    try:
        dividendo = float(input("Ingrese el dividendo: "))
        divisor = float(input("Ingrese el divisor: "))
        
        if divisor == 0:
            print("Error: No se puede dividir entre cero.")
        else:
            resultado = dividendo / divisor
            print(f"\n{dividendo} ÷ {divisor} = {resultado}")
    except ValueError:
        print("Error: Debe ingresar números válidos.")

def calcular_factorial():
    print("\n--- CÁLCULO DE FACTORIAL (n!) ---")
    try:
        n = int(input("Ingrese un número entero no negativo: "))
        
        if n < 0:
            print("Error: El factorial no está definido para números negativos.")
            return
        
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        
        print(f"\n{n}! = {factorial}")
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")

def tablas_multiplicar():
    print("\n--- TABLAS DE MULTIPLICAR ---")
    try:
        tabla = int(input("Ingrese el número de tabla que desea ver (1-10): "))
        
        if tabla < 1 or tabla > 10:
            print("Error: Debe ingresar un número entre 1 y 10.")
            return
        
        print(f"\nTabla del {tabla}:")
        print("-" * 15)
        for i in range(1, 11):
            resultado = tabla * i
            print(f"{tabla} x {i:2} = {resultado:3}")
        print("-" * 15)
    except ValueError:
        print("Error: Debe ingresar un número válido.")

def calcular_cuadrado_cubo():
    print("\n--- CÁLCULO DE CUADRADO Y CUBO ---")
    try:
        numero = float(input("Ingrese un número: "))
        
        cuadrado = numero ** 2
        cubo = numero ** 3
        
        print(f"\nNúmero: {numero}")
        print(f"Cuadrado ({numero}²): {cuadrado}")
        print(f"Cubo ({numero}³): {cubo}")
    except ValueError:
        print("Error: Debe ingresar un número válido.")

def calcular_promedio():
    print("\n--- CÁLCULO DE PROMEDIO ---")
    print("Ingrese una serie de números (ingrese -1 para terminar):")
    
    numeros = []
    contador = 1
    
    while True:
        try:
            numero = float(input(f"Número {contador}: "))
            
            if numero == -1:
                break
            
            numeros.append(numero)
            contador += 1
        except ValueError:
            print("Error: Debe ingresar un número válido.")
    
    if len(numeros) == 0:
        print("No se ingresaron números para calcular el promedio.")
        return
    
    suma = sum(numeros)
    promedio = suma / len(numeros)
    
    print(f"\nTotal de números ingresados: {len(numeros)}")
    print(f"Suma total: {suma}")
    print(f"Promedio: {promedio}")

def encontrar_max_min():
    print("\n--- ENCONTRAR MÁXIMO Y MÍNIMO ---")
    try:
        n = int(input("¿Cuántos números enteros desea ingresar?: "))
        
        if n <= 0:
            print("Debe ingresar un número positivo mayor que cero.")
            return
        
        numeros = []
        for i in range(1, n + 1):
            try:
                numero = int(input(f"Ingrese el número entero {i}: "))
                numeros.append(numero)
            except ValueError:
                print("Error: Debe ingresar un número entero válido.")
                return
        
        if len(numeros) > 0:
            maximo = max(numeros)
            minimo = min(numeros)
            
            print(f"\nTotal de valores introducidos: {len(numeros)}")
            print(f"Valor máximo: {maximo}")
            print(f"Valor mínimo: {minimo}")
            print(f"Lista de números: {numeros}")
    except ValueError:
        print("Error: Debe ingresar un número válido.")

def main():
    print("¡Bienvenido al Programa de Operaciones Matemáticas!")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("\nSeleccione una opción (1-9): "))
            
            if opcion == 1:
                suma_n_numeros()
            elif opcion == 2:
                producto_n_numeros()
            elif opcion == 3:
                division_dos_numeros()
            elif opcion == 4:
                calcular_factorial()
            elif opcion == 5:
                tablas_multiplicar()
            elif opcion == 6:
                calcular_cuadrado_cubo()
            elif opcion == 7:
                calcular_promedio()
            elif opcion == 8:
                encontrar_max_min()
            elif opcion == 9:
                print("\n¡Gracias por usar el programa! ¡Hasta pronto!")
                break
            else:
                print("Error: Opción no válida. Por favor, seleccione una opción del 1 al 9.")
        
        except ValueError:
            print("Error: Debe ingresar un número válido.")
        input("\nPresione Enter para continuar...")
if __name__ == "__main__":
    main()