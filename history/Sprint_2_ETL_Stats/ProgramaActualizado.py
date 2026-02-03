import pandas as pd
import numpy as np
import time
import sys
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración del entorno de ejecución
# Se utiliza Pathlib para garantizar la compatibilidad entre sistemas operativos (Windows/Mac/Linux)
# y asegurar que la ruta sea relativa a la ubicación de este script.
base_path = Path(__file__).resolve().parent
data_folder = 'data_snapshot_v2'

def load_data():
    """
    Orquesta la carga de los datasets históricos desde el snapshot del Sprint 2.
    Maneja excepciones críticas de archivo no encontrado para evitar cierres abruptos.
    
    Returns:
        tuple: (df_detalle, df_ventas, df_productos) o (None, None, None) si falla.
    """
    try:
        # Carga de datos crudos
        df_detalle = pd.read_csv(base_path / data_folder / 'detalle_ventas_limpio.csv')
        df_ventas = pd.read_csv(base_path / data_folder / 'venta_limpio.csv')
        df_productos = pd.read_csv(base_path / data_folder / 'producto_limpio.csv')
        print("Datos cargados exitosamente desde archivos limpios.")
        return df_detalle, df_ventas, df_productos
    except FileNotFoundError as e:
        print("\n" + "=" * 70)
        print(f"ERROR CRITICO: Archivo no encontrado. El script NO puede continuar sin los datos.")
        print(f"Ruta faltante: {e.filename}")
        print("Por favor, asegurese de que los archivos CSV limpios esten presentes.")
        print("=" * 70)
        return None, None, None

# Inicialización global de datos
df_detalle, df_ventas, df_productos = load_data()
time.sleep(2)

def display_descriptive_stats(df_detalle, df_ventas):
    """
    Calcula y presenta métricas de tendencia central y dispersión.
    Analiza Importe, Cantidad y Ticket Promedio para fundamentar decisiones de negocio.
    """
    if df_detalle is None or df_ventas is None:
        print("ERROR: Datos no disponibles para realizar este analisis.")
        return

    # Conversión de tipos para asegurar precisión aritmética
    importe_serie = df_detalle['importe'].astype(float)
    cantidad_serie = df_detalle['cantidad'].astype(int)

    # Cálculo de KPIs de Negocio
    media_importe = importe_serie.mean()
    mediana_importe = importe_serie.median()
    std_importe = importe_serie.std()
    min_importe = importe_serie.min()
    max_importe = importe_serie.max()

    moda_cantidad = cantidad_serie.mode().iloc[0] if not cantidad_serie.mode().empty else 'Vacio'
    min_cantidad = cantidad_serie.min()
    max_cantidad = cantidad_serie.max()
    media_cantidad = cantidad_serie.mean()
    mediana_cantidad = cantidad_serie.median()
    desv_cantidad = cantidad_serie.std()

    # Cálculo del Average Order Value (AOV)
    importe_total_ventas = importe_serie.sum()
    num_transacciones_unicas = df_ventas['id_venta'].nunique()
    ticket_promedio = importe_total_ventas / num_transacciones_unicas

    print("\n" + "=" * 60)
    print("        RESULTADOS DE ESTADISTICAS DESCRIPTIVAS")
    print("=" * 60)
    
    print("\n--- 1. Metricas de Valor (Importe de Ventas) ---")
    print(f" Media (µ): ..................... ${media_importe:10.2f}")
    print(f" Mediana (Q2): ................... ${mediana_importe:10.2f}")
    print(f" Desviación Estandar (σ): ........ ${std_importe:10.2f}")
    print(f" Minimo Importe: ................. ${min_importe:10.2f}")
    print(f" Maximo Importe: ................. ${max_importe:10.2f}")
    
    print("\n--- 2. Metricas de Cantidad y Frecuencia ---")
    print(f" Moda (Cantidad): ................ {moda_cantidad:10d}")
    print(f" Minimo Cantidad: ................ {min_cantidad:10d}")
    print(f" Maximo Cantidad: ................ {max_cantidad:10d}")
    print(f" Media (μ): .................... {media_cantidad:10.3f} unidades")
    print(f" Mediana (50%): ................ {mediana_cantidad:10.1f} unidades")
    print(f" Desviación Estándar (σ): ...... {desv_cantidad:10.3f} unidades")
    
    print("\n--- 3. Metricas Agregadas Clave ---")
    print(f" Ticket Promedio de Venta: ....... ${ticket_promedio:10.2f}")

    print("\nHALLAZGO CLAVE:")
    print(f" **La métrica principal a optimizar es el Ticket Promedio: ${ticket_promedio:10.2f}**")
    print(" Ticket Promedio de Venta: (Es el indicador de éxito que une las estrategias de Clientes y Productos).")
    print(f" **La Media (${media_importe:.2f}) > Mediana (${mediana_importe:.2f}) indica una distribución Sesgada a la Derecha (productos de alto valor).**")
    print(f" **La Cantidad vendida tiene Baja Variabilidad (σ={desv_cantidad:.3f}) y Rango limitado ({min_cantidad}-{max_cantidad}).**")
    print(f" **La Media (≈{media_cantidad:.2f}) ≈ Mediana (≈{mediana_cantidad:.1f}) indica una distribución Aproximadamente Simétrica.**")
    print(" *Implicación: Las compras se concentran en bajo volumen (1 a 3 unidades). Esto simplifica la predicción de inventario.*")

    print("-" * 60)
    # Pausa interactiva solicitada
    input("\nPresione Enter para volver al menú principal...")

def display_outliers(df_detalle):
    """
    Implementa el método del Rango Intercuartílico (IQR) para la detección de anomalías.
    Identifica transacciones atípicas que pueden sesgar el análisis general.
    """
    if df_detalle is None:
        print("ERROR: Datos de detalle de ventas no disponibles para este analisis.")
        return

    columna = 'importe'
    df = df_detalle.copy()

    # Cálculo estadístico de cuartiles
    Q1 = df[columna].quantile(0.25)
    Q2 = df[columna].quantile(0.50)
    Q3 = df[columna].quantile(0.75)
    IQR = Q3 - Q1
    
    # Definición de umbrales (Fences)
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    
    # Segmentación de datos anómalos
    outliers_superiores = df[df[columna] > limite_superior]
    outliers_inferiores = df[df[columna] < limite_inferior]
    max_valor = df[columna].max()
    
    print("\n" + "=" * 60)
    print("        DETECCION DE OUTLIERS (RANGO INTERCUARTILICO)")
    print("=" * 60)
    print(f"Total de registros analizados: {len(df)}")

    print("\n--- 1. Cuartiles y Rango Intercuartilico (IQR) ---")
    print(f" Q1 (Cuartil 1): ................. ${Q1:10.2f}")
    print(f" Q2 (Mediana): ................... ${Q2:10.2f}")
    print(f" Q3 (Cuartil 3): ................. ${Q3:10.2f}")
    print(f" Rango Intercuartilico (IQR): .... ${IQR:10.2f}")

    print("\n--- 2. Definicion de Limites (Fences) ---")
    print(f" Limite Inferior (Q1 - 1.5*IQR): . ${limite_inferior:10.2f}")
    print(f" Limite Superior (Q3 + 1.5*IQR): . ${limite_superior:10.2f}")
    
    print("\n--- 3. Hallazgos y Conclusion de Outliers ---")
    print(f" Outliers Inferiores (ventas muy bajas): {len(outliers_inferiores):10d}")
    print(f" Outliers Superiores (ventas muy altas): {len(outliers_superiores):10d}")
    print(f" Valor Maximo en los datos: .............. ${max_valor:10.2f}")
    
    if max_valor > limite_superior:
        print("\n ¡CONFIRMACION: El valor máximo es un Outlier, superando el limite!")
        print(f" Para la documentación, el Limite Superior es: ${limite_superior:.2f}")

        print("\nHALLAZGO CLAVE:")
        print(f" **Se detectaron {len(outliers_superiores)} Outliers Superiores: la tienda opera con un Modelo Dual de Ingresos (Segmento Premium).**")
    else:
        print("\n El valor máximo no supera el LLimite Superior.")

    print("-" * 60)
    input("\nPresione Enter para volver al menú principal...")

def display_correlations(df_detalle, df_productos):
    """
    Evalúa la fuerza y dirección de las relaciones lineales entre variables (Pearson).
    Determina si el precio o el importe influyen en el comportamiento de compra.
    """
    if df_detalle is None or df_productos is None:
        print("ERROR: Datos de detalle o productos no disponibles para este analisis.")
        return

    # Enriquecimiento del dataset
    df_analisis = df_detalle[['cantidad', 'importe', 'id_producto']].merge(
        df_productos[['id_producto', 'precio_unitario']],
        on='id_producto',
        how='left'
    )
    df_analisis.dropna(inplace=True)

    # Cálculo de coeficientes
    corr_precio_cantidad = df_analisis['precio_unitario'].corr(df_analisis['cantidad'])
    corr_importe_cantidad = df_analisis['importe'].corr(df_analisis['cantidad'])

    print("\n" + "=" * 70)
    print("        RESULTADOS DEL ANALISIS DE CORRELACIONES (PEARSON)")
    print("=" * 70)
    
    # Análisis 1: Precio vs Cantidad
    print("\n--- 1. Correlacion entre Precio Unitario y Cantidad Vendida ---")
    print(f" Coeficiente (r): {corr_precio_cantidad:10.4f}")

    r2_precio_cantidad = corr_precio_cantidad ** 2
    print(f" Coeficiente de determinacion (r²): {r2_precio_cantidad:10.4f}")

    if abs(corr_precio_cantidad) < 0.2:
        interpretacion_1 = (
            "Correlacion muy debil o nula: el precio unitario apenas influye en la cantidad vendida."
        )
    elif 0.2 <= abs(corr_precio_cantidad) < 0.5:
        interpretacion_1 = (
            "Correlacion debil: existe una leve relacion entre el precio y la cantidad vendida, "
            "aunque otros factores explican la mayor parte del comportamiento."
        )
    elif 0.5 <= abs(corr_precio_cantidad) < 0.8:
        interpretacion_1 = (
            "Correlacion moderada: los cambios en el precio comienzan a reflejarse en la cantidad vendida."
        )
    else:
        interpretacion_1 = (
            "Correlacion fuerte: el precio unitario tiene una influencia importante en la cantidad vendida."
        )

    print(f" Interpretacion: {interpretacion_1}")
    print(f" El {r2_precio_cantidad*100:.2f}% de la variabilidad total en la cantidad vendida puede explicarse mediante una relación lineal con el precio unitario.")

    # Análisis 2: Importe vs Cantidad
    print("\n--- 2. Correlacion entre Importe de Venta y Cantidad Vendida ---")
    print(f" Coeficiente (r): {corr_importe_cantidad:10.4f}")

    r2_importe_cantidad = corr_importe_cantidad ** 2
    print(f" Coeficiente de determinacion (r²): {r2_importe_cantidad:10.4f}")

    if abs(corr_importe_cantidad) < 0.2:
        interpretacion_2 = (
            "Correlacion muy debil o nula: el importe de venta no guarda una relacion lineal clara con la cantidad vendida."
        )
    elif 0.2 <= abs(corr_importe_cantidad) < 0.5:
        interpretacion_2 = (
            "Correlacion debil: la relacion entre importe y cantidad es leve, posiblemente afectada por diferencias de precios."
        )
    elif 0.5 <= abs(corr_importe_cantidad) < 0.8:
        interpretacion_2 = (
            "Correlacion moderada: como era esperable, al aumentar la cantidad vendida suele aumentar el importe total."
        )
    else:
        interpretacion_2 = (
            "Correlacion fuerte: el importe esta altamente determinado por la cantidad vendida, lo que valida la coherencia de los datos."
        )

    print(f" Interpretacion: {interpretacion_2}")
    print(f" El {r2_importe_cantidad*100:.2f}% de la variabilidad total del importe puede explicarse mediante una relacion lineal con la cantidad vendida.")

    print("--------------")
    print("\nHALLAZGO CLAVE:")
    print(f" **Correlación Nula (-0.0745) entre Precio y Cantidad: el precio NO influye en el volumen de compra.**")
    print(f" **La Correlación Positiva (0.5997) entre Importe y Cantidad confirma que la CANTIDAD es el principal motor del ingreso.**")
    print("-" * 70)
    input("\nPresione Enter para volver al menú principal...")

def display_visualizations(df_detalle, df_ventas):
    """
    Genera dashboards estáticos para la exploración visual de datos.
    Incluye análisis de regresión visual y distribución por medio de pago.
    """
    if df_detalle is None or df_ventas is None:
        print("ERROR: Datos no disponibles para generar los graficos.")
        return

    print("\n" + "=" * 70)
    print("        GENERACION DE GRAFICOS REPRESENTATIVOS")
    print("=" * 70)
    time.sleep(2)

    # 1. Gráfico de Dispersión (Regresión)
    print("\n--- 1. Gráfico de Dispersión (Scatter Plot) de Importe vs. Cantidad (con Línea de Regresión) ---")
    plt.figure(figsize=(7, 4))
    sns.regplot(x='cantidad', y='importe', data=df_detalle, scatter_kws={'s': 10}, line_kws={"color": "red"}) 
    plt.title('Relacion Importe vs. Cantidad (Correlacion Lineal)', fontsize=10)
    plt.xlabel('Cantidad de Productos')
    plt.ylabel('Importe ($)')
    plt.show() 
    time.sleep(2)

    # 2. Gráfico de Barras (Medio de Pago)
    print("\n--- 2. Gráfico de Barras (Bar Plot) por Medio de Pago ---")
    
    df_merged = pd.merge(df_detalle, df_ventas[['id_venta', 'medio_pago']], on='id_venta', how='left')
    df_grouped = df_merged.groupby('medio_pago')['importe'].sum().reset_index().sort_values(by='importe', ascending=False)
    
    plt.figure(figsize=(7, 4))
    sns.barplot(x='medio_pago', y='importe', data=df_grouped, palette="viridis")
    plt.title('Ventas Totales por Medio de Pago', fontsize=10)
    plt.xlabel('Medio de Pago')
    plt.ylabel('Importe Total Acumulado ($)')
    plt.xticks(rotation=0)
    plt.show() 
    time.sleep(2)
    
    print("-" * 70)
    print(" Visualizaciones generadas exitosamente con referencias añadidas. Vuelva al menu principal.")
    print("-" * 70)
    input("\nPresione Enter para volver al menú principal...")

def display_visualizations2(df_detalle, df_ventas, df_productos):
    """
    Genera visualizaciones de ranking de productos y evolución temporal.
    Permite identificar los "Best Sellers" y la estacionalidad de las ventas.
    """
    if df_detalle is None or df_ventas is None:
        print("ERROR: Datos no disponibles para generar los graficos.")
        return

    print("\n" + "=" * 70)
    print("        GENERACION DE GRAFICOS REPRESENTATIVOS")
    print("=" * 70)
    time.sleep(1)

    sns.set_theme(style="whitegrid")

    # 1) Top 10 Productos
    print("\n--- 1) Top 10 Productos Más Vendidos ---")

    df_top = (
        df_detalle.groupby("id_producto")["cantidad"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    df_top = df_top.merge(
        df_productos[["id_producto", "nombre_producto"]],
        on="id_producto",
        how="left"
    )

    plt.figure(figsize=(6, 4))
    plt.barh(df_top["nombre_producto"], df_top["cantidad"])
    plt.xlabel("Unidades Vendidas")
    plt.title("Top 10 Productos Más Vendidos")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()
    time.sleep(1)

    # 2) Evolución Temporal
    print("\n--- 2) Evolución Temporal de Ventas (Mensual) ---")

    df_ventas2 = df_ventas.copy()
    df_ventas2["fecha"] = pd.to_datetime(df_ventas2["fecha"])

    ventas_tiempo = (
        df_ventas2.set_index("fecha")
        .resample("ME")["id_venta"]
        .count()
    )

    plt.figure(figsize=(7, 4))
    plt.plot(ventas_tiempo.index, ventas_tiempo.values, marker='o')
    plt.xlabel("Fecha")
    plt.ylabel("Número de Ventas")
    plt.title("Evolución Temporal de Ventas (Mensual)")
    plt.xticks(rotation=45)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()
    time.sleep(1)

    print("-" * 70)
    print(" Visualizaciones generadas exitosamente. Vuelva al menu principal.")
    print("-" * 70)
    input("\nPresione Enter para volver al menú principal...")

def main_menu():
    """
    Ciclo de vida principal de la aplicación CLI.
    Gestiona la interacción con el usuario y el enrutamiento a las funciones de análisis.
    """
    while True and df_detalle is not None and df_ventas is not None and df_productos is not None:
        print("\n" + "*" * 50)
        print(" MENU DE ANALISIS ESTADISTICO - TIENDA AURELION")
        print("*" * 50)
        print("1. Mostrar Estadisticas Descriptivas y dispersion (Importe, Cantidad, Ticket Promedio)")
        print("2. Mostrar Detección de Outliers (Cuartiles, Limites, Conteo)")
        print("3. Mostrar Analisis de Correlaciones (Precio/Importe vs. Cantidad)")
        print("4. Mostrar Graficas 1")
        print("5. Mostrar Graficas 2")
        print("6. Salir del Programa")
        print("*" * 50)

        opcion = input("Ingrese el número de la opcion deseada (1-6): ")

        if opcion == '1':
            display_descriptive_stats(df_detalle, df_ventas)
        elif opcion == '2':
            display_outliers(df_detalle)
        elif opcion == '3':
            display_correlations(df_detalle, df_productos)
        elif opcion == '4':
            display_visualizations(df_detalle, df_ventas)
        elif opcion == '5':
            display_visualizations2(df_detalle, df_ventas , df_productos)
        elif opcion == '6':
            print("\nGracias por consultar el analisis. ¡Hasta pronto!")
            break
        else:
            print("\nOpcion no valida. Por favor, ingrese un numero entre 1 y 6.")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()