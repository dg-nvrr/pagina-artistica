import os

# --- Req 6: Funciones y modularización ---
def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def mostrar_menu():
    print("\n--- GESTIÓN DE ARTE ---")
    print("1. Ver catálogo")
    print("2. Cotizar (con IVA)")
    print("3. Agregar obra")
    print("4. Salir")

# --- Req 1: Variables y operadores ---
iva = 0.19

# --- Req 5: Listas y Diccionarios ---
obras = [
    {"titulo": "Atardeceres", "precio": 150000, "tipo": "Pintura"},
    {"titulo": "Colgante Lunar", "precio": 45000, "tipo": "Orfebreria"},
    {"titulo": "Abstracción III", "precio": 80000, "tipo": "Mixta"}
]

# --- Req 4: Bucle While ---
ejecutando = True

while ejecutando:
    mostrar_menu()
    
    # --- Req 2: Tipos de datos (Input) ---
    opcion = input("\nOpción: ")

    # --- Req 3: Condicionales (If/Elif) ---
    if opcion == "1":
        limpiar_pantalla()
        for obra in obras:
            print(f"- {obra['titulo']} ({obra['tipo']}): ${obra['precio']}")
            
    elif opcion == "2":
        try:
            base = float(input("Precio base: "))
            final = base * (1 + iva)
            print(f"Total con IVA: ${final:,.0f}")
        except ValueError:
            print("Error: Ingrese un número.")

    elif opcion == "3":
        nombre = input("Nombre: ")
        tipo = input("Tipo: ")
        obras.append({"titulo": nombre, "precio": 0, "tipo": tipo})
        print("Guardado.")

    elif opcion == "4":
        print("Saliendo...")
        ejecutando = False
    else:
        print("Opción inválida.")

        print("--- Fin de la ejecución. Sistema desarrollado por Dg-nvrr. ---")

        # --- Codigo revisado y listo para echar a andar ---