import os

# --- Req 6: Funciones y modularización ---
def limpiar_pantalla():
    # Detecta el sistema operativo para limpiar consola
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def mostrar_menu():
    print("\n--- GESTIÓN DE ARTE (v2.0) ---")
    print("1. Ver catálogo")
    print("2. Cotizar obra (con IVA)")
    print("3. Agregar nueva obra")
    print("4. Ver estadísticas de inventario") # ¡NUEVO!
    print("5. Salir")

# Función nueva para calcular totales
def mostrar_estadisticas(lista_obras):
    cantidad = len(lista_obras)
    valor_total = sum(obra['precio'] for obra in lista_obras)
    print(f"\n--- ESTADÍSTICAS ---")
    print(f"Obras en catálogo: {cantidad}")
    print(f"Valor total del inventario: ${valor_total:,.0f}")
    input("\nPresione Enter para continuar...")

# --- Req 1: Variables y operadores ---
iva = 0.19

# --- Req 5: Listas y Diccionarios ---
obras = [
    {"titulo": "Atardeceres", "precio": 150000, "tipo": "Pintura"},
    {"titulo": "Colgante Lunar", "precio": 45000, "tipo": "Orfebreria"},
    {"titulo": "Abstracción III", "precio": 80000, "tipo": "Mixta"}
]

# --- Req 4: Bucle While Principal ---
ejecutando = True

while ejecutando:
    mostrar_menu()
    
    # --- Req 2: Tipos de datos (Input) ---
    opcion = input("\nSeleccione una opción: ")

    # --- Req 3: Condicionales (If/Elif) ---
    if opcion == "1":
        limpiar_pantalla()
        print("\n--- CATÁLOGO ---")
        for i, obra in enumerate(obras, 1):
            print(f"{i}. {obra['titulo']} ({obra['tipo']}): ${obra['precio']:,.0f}")
            
    elif opcion == "2":
        try:
            base = float(input("Ingrese precio base de la obra: "))
            final = base * (1 + iva)
            print(f"--> Precio final con IVA (19%): ${final:,.0f}")
        except ValueError:
            print("¡Error! Debe ingresar un número válido.")

    elif opcion == "3":
        print("\n--- NUEVA OBRA ---")
        nombre = input("Título: ")
        tipo = input("Técnica/Tipo: ")
        try:
            precio = int(input("Precio neto: "))
            obras.append({"titulo": nombre, "precio": precio, "tipo": tipo})
            print("¡Obra guardada exitosamente!")
        except ValueError:
            print("Error: El precio debe ser un número entero.")

    elif opcion == "4": # Nueva funcionalidad
        mostrar_estadisticas(obras)

    elif opcion == "5":
        print("Cerrando sistema...")
        ejecutando = False
    else:
        print("Opción no válida, intente nuevamente.")

        print("--- Fin de la ejecución. Sistema desarrollado por Dg-nvrr. ---")

        # --- Codigo revisado y listo para echar a andar ---