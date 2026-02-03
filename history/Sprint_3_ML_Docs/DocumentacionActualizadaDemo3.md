# Documentación Técnica del Modelado de Machine Learning
A continuacion se detalla la implementación de los algoritmos de Inteligencia Artificial aplicados al proyecto "Tienda Aurelion". Se han desarrollado dos modelos distintos para abordar los problemas clave del negocio: la predicción de demanda (para inventario) y la segmentación de clientes (para marketing).

## 1. Objetivo (predecir o clasificar)

El objetivo de esta etapa es pasar del análisis descriptivo a la predicción y agrupación automática, utilizando algoritmos de Machine Learning supervisados y no supervisados.

**Modelo A: Predicción de Demanda**

* Tipo de problema: Regresión (Supervisado).

* Objetivo: Predecir la cantidad exacta de productos que se venderán en los próximos meses. Esto responde al problema de gestión de inventario, permitiendo a la tienda anticipar cuánto stock comprar para no quedarse sin mercadería ni acumular exceso.

**Modelo B: Segmentación de Clientes**

* Tipo de problema: Clustering / Agrupamiento (No Supervisado).

* Objetivo: Clasificar a la base de datos de clientes en grupos con comportamientos similares. Esto responde al problema de "no conocer al cliente", permitiendo identificar quiénes son los compradores VIP, quiénes compran poco y quiénes gastan mucho, para personalizar las promociones.

## 2. Algoritmo elegido y justificación

**Modelo A: Regresión Lineal (Linear Regression)**

Se eligió el algoritmo de Regresión Lineal Simple de la librería Scikit-learn.

* Justificación: Al observar los datos históricos de ventas, notamos una tendencia que puede explicarse a través del tiempo. Este algoritmo es ideal para iniciar porque es interpretable, rápido y nos permite trazar una línea de tendencia clara para estimar valores futuros (ventas) basándonos en una variable independiente (tiempo).

**Modelo B: K-Means (K-Medias)**

Se eligió el algoritmo K-Means.

* Justificación: Es uno de los algoritmos más eficientes y populares para agrupar datos cuando no tenemos etiquetas predefinidas (no sabemos de antemano quién es VIP y quién no). K-Means funciona calculando la distancia entre los clientes basándose en sus hábitos de compra y creando grupos compactos y diferenciados.

## 3. Entradas (X) y salida (y)

Para que los modelos funcionen, debemos definir qué datos entran al algoritmo (Features) y qué esperamos que salga (Target).

**Para la Regresión Lineal:**
* Entrada ($X$): El Tiempo (variable tiempo_idx). Transformamos las fechas de los meses en una secuencia numérica (0, 1, 2, 3...) para que el modelo entienda la progresión temporal.
* Salida ($y$): La Cantidad Vendida. Es el número total de unidades de una categoría (ej. Limpieza) que se vendieron en ese mes.

**Para el Clustering (K-Means):**

* Entradas ($X$): Utilizamos dos variables clave del comportamiento del cliente:
    1. total_importe_cliente: Cuánto dinero ha gastado en total el cliente en la tienda.
    2. total_cantidad_cliente: Cuántos productos ha comprado en total.
* Salida ($y$): El Grupo Asignado (Cluster). El algoritmo nos devuelve un número (0, 1 o 2) que representa la "etiqueta" del grupo al que pertenece ese cliente.

## 4. Métricas de evaluación
Para saber si nuestros modelos son confiables, utilizamos métricas matemáticas específicas.

**Métricas de Regresión:**
* $R^2$ (Coeficiente de Determinación): Nos indica qué tan bien se ajusta nuestra línea de predicción a los datos reales. Un valor cercano a 1 indica un ajuste perfecto.
* MSE (Error Cuadrático Medio) y RMSE (Raíz del Error): Miden el margen de error promedio entre lo que el modelo predijo y lo que realmente pasó. Buscamos que este número sea lo más bajo posible.

**Métricas de Clustering:**

* Inercia: Mide qué tan cerca están los puntos (clientes) del centro de su propio grupo. Queremos una inercia baja, lo que significa grupos muy compactos.

* Silhouette Score: Mide qué tan bien separado está un grupo de los otros. Un valor cercano a 1 indica que los grupos están perfectamente definidos y no se mezclan entre sí.

## 5. Modelo ML implementado

Ambos modelos fueron implementados utilizando Python y la biblioteca estándar de la industria Scikit-learn (sklearn).

* **Librerías clave:** pandas para manejo de datos, matplotlib para gráficos y sklearn para los algoritmos matemáticos.

* **Configuración:**

    * En Regresión: Se instanció LinearRegression().

    * En Clustering: Se instanció KMeans(n_clusters=3), configurado para buscar 3 grupos de clientes distintos.


## 6. División train/test y entrenamiento

### Entrenamiento de Regresión

Siguiendo las buenas prácticas de Machine Learning, no usamos todos los datos para entrenar.

* División: Usamos el comando train_test_split.

    * 80% Train (Entrenamiento): Datos que el modelo usó para aprender la tendencia.

    * 20% Test (Prueba): Datos que guardamos "en secreto" para evaluar si el modelo predecía bien.

* Proceso: Se ejecutó el método .fit(X_train, y_train) para que la computadora aprendiera la relación entre el paso del tiempo y las ventas.

**Entrenamiento de Clustering**

Al ser aprendizaje no supervisado, el enfoque es distinto. Usamos el total de los datos de clientes para encontrar patrones globales.

* Proceso: Se prepararon los datos de los clientes (agrupando sus compras totales) y se ejecutó .fit(x_clustering) para que el algoritmo encontrara automáticamente los centros de los 3 grupos.

## 7. Predicciones y métricas calculadas

**Resultados de la Regresión (Categorías Clave)**

El modelo de regresión lineal se evaluó en dos de las categorías más importantes de la tienda para probar su capacidad de generalización: Limpieza y Alimentos.

**A. Categoría Limpieza**
* Coeficiente de Determinación ($R^2$): 0.66
    * Interpretación: El modelo logra explicar el 66% de la variación en las ventas de productos de limpieza basándose solo en el tiempo. Es un resultado sólido para una regresión simple, indicando que existe una tendencia clara.
* Error Promedio (RMSE): 37.27
    * Interpretación: Las predicciones del modelo tienen un margen de error promedio de aproximadamente 37 unidades. Para la gestión de inventario, esto nos permite establecer un stock de seguridad de +/- 37 productos sobre la predicción para evitar quiebres.

**B. Categoría Alimentos**
* Coeficiente de Determinación ($R^2$): 0.62

    * Interpretación: El modelo explica el 62% del comportamiento de ventas. Es ligeramente inferior a Limpieza, lo que sugiere que la demanda de alimentos podría depender más de otros factores (como estacionalidad o promociones) que solo del paso del tiempo.

* Error Promedio (RMSE): 45.34

    * Interpretación: El error promedio asciende a 45 unidades, lo cual es esperable dada la mayor volatilidad en el consumo de alimentos.

### Resultados del Clustering (Segmentación de Clientes)

El modelo K-Means agrupó exitosamente a los clientes en 3 perfiles bien diferenciados. Las métricas de validación confirman que la segmentación es extremadamente precisa.

* Silhouette Score: 0.9323

    * Interpretación: Este valor es excepcionalmente alto (el máximo es 1). Indica una separación casi perfecta entre los grupos. Significa que los clientes dentro de cada grupo son muy parecidos entre sí y muy diferentes a los de los otros grupos. No hay zonas grises.

**Perfiles Identificados (Centroides y Distribución)**

El algoritmo identificó tres tipos de clientes basándose en sus promedios de gasto y consumo:

1. Grupo 0: "Cliente Estándar" (La Base Masiva)

    * Población: 599 clientes (La gran mayoría).

    * Comportamiento Promedio: Gasto de $10,572 y compra de 3 unidades.

    * Conclusión: Representan el consumo minorista típico. El objetivo aquí es aumentar su ticket promedio mediante venta cruzada.

2. Grupo 1: "Cliente Premium" (Alto Volumen)

    * Población: 29 clientes.

    * Comportamiento Promedio: Gasto de $433,631 y compra de 188 unidades.

    * Conclusión: Un grupo pequeño pero de alto valor. Probablemente pequeñas empresas o familias numerosas que requieren estrategias de retención.

3. Grupo 2: "Cliente VIP / Mayorista" (Top Tier)

    * Población: 21 clientes.

    * Comportamiento Promedio: Gasto de $656,400 y compra de 244 unidades.

    * Conclusión: Son los "socios" de la tienda. Aunque son pocos (menos del 5% de la base), generan un flujo de caja crítico. Perder a uno de estos clientes tiene un impacto financiero significativo.

## 8. Resultados en uno o más gráficos

Las visualizaciones generadas por el código Python nos permiten validar intuitivamente si los modelos matemáticos se ajustan a la realidad del negocio. A continuación, se detallan los gráficos obtenidos.

### Gráfico 1: Proyección de Ventas con Etiquetas (Regresión Lineal)

Este gráfico de dispersión superpuesto con una línea de tendencia visualiza el comportamiento de ventas para las categorías Limpieza y Alimentos.

* Puntos Azules (Datos Reales): Cada punto representa la venta real ocurrida en un mes específico. La dispersión vertical de estos puntos nos muestra la volatilidad natural de la demanda.

* Línea Roja (Tendencia Aprendida): Esta recta continua representa la predicción del modelo de Regresión Lineal (modelo.predict(X)).

    * Interpretación: La inclinación de la línea roja nos indica visualmente si la categoría está en crecimiento o decrecimiento.

    * Ajuste: La distancia vertical entre un punto azul y la línea roja representa visualmente el Error (MSE) del modelo. Cuanto más cerca estén los puntos de la línea, más precisa es la predicción.

* Etiquetas Grises (Meses): Se añadieron anotaciones numéricas junto a cada punto (ej. "0", "1", "2"...) que corresponden al tiempo_idx. Esto permite identificar rápidamente qué meses específicos tuvieron picos de venta inusuales (outliers) que se alejan de la tendencia roja.

### Gráfico 2: KMeans Clusters (Gasto vs. Cantidad)

Este gráfico de dispersión revela la estructura oculta de la base de datos de clientes, utilizando dos ejes críticos: Gasto Total (Eje X) y Cantidad Total (Eje Y).

* Codificación por Colores (Azul, Rojo, Naranja):

    * El código asignó automáticamente tres colores (Azul, Rojo, Naranja) para diferenciar los grupos.

    * Se observa una Mancha Densa (generalmente azul o el color del Grupo 0) ubicada en la esquina inferior izquierda. Esto valida visualmente que la gran mayoría de clientes (599 personas) compran poco y gastan poco.

    * Se observan Puntos Dispersos (Rojos/Naranjas) que se extienden hacia la derecha y arriba. Estos son los Grupos 1 y 2, visualmente separados del resto, confirmando que son perfiles de comportamiento totalmente distintos.

* Centroides (Puntos Grandes con Borde Negro):

    * Dentro de cada nube de color, aparece un punto más grande y marcado. Este es el centroide matemático calculado por el algoritmo.

    * Interpretación: Este punto representa al "Cliente Promedio" de ese grupo. Al ver la gran distancia física en el gráfico entre el centroide del Grupo 0 y el del Grupo 2, confirmamos visualmente la métrica de Silhouette (0.93): los grupos no se mezclan, la segmentación es exitosa.
