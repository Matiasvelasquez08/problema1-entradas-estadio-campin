# Programa para calcular el total a pagar en entradas al estadio El Campín
#-----------------------------------
#Nombre: Matias felipe velasquez
#Codigo y Grupo: 213022-270
#Carrera: Ingenieria de Sistemas
#Codigo de fuente: autoria propia
#-----------------------------------

def main():
    print("="*50)
    print("ESTADIO EL CAMPÍN - CALCULADORA DE ENTRADAS")
    print("="*50)
    
   
    print("\nSectores disponibles:")
    print("A - Norte alta: $15,000")
    print("B - Norte baja: $13,000") 
    print("C - Oriental alta: $10,000")
    print("D - Occidental alta: $11,000")
    print("E - Exclusivo: $20,000")
    print("-"*50)
    
   
    sector = input("\nIngrese el código del sector (A, B, C, D, E): ").upper().strip()
    
   
    precio_unitario = 0
    nombre_sector = ""
    
    if sector == "A":
        precio_unitario = 15000
        nombre_sector = "Norte alta"
    elif sector == "B":
        precio_unitario = 13000
        nombre_sector = "Norte baja"
    elif sector == "C":
        precio_unitario = 10000
        nombre_sector = "Oriental alta"
    elif sector == "D":
        precio_unitario = 11000
        nombre_sector = "Occidental alta"
    elif sector == "E":
        precio_unitario = 20000
        nombre_sector = "Exclusivo"
    else:
        print("❌ Error: Código de sector inválido")
        return
    
    
    try:
        cantidad = int(input("Ingrese la cantidad de entradas: "))
        
     
        if cantidad <= 0:
            print("❌ Error: La cantidad debe ser un número entero positivo")
            return
            
    except ValueError:
        print("❌ Error: La cantidad debe ser un número entero positivo")
        return
    
    
    total_pagar = precio_unitario * cantidad
    
    
    print("\n" + "="*50)
    print("RESUMEN DE COMPRA")
    print("="*50)
    print(f"Sector: {sector} - {nombre_sector}")
    print(f"Precio Unitario de la boleta: ${precio_unitario:,}")
    print(f"Cantidad de entradas compradas: {cantidad}")
    print(f"Total a pagar: ${total_pagar:,}")
    print("="*50)
    print("¡Gracias por elegir el Estadio El Campín!")


if __name__ == "__main__":
    main()
