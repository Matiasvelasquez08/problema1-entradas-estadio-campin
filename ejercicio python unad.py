#-----------------------------------
#Nombre: Matias felipe velasquez
#Codigo y Grupo: 213022-270
#Carrera: Ingenieria de Sistemas
#Codigo de fuente: autoria propia
#-----------------------------------
#programa para comprar una entrada al estadio el campin
def mostrar_sectores():
    
    print("\n" + "="*50)
    print("    ESTADIO EL CAMPÍN - SECTORES DISPONIBLES")
    print("="*50)
    sectores = {
        'A': ('Norte alta', 15000),
        'B': ('Norte baja', 13000),
        'C': ('Oriental alta', 10000),
        'D': ('Occidental alta', 11000),
        'E': ('Exclusivo', 20000)
    }
    
    for codigo, (nombre, precio) in sectores.items():
        print(f"  {codigo} - {nombre:<18} ${precio:,}")
    print("="*50)
    return sectores

def validar_cantidad():
   
    while True:
        try:
            cantidad = input("\nIngrese la cantidad de entradas: ")
            cantidad = int(cantidad)
            
            if cantidad <= 0:
                print("❌ Error: La cantidad debe ser un número entero positivo.")
                continue
                
            return cantidad
            
        except ValueError:
            print("❌ Error: Por favor ingrese un número entero válido.")

def seleccionar_sector(sectores):
    
    while True:
        sector = input("\nSeleccione el sector (A, B, C, D, E): ").upper().strip()
        
        if sector in sectores:
            return sector
        else:
            print("❌ Error: Sector no válido. Por favor seleccione A, B, C, D o E.")

def calcular_total():
    
    print("  SISTEMA DE VENTA DE ENTRADAS - ESTADIO EL CAMPÍN")
    
    
    sectores = mostrar_sectores()
    
   
    sector_codigo = seleccionar_sector(sectores)
    sector_nombre, precio_unitario = sectores[sector_codigo]
    
    
    cantidad = validar_cantidad()
    
    
    total = precio_unitario * cantidad
    
   
    print("\n" + "="*50)
    print("           RESUMEN DE COMPRA")
    print("="*50)
    print(f"  Sector seleccionado: {sector_codigo} - {sector_nombre}")
    print(f"  Precio unitario:     ${precio_unitario:,}")
    print(f"  Cantidad de entradas: {cantidad}")
    print("-"*50)
    print(f"  TOTAL A PAGAR:       ${total:,}")
    print("="*50)
    
    return total

def main():
    
    while True:
        try:
            calcular_total()
            
            continuar = input("\n¿Desea realizar otra compra? (s/n): ").lower().strip()
            if continuar not in ['s', 'si', 'sí', 'y', 'yes']:
                print("\n¡Gracias por usar el sistema de venta de entradas!")
                break
                
        except KeyboardInterrupt:
            print("\n\n¡Gracias por usar el sistema de venta de entradas!")
            break
        except Exception as e:
            print(f"\n❌ Error inesperado: {e}")
            print("Intente nuevamente.")

if __name__ == "__main__":

    main()
