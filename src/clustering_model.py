from pathlib import Path
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import numpy as np

def ejecutar_clustering():
    """
    Ejecuta el modelo de segmentación de clientes K-Means basado en Recencia y Monto.
    Genera visualizaciones y métricas de evaluación.
    """
    # 1. Configuración de Rutas (Pathlib para compatibilidad SO)
    # Se asume estructura: repo/src/clustering_model.py -> repo/data
    base_path = Path(__file__).resolve().parent.parent / 'data' 

    # Carga de datos
    try:
        clientes = pd.read_csv(base_path / 'cliente_limpio.csv')
        detalle = pd.read_csv(base_path / 'detalle_ventas_limpio.csv')
        ventas = pd.read_csv(base_path / 'venta_limpio.csv')
    except FileNotFoundError as e:
        print(f"Error Crítico: No se encontraron los archivos de datos en {base_path}")
        print(f"Detalle: {e}")
        return

    # 2. Ingeniería de Características (Feature Engineering)
    # Unir detalle con ventas para obtener id_cliente
    df = detalle.merge(ventas[['id_venta', 'id_cliente']], on='id_venta', how='left')

    # Limpieza de nulos y conversión de tipos
    df['cantidad'] = pd.to_numeric(df.get('cantidad', 0), errors='coerce').fillna(0)
    df['importe'] = pd.to_numeric(df.get('importe', 0), errors='coerce').fillna(0.0)

    # Agregación por Cliente (RFM simplificado: Monetary + Frequency/Quantity)
    clientes_feats = df.groupby('id_cliente').agg(
        total_importe_cliente=('importe', 'sum'),
        total_cantidad_cliente=('cantidad', 'sum')
    ).reset_index()

    # Consolidación del Dataset Final
    df_clientes = clientes.merge(clientes_feats, on='id_cliente', how='left')
    df_clientes[['total_importe_cliente', 'total_cantidad_cliente']] = df_clientes[['total_importe_cliente', 'total_cantidad_cliente']].fillna(0)

    # 3. Modelado (K-Means)
    x_clustering = df_clientes[['total_importe_cliente', 'total_cantidad_cliente']]
    
    # Configuración del modelo
    modelo_cl = KMeans(n_clusters=3, random_state=42)
    modelo_cl.fit(x_clustering)
    
    # Asignación de etiquetas
    df_clientes['grupo'] = modelo_cl.labels_

    # 4. Resultados y Visualización
    print(f"\n--- Resultados del Clustering (K={modelo_cl.n_clusters}) ---")
    print("Distribución de Clientes por Grupo:")
    print(df_clientes['grupo'].value_counts().sort_index())

    print("\nCentroides (Perfil Promedio de cada Grupo):")
    for i, c in enumerate(modelo_cl.cluster_centers_):
        print(f"Grupo {i}: Gasto Promedio: ${c[0]:.2f} | Cantidad Promedio: {c[1]:.2f} unidades")

    # Visualización
    X = x_clustering.values
    labels = modelo_cl.labels_
    centers = modelo_cl.cluster_centers_

    plt.figure(figsize=(8, 5))
    colors_map = ['#1f77b4', '#d62728', '#ff7f0e'] # Azul, Rojo, Naranja
    
    for k in range(len(centers)):
        members = (labels == k)
        center = centers[k]
        color = colors_map[k % len(colors_map)]
        
        plt.scatter(X[members, 0], X[members, 1], s=30, c=color, alpha=0.5, label=f'Grupo {k}')
        plt.scatter(center[0], center[1], s=200, c=color, edgecolors='k', marker='X', label=f'Centroide {k}')

    plt.title('Segmentación de Clientes: Valor vs Volumen')
    plt.xlabel('Gasto Total ($)')
    plt.ylabel('Cantidad Total de Productos')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.show()

    # 5. Evaluación Técnica
    print("\n--- Métricas de Desempeño ---")
    print(f"Inercia (Cohesión intra-cluster): {modelo_cl.inertia_:,.0f}")
    
    try:
        sil_score = silhouette_score(x_clustering, labels)
        print(f"Silhouette Score (Separabilidad): {sil_score:.4f}")
    except Exception as e:
        print(f"No se pudo calcular Silhouette: {e}")

    #  Guardar Resultados 
    output_file = base_path / 'clientes_con_clusters.csv'
    df_clientes.to_csv(output_file, index=False)
    print(f"\n[Éxito] Base de datos enriquecida guardada en: {output_file.name}")