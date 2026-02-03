# 🛒 Aurelion Retail Analytics: Solución Integral de BI

![Status](https://img.shields.io/badge/Status-Completado-success)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![PowerBI](https://img.shields.io/badge/PowerBI-Desktop-yellow)
![Machine Learning](https://img.shields.io/badge/Sklearn-Regression%20%26%20Clustering-orange)

## Descripción del Proyecto

Este repositorio contiene una solución *integral* de Business Intelligence desarrollada para **Tienda Aurelion**, un e-commerce en crecimiento. El objetivo principal fue transformar datos transaccionales brutos en decisiones estratégicas mediante un pipeline de datos que incluye:

1.  **Ingeniería de Datos:** Validación y estructuración de bases de datos relacionales.
2.  **Análisis Exploratorio (EDA):** Detección estadística de patrones de venta, outliers y correlaciones.
3.  **Machine Learning:** Implementación de algoritmos para segmentación de clientes y predicción de demanda.
4.  **Visualización Interactiva:** Un tablero de control en Power BI para la toma de decisiones gerenciales.

---

## 📂 Estructura del Repositorio

El proyecto está organizado para mostrar tanto el producto final como la evolución histórica del desarrollo.

```text
Tienda-Aurelion-BI/
│
├── 📁 dashboard/          # ENTREGABLE FINAL
│   └── Tienda_Aurelion_Dashboard.pbix  # Tablero interactivo en Power BI
│
├── 📁 src/                # CÓDIGO FUENTE DE PRODUCCIÓN
│   ├── main_analysis.py       # Orquestador del análisis y menú CLI
│   ├── clustering_model.py    # Modelo K-Means para segmentación de clientes
│   └── regression_model.py    # Modelo de Regresión Lineal para demanda
│
├── 📁 data/               # DATASET FINAL (Limpio y Normalizado)
│   ├── cliente_limpio.csv
│   ├── venta_limpio.csv
│   ├── detalle_ventas_limpio.csv
│   └── producto_limpio.csv
│
└── 📁 history/            # TRAZABILIDAD Y DOCUMENTACIÓN (Evolución por Sprints)
    ├── Sprint_1_Inicio/       # Definición del problema y el contexto
    ├── Sprint_2_ETL_Stats/    # Script de análisis estadístico descriptivo, detección de outliers y visualización
    │   └── data_snapshot_v2/  # (Snapshot de datos utilizado en esta fase)
    └── Sprint_3_ML_Docs/      # Documentación técnica de los modelos de ML
```
---

## 🚀 Tecnologías y Librerías

El proyecto utiliza un stack tecnológico centrado en datos:

* **Python:** Lenguaje principal de procesamiento.

    * **pandas & numpy:** Manipulación de datos y álgebra lineal.

    * **scikit-learn:** Modelado predictivo (Regresión) y descriptivo (K-Means).

    * **matplotlib & seaborn:** Visualización de datos estática.

    * **pathlib:** Gestión robusta de rutas de archivos.

* **Power BI:** Visualización dinámica, modelado de datos (Esquema Estrella) y DAX.

---

## 📈 Modelos de Machine Learning Implementados

El código fuente en **src/** ejecuta dos modelos clave para el negocio:

1. **Segmentación de Clientes (Clustering)**

    * **Algoritmo:** K-Means.

    * **Lógica:** Agrupa clientes basándose en dos dimensiones clave: **Monto Total Gastado** y **Volumen de Productos Comprados**.

    * **Resultado:** Identificación de perfiles "VIP", "Promedio" y "Bajo Consumo" para estrategias de marketing diferenciadas.

2. **Predicción de Demanda (Regresión)**

    * **Algoritmo:** Regresión Lineal Simple.

    * **Lógica:** Analiza la tendencia histórica de ventas por categoría (Alimentos vs. Limpieza).

    * **Resultado:** Proyección de unidades vendidas para optimización de stock (evitar quiebres o sobre-stock).

---

## 📜 Historia del Proyecto (Metodología Ágil)

El desarrollo se llevó a cabo en 4 Sprints incrementales. La evidencia de cada etapa se encuentra en la carpeta **history/**.

* **Sprint 1:** Definición del contexto E-commerce y **Análisis de la Arquitectura de Datos** (Evaluación de tablas y clasificación de variables por tipo: cualitativas/cuantitativas).

* **Sprint 2:** Análisis Exploratorio y Estadístico. Validación de la calidad de los datos mediante estadística descriptiva. Se implementaron algoritmos para la detección de outliers (Rango Intercuartílico) y análisis de correlaciones para entender la estructura del negocio antes del modelado.

    * **Nota:** El código en python de esta fase utiliza un dataset preliminar ubicado en history/Sprint_2.../data_snapshot_v2.

* **Sprint 3:** Implementación de modelos de Inteligencia Artificial y ampliación del dataset para robustecer el entrenamiento de los algoritmos.

* **Sprint 4:** Integración final en Power BI y Modelado de Datos Avanzado. Creación de métricas DAX complejas, tooltips personalizados, agrupaciones, jerarquía y navegación por drill-through. Se diseñó una **Tabla Calendario dedicada** (inexistente en la fuente original) para garantizar la continuidad cronológica del modelo, centralizar jerarquías temporales y habilitar cálculos de inteligencia de tiempo de alto rendimiento (YTD, YoY).

---

## 🛠️ Instrucciones de Ejecución

Para ejecutar el pipeline de análisis en Python:

1.  **Clonar el repositorio.**
2.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Navegar a la carpeta `src`:**
    ```bash
    cd src
    ```
4.  **Ejecutar el orquestador:**
    ```bash
    python main_analysis.py
    ```

---

## 👤 Autor

**Uriel Romero**
* Estudiante de Ingeniería en Sistemas de Información.
* Analista de Datos Jr. / Desarrollador BI.
* [www.linkedin.com/in/uriel-romero-](https://www.linkedin.com/in/uriel-romero-)

### 📅 Historial de Desarrollo

**1. Fase Inicial (Trabajo en Equipo):**
El proyecto original fue desarrollado como parte de un desafío académico en colaboración con **Ivan Zirulnik, Nicolas Cook, Marco Huanca y Valeria Belen**. Juntos definimos la lógica de negocio y construimos el Dashboard base en Power BI.

**2. Evolución Post-Cursado (Trabajo Individual):**
Este repositorio representa una **versión extendida y optimizada** desarrollada individualmente por mí tras finalizar el curso con fines de portafolio profesional.
* **Refactorización:** Reescritura del código Python para cumplir estándares profesionales (modularización y manejo de errores).
* **Ingeniería:** Estructuración del repositorio y organización de la documentación técnica histórica.
* **Pipeline:** Optimización del flujo de datos para este portafolio.

