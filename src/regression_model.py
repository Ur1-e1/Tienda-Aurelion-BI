from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import timedelta
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

def predecir_demanda(categoria):
    """
    Entrena un modelo de Regresión Lineal para predecir la demanda futura
    de una categoría específica basándose en datos históricos.
    """
    categoria_elegida = categoria.lower()
    
    # 1. Carga de Datos
    base_path = Path(__file__).resolve().parent.parent / 'data'
    
    try:
        ventas = pd.read_csv(base_path / 'venta_limpio.csv')
        detalle = pd.read_csv(base_path / 'detalle_ventas_limpio.csv')
        productos = pd.read_csv(base_path / 'producto_limpio.csv') 
    except FileNotFoundError:
        print("Error: Archivos de datos no encontrados en la ruta esperada.")
        return

    # 2. Preprocesamiento
    df_completo = detalle.merge(ventas, on='id_venta').merge(productos, on='id_producto')
    df_completo['fecha'] = pd.to_datetime(df_completo['fecha'])

    # Filtrado por Categoría
    df_filtrado = df_completo[df_completo['categoria'] == categoria_elegida].copy()
    
    if df_filtrado.empty:
        print(f"Advertencia: No hay datos para la categoría '{categoria_elegida}'")
        return

    # Agrupación temporal (Mensual)
    df_filtrado['periodo'] = df_filtrado['fecha'].dt.to_period('M')
    datos_agrupados = df_filtrado.groupby('periodo')['cantidad'].sum().reset_index()
    
    # Creación de variable independiente (Índice de Tiempo)
    datos_agrupados['tiempo_idx'] = range(len(datos_agrupados))

    X = datos_agrupados[['tiempo_idx']]
    y = datos_agrupados['cantidad']

    # 3. Entrenamiento del Modelo
    # Split 80/20 para validación
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
    
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)

    # 4. Evaluación de Métricas
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred) # Mide el error promedio en unidades
    rmse = np.sqrt(mse) # Raíz del error cuadrático 

    print(f"--- RESULTADOS PARA: {categoria_elegida.upper()} ---")
    print(f"Coeficiente de determinación (R²): {r2:.2f}")
    print(f"Error Cuadrático Medio (MSE): {mse:.2f}")
    print(f"Error Absoluto Medio (MAE): {mae:.2f}")
    print(f"Raíz del Error Cuadrático Medio (RMSE): {rmse:.2f}")

    # 5. Visualización
    plt.figure(figsize=(10, 6))
    
    # Datos Históricos
    plt.scatter(X, y, color='#1f77b4', label='Ventas Reales')
    
    # Línea de Tendencia
    plt.plot(X, modelo.predict(X), color='#d62728', linewidth=2, label='Tendencia (Predicción)')

    # Etiquetas de datos
    for i, txt in enumerate(X['tiempo_idx']):
         plt.annotate(txt, (X['tiempo_idx'].iloc[i], y.iloc[i]), 
                      xytext=(0, 5), textcoords='offset points', 
                      ha='center', fontsize=8, color='gray')

    plt.title(f'Proyección de Demanda: {categoria_elegida.capitalize()}')
    plt.xlabel('Índice Temporal (Meses)')
    plt.ylabel('Cantidad Vendida')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

    # 6. Utilidad Interactiva (Conversor de Fechas)
    _ejecutar_calculadora_fechas(datos_agrupados)

def _ejecutar_calculadora_fechas(df_agrupado):
    """Función auxiliar para interpretar el eje X del gráfico."""
    print("\n--- Calculadora de Fechas (Eje X) ---")
    print("Ingrese un valor del Eje X para conocer la fecha estimada.")
    
    fecha_base = df_agrupado['periodo'].min().start_time
    
    while True:
        entrada = input("Valor del Eje X (o 's' para salir): ")
        if entrada.lower() == 's': break
        
        try:
            valor_x = float(entrada)
            dias_estimados = int(valor_x * 30.44)
            fecha_calc = fecha_base + timedelta(days=dias_estimados)
            print(f"> Fecha estimada: {fecha_calc.strftime('%B %Y')}")
        except ValueError:
            print("Por favor ingrese un número válido.")