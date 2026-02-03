import time

def print_esquema_tabla(titulo, descripcion, campos):
    """
    Imprime el esquema de una tabla con su descripción y campos.
    
    Args:
        titulo (str): Título de la tabla.
        descripcion (str): Descripción de la tabla.
        campos (list): Lista de listas con los campos de la tabla.
    """
    ancho_campo = 20
    ancho_tipo = 15
    ancho_escala = 20
    ancho_rol = 25
    ancho_total = ancho_campo + ancho_tipo + ancho_escala + ancho_rol + 9
    print("=" * ancho_total)
    print(f"### {titulo}")
    print(descripcion)
    print("-" * ancho_total)
    encabezados = campos[0]
    print(
        f"| {encabezados[0]:<{ancho_campo}} | {encabezados[1]:<{ancho_tipo}} | {encabezados[2]:<{ancho_escala}} | {encabezados[3]:<{ancho_rol}} |"
    )
    separador = "-" * (ancho_campo + ancho_tipo + ancho_escala + ancho_rol + 9)
    print(f"+{separador}+")
    for fila in campos[1:]:
        print(
            f"| {fila[0]:<{ancho_campo}} | {fila[1]:<{ancho_tipo}} | {fila[2]:<{ancho_escala}} | {fila[3]:<{ancho_rol}} |"
        )
    print(f"+{separador}+")
    print("\n")



tabla_clientes_desc = """
Definición: Tabla maestra que almacena todos los datos de las personas registradas en la tienda.
"""
tabla_clientes_campos = [
    ["Campo", "Tipo de Dato", "Escala de Medida", "Rol en la BD"],
    ["id_cliente", "int", "Nominal", "Clave Principal (PK)"],
    ["nombre_cliente", "str", "Nominal", "Atributo"],
    ["email", "str", "Nominal", "Atributo"],
    ["ciudad", "str", "Nominal", "Atributo"],
    ["fecha_alta", "date", "Intervalo", "Atributo"]
]
tabla_ventas_desc = """
Definición: Es la "cabecera" de cada transacción. Contiene información general de la compra, como la fecha y el método de pago. Se relaciona con la tabla Clientes a través de id_cliente.
"""
tabla_ventas_campos = [
    ["Campo", "Tipo de Dato", "Escala de Medida", "Rol en la BD"],
    ["id_venta", "int", "Nominal", "Clave Principal (PK)"],
    ["fecha", "date", "Intervalo", "Atributo"],
    ["id_cliente", "int", "Nominal", "Clave Foránea (FK)"],
    ["nombre_cliente", "str", "Nominal", "Atributo"],
    ["email", "str", "Nominal", "Atributo"],
    ["medio_pago", "str", "Nominal", "Atributo"]
]
tabla_productos_desc = """
Definición: Tabla maestra que contiene el catálogo de artículos que vende la tienda.
"""
tabla_productos_campos = [
    ["Campo", "Tipo de Dato", "Escala de Medida", "Rol en la BD"],
    ["id_producto", "int", "Nominal", "Clave Principal (PK)"],
    ["nombre_producto", "str", "Nominal", "Atributo"],
    ["categoria", "str", "Nominal", "Atributo"],
    ["precio_unitario", "int", "Razón", "Atributo"]
]
tabla_detalle_ventas_desc = """
Definición: El corazón de los datos. Esta tabla relaciona cada venta con los productos específicos que se llevaron, las cantidades y los ingresos generados. Permite los cálculos de Monto Monetario y Asociación de Productos.
"""
tabla_detalle_ventas_campos = [
    ["Campo", "Tipo de Dato", "Escala de Medida", "Rol en la BD"],
    ["id_venta", "int", "Nominal", "Clave Compuesta (PK/FK)"],
    ["id_producto", "int", "Nominal", "Clave Compuesta (PK/FK)"],
    ["nombre_producto", "str", "Nominal", "Atributo"],
    ["cantidad", "int", "Razón", "Atributo"],
    ["precio_unitario", "int", "Razón", "Atributo"],
    ["importe", "int", "Razón", "Métrica"]
]

def mostrar_documentacion_general():
    while True:
        print("\nDocumentación General:")
        print("1. Tema")
        print("2. Problema")
        print("3. Solución")
        print("4. Hacer para atras.")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            print("\nTema: Tienda Aurelion opera como un E-commerce (Comercio Electrónico). El objetivo del proyecto es potenciar su estrategia" \
            " digital usando los datos de las ventas para optimizar la inversión en marketing, la gestión " \
            "de inventario y la relación con el cliente. El éxito depende de entender la experiencia digital a través del análisis de datos.")
            time.sleep(3)
        elif opcion == '2':
            print("\nProblema: El proyecto aborda dos problemas clave: 1) La falta de un sistema para identificar y segmentar a los clientes más valiosos (lo que causa marketing ineficiente). " \
            "2) La ineficiencia en la oferta de productos al desconocer su rendimiento combinado y las oportunidades de venta cruzada.")
            time.sleep(3)
        elif opcion == '3':
            print("""\nSolución: La solución consiste en un Marco de Análisis Descriptivo en dos pilares:
1-Cliente (Problema 1): Clasificar clientes (VIP, Promesa, Dormido) usando métricas F-M-P (Frecuencia, Monto, Preferencia) para personalizar el marketing.
2-Producto (Problema 2): Optimizar la gestión de inventario (productos más/menos vendidos) e impulsar la venta cruzada analizando los productos comprados juntos.""")
            time.sleep(3)
        if opcion == '4':
            break
        

def mostrar_fuente_datos():
    mostrar = """
La información de la Tienda Aurelion proviene de dos sistemas principales:
1-Punto de Venta (POS): Genera las tablas dinámicas de Ventas, Detalle_ventas y Productos (las transacciones).

2-Gestión de Clientes (CRM): Proporciona la tabla estática de Clientes (datos de registro y contacto).

Esta estructura de datos es el registro completo de la operación de E-commerce (Clientes, Productos, Ventas y Detalle_ventas).
"""
    print(mostrar)
    time.sleep(3)
def mostrar_estructura_tablas():
    print_esquema_tabla("Clientes", tabla_clientes_desc, tabla_clientes_campos)
    print_esquema_tabla("Ventas", tabla_ventas_desc, tabla_ventas_campos)
    print_esquema_tabla("Productos", tabla_productos_desc, tabla_productos_campos)
    print_esquema_tabla("Detalle_ventas", tabla_detalle_ventas_desc, tabla_detalle_ventas_campos)
    time.sleep(3)
def mostrar_metodologia_pasos():
    resumen = """
El programa Python funciona como una Interfaz Interactiva de Consulta.
Su propósito es mostrar toda la documentación del proyecto (Tema, Problema, Solución, Estructura de Datos y Sugerencias) 
a través de un menú principal en la consola, permitiendo al usuario navegar de forma cíclica y organizada.
--- Pasos Clave ---
1.  **Inicio y Menú:** El programa se inicia y entra en un bucle que muestra el menú principal (7 opciones).
2.  **Captura y Lógica:** Lee la opción del usuario y ejecuta una lógica condicional (IF-ELSE) para llamar a la función de documentación correspondiente.
3.  **Fin:** El usuario selecciona la Opción 7 para salir del bucle y terminar el programa.

"""
    print(resumen)
    time.sleep(3)
def mostrar_copilot_sugerencias():
    sugerencias = """
Las sugerencias de Copilot buscan optimizar el código Python (mejorar la legibilidad con diccionarios para constantes y estructuras) y mejorar 
la documentación (aumentar la claridad visual usando tablas Markdown para las métricas F-M-P y añadiendo resúmenes ejecutivos para los problemas clave).
"""
    print(sugerencias)
    time.sleep(3)

def main():
    
    while True:
        
        print("\n" + "*"*50)
        print("  MENÚ DE CONSULTA - PROYECTO TIENDA AURELION")
        print("*"*50)
        print("1. Mostrar Documentación General (Tema, Problema, Solución)")
        print("2. Fuente de datos y Descripción")
        print("3. Mostrar Estructura de Tablas (Clientes, Ventas, Productos)")
        print("4. Mostrar Metodología y Pasos (Pasos, Pseudocódigo)")
        print("5. Mostrar Sugerencias de Copilot")
        print("6. Mostrar Integrantes de equipo")
        print("7. Salir del Programa")
        print("*"*50)

        
        opcion = input("Ingrese el número de la opción deseada (1-7): ")

        
        if opcion == '1':
            mostrar_documentacion_general()
        elif opcion == '2':
            mostrar_fuente_datos()
        elif opcion == '3':
            mostrar_estructura_tablas()
        elif opcion == '4':
            mostrar_metodologia_pasos()
        elif opcion == '5':
            mostrar_copilot_sugerencias()
        elif opcion == '6':
            print("\nIntegrantes del equipo:")
            print("1. Nicolas Cook")
            print("2. Marco Huanca")
            print("3. Valeria Belen")
            print("4. Uriel Romero")
            time.sleep(3)
        elif opcion == '7':
            print("\nGracias por consultar la documentación. ¡Hasta luego!")
            break  
        else:
            print("\n*** ERROR: Opción no válida. Por favor, ingrese un número del 1 al 7. ***")
            time.sleep(1) 


main()