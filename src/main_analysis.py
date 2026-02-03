

from clustering_model import ejecutar_clustering
from regression_model import predecir_demanda

print("\n=======================================================================\n")
print("¡Bienvenido! Este es el Proyecto del Grupo 3 sobre la Tienda Aurelion. Aquí puede consultar sobre los métodos de Machine Learning utilizados." \
"\nSe han desarrollado dos modelos distintos para abordar los problemas clave del negocio: la predicción de demanda (para inventario) y la segmentación de clientes (para marketing)." \
"\nPuede navegar por las diferentes secciones del proyecto utilizando el menú interactivo a continuación.")

Problema = "1. El Problema de No Conocer a Nuestros Mejores Clientes \n 2. Ineficiencia en la Oferta de Productos (Gestión de Inventario y Promoción)"
Solucion = "Potenciar la estrategia digital de la tienda: Aprovechar la información de las ventas para dirigir de forma más inteligente y asegurar que se tiene en stock los productos más demandados (gestión de inventario) y construir una relación duradera y rentable con cada cliente."
Modelo_1 = "Predicción de demanda"
Modelo_2 = "Segmentación de clientes"
Cliente_Estandar = "599 clientes. \nComportamiento Promedio: Gasto de $10,572 y compra de 3 unidades. \nRepresentan el consumo minorista típico. El objetivo aquí es aumentar su ticket promedio mediante venta cruzada."
Cliente_Premium = "29 clientes. \nComportamiento Promedio: Gasto de $433,631 y compra de 188 unidades. \n Un grupo pequeño pero de alto valor. Probablemente pequeñas empresas o familias numerosas que requieren estrategias de retención."
Cliente_VIP = "21 clientes. \nComportamiento Promedio: Gasto de $656,400 y compra de 244 unidades. \nSon los 'socios' de la tienda. Aunque son pocos (menos del 5% de la base), generan un flujo de caja crítico. Perder a uno de estos clientes tiene un impacto financiero significativo."
Salida = "Esto es todo por ahora. Pronto tendremos más detalles del proyecto"

Opciones_menu = {"1": Problema, "2": Solucion, "3": Modelo_1, "4": Modelo_2, "5": 'Grupos_de_clientes', "6": Salida}

while True:
    print("\nEstas son las secciones del menú que puede consultar:\n 1. Problema\n 2. Solución\n 3. Primer Modelo de ML usado\n 4. Segundo Modelo de ML usado \n 5. Conformación de grupo de clientes\n 6. División train/test y entrenamiento\n 7. Cierre")

    Opciones_menu = input("Seleccione la sección que desea ver (1-7): ")
    
    if Opciones_menu == "1":
        print(Problema)
    
    elif Opciones_menu == "2":
        print(Solucion)

    elif Opciones_menu == "3":
        print(f'Se utilizó la técnica de REGRESIÓN LINEAL para hacer una {Modelo_1} \nAl observar los datos históricos de ventas, notamos una tendencia que puede explicarse a través del tiempo.')
        print("------")
        print("Elije una opcion:\n1. Ejecutar el modelo de Regresion Lineal y ver grafica\n2. Volver al menu\n")
        opcion_regresion = input("Seleccione una opción (1-2): ")
        if opcion_regresion == "1":
            while True:
                categoria = input("Seleccione una categoría de producto para predecir la demanda (ingresa 1 para 'limpieza' o 2 para 'alimentos'): ")
                if categoria == "1":
                    predecir_demanda('limpieza')
                    break
                elif categoria == "2":
                    predecir_demanda('alimentos')
                    break
        
    elif Opciones_menu == "4":
        print(f'Se utilizó la técnica de CLUSTERING para hacer una {Modelo_2} \nEsto responde al problema de "no conocer al cliente", permitiendo identificar quiénes son los compradores VIP, quiénes compran poco y quiénes gastan mucho, para personalizar las promociones.')
        print("------")
        print("Elije una opcion:\n1. Ejecutar el modelo de Clustering y ver grafica\n2. Volver al menu\n")
        opcion_regresion = input("Seleccione una opción (1-2): ")
        if opcion_regresion == "1":
            ejecutar_clustering()

    elif Opciones_menu == "5":
        print(f'Estos son los diferentes grupos de clientes identificados mediante el modelo de Clustering:' )
        Opciones_Clientes = {"1": Cliente_Estandar, "2": Cliente_Premium, "3": Cliente_VIP}
        while True:
            Opciones_Clientes = input('Coloque el código para mostrar los grupos de clientes aquí: 1. Cliente estándar 2. Cliente Premium. 3. Cliente VIP/Mayorista\n')
            if Opciones_Clientes == "1":
                print(Cliente_Estandar)
            elif Opciones_Clientes == "2":
                print(Cliente_Premium)
            elif Opciones_Clientes == "3":
                print(Cliente_VIP)
            else:
                print("Error. Por favor, seleccione una opción válida.")
                continue
            break
    
    elif Opciones_menu == "6":
        print("""
-Regresión (Predicción): Se dividieron los datos en dos partes: 80% para entrenar al modelo (que aprenda la tendencia) y 
20% para probarlo (verificar si predice bien con datos "nuevos").

-Clustering (Agrupación): Al ser un método para descubrir patrones, se usó el 100% de los datos disponibles 
para que el algoritmo detectara automáticamente las características comunes y formara los 3 grupos de clientes.
""")
    
    elif Opciones_menu == "7":
        print(Salida)
        break
    
    else:
        print("Error. Por favor, seleccione una opción válida.")

    input("\nPresiona Enter para continuar...")
