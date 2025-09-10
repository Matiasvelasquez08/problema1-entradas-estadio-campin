# Programa para calcular el total a pagar en entradas al estadio El Campín
#-----------------------------------
#Nombre: Matias felipe velasquez
#Codigo y Grupo: 213022-270
#Carrera: Ingenieria de Sistemas
#Codigo de fuente: autoria propia
#-----------------------------------

print("=" * 50)
print("    ESTADIO EL CAMPÍN - CALCULADORA DE ENTRADAS")
print("=" * 50)


sectores = {
    'A': {'nombre': 'Norte Alta', 'precio': 15000},
    'B': {'nombre': 'Norte Baja', 'precio': 13000},
    'C': {'nombre': 'Oriental Alta', 'precio': 10000},
    'D': {'nombre': 'Occidental Alta', 'precio': 11000},
    'E': {'nombre': 'Exclusivo', 'precio': 20000}
}


print("\nSECTORES DISPONIBLES:")
print("-" * 30)
for codigo, info in sectores.items():
    print(f"{codigo} - {info['nombre']}: ${info['precio']:,}")


while True:
    sector_elegido = input("\nIngrese el código del sector (A, B, C, D, E): ").upper().strip()
    
    if sector_elegido in sectores:
        break
    else:
        print("Error: Código de sector inválido. Por favor ingrese A, B, C, D o E.")


while True:
    try:
        cantidad_str = input("Ingrese la cantidad de entradas: ").strip()
        cantidad = int(cantidad_str)
        
        # Validar que sea un entero positivo
        if cantidad > 0:
            break
        else:
            print("Error: La cantidad debe ser un número entero positivo.")
    except ValueError:
        print("Error: Por favor ingrese un número entero válido.")


precio_unitario = sectores[sector_elegido]['precio']
total_pagar = precio_unitario * cantidad


print("\n" + "=" * 50)
print("           RESUMEN DE COMPRA")
print("=" * 50)
print(f"Sector seleccionado: {sector_elegido} - {sectores[sector_elegido]['nombre']}")
print(f"Precio unitario de la boleta: ${precio_unitario:,}")
print(f"Cantidad de entradas compradas: {cantidad}")
print(f"Total a pagar: ${total_pagar:,}")
print("=" * 50)
print("¡Gracias por su compra!")
