# Función para solicitar una base y una altura y graficar un rectángulo

def mostrarRectangulo():
     
    base = int(input("Ingrese por favor la base o el ancho: "))
    altura = int(input("Ingrese por favor la altura: "))
     
    print("Tenemos en cuenta que el área de un rectángulo es base * altura, y que su perímetro se calcula como: Perimetro = 2 * base + 2 * altura")
    
# Se realizan las fórmulas de área y perímetro: 

    a = base * altura
    p = 2 * base + 2 * altura
    
    print(f"El área del rectángulo es: {a} y su perímetro es: {p}")
     
    for i in range(base):
        linea = ""
        for j in range(altura):
            linea += "*" # Agregar un asterisco a la línea
        print(linea) # Imprimir la línea en la consola

# Se llama a la función: 

mostrarRectangulo()
