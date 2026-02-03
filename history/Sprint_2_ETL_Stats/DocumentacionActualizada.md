## Estadísticas descriptivas básicas calculadas

El objetivo de esta fase, es utilizar las medidas de tendencia central y dispersión para obtener un resumen cuantitativo de las variables clave del negocio. Estas métricas servirán como base para la interpretación de resultados y la toma de decisiones.

A continuación, se detallan las estadísticas calculadas sobre las variables monetarias y de cantidad, justificando su relevancia para el contexto de E-commerce de la Tienda Aurelion:

### 1. Métricas de Valor (Importe de Ventas)

Calculadas sobre la columna importe de la tabla detalle_ventas_limpio.

* **Media ($\mu$): 7730.08**

    * Cálculo: Se obtiene el promedio de todos los importes de productos vendidos.

    * Por qué se calcula: La media nos da el importe promedio que genera cada ítem vendido. Dado que la Media ($\$7730.08$) es significativamente mayor que la Mediana ($\$6702.00$), concluimos que la distribución de los precios está sesgada a la derecha. Esto significa que, aunque la mayoría de los productos se venden por debajo de $\$7730$, existen productos de muy alto valor (los outliers) que elevan considerablemente el promedio general, lo cual merece ser investigado en la próxima fase de análisis.

* **Mediana (percentil 50): 6702.00**

    * Cálculo: Es el valor central que divide la distribución del importe en dos mitades.

    * Por qué se calcula: La mediana es una medida robusta que no es afectada por los outliers. Su valor de $6702.00 es el importe real que divide las ventas por producto de la Tienda Aurelion: el 50% de los productos se vende por debajo de esta cifra y el 50% por encima. Este valor es más representativo de la venta "típica" que la Media.

* **Desviación Estándar ($\sigma$): 5265.54**

    * Cálculo: Mide la dispersión de los datos con respecto a la Media.

    * Por qué se calcula: Nos indica la volatilidad o dispersión de los importes de venta. Una desviación estándar de $5265.54 (un valor alto, siendo dos tercios de la Media) confirma que los precios en la tienda varían enormemente. Esto es clave, ya que confirma que la Tienda Aurelion no solo vende productos de precio bajo, sino que la oferta incluye artículos de lujo o mucho más caros, generando una gran heterogeneidad en los ingresos por producto.

### 2. Métricas de Cantidad y Frecuencia

Calculadas sobre la columna cantidad de la tabla detalle_ventas_limpio.

* **Moda: 2**

    * Cálculo: Es el valor que aparece con mayor frecuencia en la columna cantidad.

    * Por qué se calcula: Es esencial para entender el patrón de compra más común. Nos revela que los clientes suelen comprar 2 unidades de un mismo producto en una transacción, lo cual es información directamente aplicable a la GESTIÓN DE INVENTARIO, el stock de seguridad y la creación de ofertas tipo "2x1" o "Lleva 2 y ahorra" para aprovechar este comportamiento.

* **Mínimo y Máximo (Rango):**

* Mínimo Cantidad: 1

* Máximo Cantidad: 5

* Mínimo Importe:  272.00

* Máximo Importe: 24865.00

    * Cálculo: El valor más bajo y el valor más alto en las columnas importe y cantidad.

    * Por qué se calcula: Establecer el rango total es fundamental para la detección inicial de outliers. El valor máximo de Importe ($24865.00) se identifica como un potencial outlier que debe ser analizado, mientras que el rango de cantidad (1 a 5) es muy limitado, lo que indica transacciones pequeñas, confirmando que la logística no necesita gestionar pedidos de volumen mayorista.

### 3. Métrica Agregada Clave (Ticket Promedio de Venta)

Aunque no es una estadística simple, se calcula a partir de las básicas y es vital para el E-commerce.

* **Ticket Promedio de Venta: 22095.14**

Cálculo: Suma total de todos los importes de venta dividida por el número total de transacciones (contando por id_venta).

Por qué se calcula:  Esta métrica es el indicador de rendimiento más importante para medir el valor medio que aporta cada cliente por transacción. Es la base para la ESTRATEGIA COMERCIAL Y DE CLIENTES de la Tienda Aurelion. El objetivo de marketing y ventas será siempre encontrar estrategias (como sugerencia de productos) para incrementar este valor clave de $22095.14.

## Identificación del tipo de distribución de variables

El análisis de la forma de la distribución es crucial porque nos permite entender cómo se agrupan los datos (concentración) y cómo se dispersan (sesgo).

### 1. Distribución del Importe de Ventas por Producto (Variable Continua)

Basado en la comparación de las medidas de tendencia central de la Sección anterior:

* Observación: La Media ($\$7730.08$) es notablemente mayor que la Mediana ($\$6702.00$).

**Conclusión:**

La variable Importe de Ventas por Producto presenta una Distribución Asimétrica Positiva (Sesgada a la Derecha)

**Implicación para el Negocio:**

* Distribución de Precio Desigual: El sesgo a la derecha confirma que la mayoría de los productos se venden a precios relativamente bajos o moderados.

* Impacto de Outliers: La larga "cola" hacia la derecha indica la existencia de un pequeño grupo de productos de precio muy elevado que, aunque son menos frecuentes, tienen un impacto desproporcionado en la Media total de ingresos. Esto valida la necesidad de un análisis de outliers más profundo en la siguiente etapa.

### 2. Distribución de la Cantidad de Productos Vendidos (Variable Discreta)

Basado en la Moda, el Rango y las Métricas de Tendencia Central y Dispersión:

* **Métricas Clave:**

    * Media ($\mu$): $2.962$ unidades.

    * Mediana: $3.0$ unidades.

    * Desviación Estándar ($\sigma$): $1.366$ unidades.

    * Rango: $[1, 5]$ unidades.

* **Observación:** El rango de compra es extremadamente limitado (solo de 1 a 5 unidades). Al comparar la Media y la Mediana, observamos que son valores prácticamente idénticos ($\mu \approx \text{Mediana}$).

**Conclusión:**

La variable Cantidad de Productos Vendidos presenta una Distribución Aproximadamente Simétrica y de Baja Variabilidad.

* Simetría: La igualdad casi perfecta entre la Media ($2.962$) y la Mediana ($3.0$) indica que la distribución es equilibrada y no presenta un sesgo significativo hacia los valores bajos o altos.

* Baja Variabilidad: La desviación estándar ($\sigma = 1.366$) es baja y subraya que la dispersión de los datos es mínima dentro del rango fijo de $[1, 5]$. Esto significa que no hay compras de alto volumen.

**Implicación para el Negocio:**

* Concentración de Compras: Los clientes se concentran fuertemente en compras de bajo volumen (1 a 3 unidades). No se registran compras de alto volumen. Esto indica que la mayoría de las transacciones son para consumo personal inmediato, lo cual es típico de un e-commerce minorista.

* Inventario Predictivo: La baja variabilidad y el rango fijo simplifican la predicción de la demanda por ítem. Los modelos de stock de seguridad deben enfocarse en asegurar la disponibilidad constante de unidades bajas (1 y 2), simplificando la planificación de packs o promociones de volumen.

## Análisis de correlaciones entre variables principales

El objetivo del análisis de correlación es medir la fuerza y dirección de la relación lineal entre dos variables, lo cual es fundamental para el modelado predictivo y la comprensión del comportamiento del cliente. Utilizamos el Coeficiente de Correlación de Pearson ($r$) para este análisis.

### 1. Correlación entre Precio Unitario y Cantidad Vendida

El coeficiente de correlación de Pearson ($r$) entre el Precio Unitario y la Cantidad Vendida es -0.0745, lo que se clasifica como una Correlación Nula / Muy Débil.

**Implicación para el Negocio (Estrategia de Precio y Volumen):**

El valor de **-0.0745** está extremadamente cerca de cero. Esto confirma que existe una relación lineal nula o muy débil entre el precio unitario de un producto y la cantidad que un cliente compra en una sola transacción.

* Significado: Que un producto sea más caro o más barato no cambia significativamente la cantidad que el cliente decide comprar (si compra 1, 2 o 5 unidades). La compra de volumen se decide por otras razones, no por el precio individual. La ley de la demanda se cumple de forma casi insignificante.

* Conclusión Clave: La decisión de volumen de compra está dominada por factores no relacionados con el precio unitario, como la categoría del producto (ej. si es un producto de despensa vs. un artículo de consumo ocasional), la necesidad inmediata o el stock que el cliente desea tener. La estrategia de volumen debe enfocarse en promociones por packs específicos o por categoría, en lugar de depender de la elasticidad de precios.

### 2. Correlación entre Importe de Venta y Cantidad Vendida

El coeficiente de correlación de Pearson ($r$) entre el Importe de Venta y la Cantidad Vendida es 0.5997, lo que indica una Correlación Positiva Moderada/Fuerte.

**Implicación para el Negocio (Consistencia de Datos y Modelo):**

El coeficiente de **0.5997** confirma una relación positiva moderada a fuerte entre el importe total de una línea de detalle y la cantidad de unidades vendidas.

* Significado: A medida que la cantidad de un producto aumenta, el importe total de esa línea de venta también lo hace. Un valor de casi 0.60 es esperado, ya que el importe es el resultado directo de multiplicar el precio por la cantidad.

* Conclusión Clave:

    * Validación de Datos: Este valor demuestra que la variable importe es coherente y un buen reflejo de la variable cantidad. Si el valor hubiera sido cercano a 0 (nulo), indicaría un problema grave en la calidad o el cálculo de los datos.

    * Implicación Operacional: El importe sigue siendo una métrica fiable para medir el impacto de las grandes ventas, aunque no tan perfectamente correlacionada como se esperaría, lo cual es un indicio saludable de que hay variedad en los precios unitarios (si todos los precios fueran iguales, la correlación sería casi 1.0). El valor de 0.5997 confirma que las cantidades más altas contribuyen significativamente a los importes más altos.

## Detección de Outliers (Valores Extremos) en el Importe de Venta

La detección de outliers (valores atípicos) se realizó sobre la columna importe utilizando el método del Rango Intercuartílico (IQR), que es robusto y se ajusta a la naturaleza asimétrica de los datos de ingresos de la Tienda Aurelion.

### 1. Cuartiles y Rango Intercuartílico (IQR)

El análisis de posición reveló los siguientes valores clave sobre los 343 registros de venta:

* Cuartil 1 ($Q_1$): $3489.00

    * El 25% de todas las líneas de venta tienen un importe igual o inferior a esta cifra.

* Cuartil 3 ($Q_3$): $10231.50

    * El 75% de todas las líneas de venta tienen un importe igual o inferior a esta cifra.

* Rango Intercuartílico (IQR): $6742.50

    * Esta es la dispersión que existe en el 50% central de los datos.

### 2. Definición de Límites (Fences) y Valores Extremos

Los límites (o fences) definen el umbral a partir del cual un valor se clasifica como atípico, utilizando la fórmula $Q_3 + 1.5 \times \text{IQR}$ para el límite superior.

* Límite Superior (Referencia 3): $20345.25

    * Este valor es el umbral que separa una venta "normalmente alta" de un outlier estadístico.

* Límite Inferior (Referencia 1): -$6624.75

    * Dado que este límite es negativo, se confirma que no existen outliers en el rango de ventas extremadamente bajas (el valor mínimo registrado es $272.00).

### 3. Hallazgos y Conclusión

El análisis identificó un grupo de ventas que superan claramente el comportamiento esperado, confirmando la heterogeneidad de los precios de la tienda.

* Conteo de Outliers Superiores: 7

    * Se detectaron 7 líneas de venta cuyo importe individual supera los $20345.25.

* Valor Máximo (Outlier Confirmado): $24865.00

    * El importe más alto registrado es de $24865.00, un valor que excede el límite superior de $20345.25 por una diferencia de más de $4500.00.

**Implicación Clave para la Tienda Aurelion:**

La existencia de 7 outliers de alto valor confirma que la Tienda Aurelion opera con un modelo dual de ingresos. Si bien la mayoría de los productos se venden a precios moderados (como lo mostró la Mediana de $6702.00), el segmento de productos premium o de lujo genera ventas de muy alto impacto que elevan significativamente el ingreso total. La estrategia de negocio debe enfocarse en nutrir y proteger a este pequeño segmento de productos de alto margen.

## Al menos 3 gráficos representativos

Esta sección de la documentación presenta las visualizaciones clave realizadas sobre los datos limpios de la Tienda Aurelion. Los gráficos tienen el propósito de transformar los resultados estadísticos calculados previamente en representaciones gráficas interpretables, permitiendo la identificación clara de patrones, distribuciones y valores atípicos (outliers).



### 1. Gráfico de Dispersión (Scatter Plot) de Importe vs. Cantidad

El Gráfico de Dispersión se utiliza para visualizar la relación entre dos variables numéricas: el importe (el valor total de la venta) y la cantidad (el número de unidades vendidas en esa línea). Este gráfico es clave para entender la correlación entre ambas variables.

**Propósito y Observación**

El objetivo es visualizar el grado y la dirección de la correlación lineal entre la cantidad de productos comprados y el importe total de esa línea de venta, tal como se analizó en la sección de Correlaciones.

* Correlación Positiva: Se observa una tendencia clara en la que, a medida que la cantidad de productos comprados aumenta, el importe total de la venta también tiende a incrementarse. Los puntos se agrupan siguiendo una dirección ascendente.

* Fuerza de la Relación: La nube de puntos no es perfectamente recta, lo que es coherente con una correlación positiva, pero imperfecta. La dispersión de los puntos se debe a la gran variación en el precio unitario de los productos de la tienda, lo que permite que una venta de baja cantidad de productos caros tenga un importe similar al de una venta de alta cantidad de productos baratos.

### 2. Gráfico de Barras (Bar Plot) por Medio de Pago

El Gráfico de Barras es la herramienta de visualización más clara para comparar la frecuencia o el valor total entre distintas categorías. En este caso, se utiliza para analizar la distribución total de las ventas (el valor en dinero) de la tienda según el medio_pago utilizado (Efectivo, QR, Transferencia, Tarjeta).

**Propósito y Observación**

El objetivo es cuantificar y visualizar qué método de pago genera la mayor cantidad de ingresos totales para la Tienda Aurelion. Los resultados obtenidos contradicen el supuesto tradicional de un E-commerce puramente digital.

* Motor de Ingresos: Efectivo: El gráfico revela que el Efectivo es, por un margen significativo, el medio de pago que acumula el mayor importe total de ventas. Este hallazgo es fundamental para la estrategia financiera de la tienda, ya que implica una gran dependencia del manejo de flujo de caja físico, probablemente a través de cobros en puntos de retiro o contra-entrega.

* Dominio Digital Secundario: El segundo método más relevante en términos de valor total es el QR. Le siguen la Transferencia y, por último, la Tarjeta, que es la que menos valor acumulado genera.

* Implicación Clave: Este patrón de uso (dominio de Efectivo) sugiere que la Tienda Aurelion atrae clientes que prefieren, o necesitan, métodos de pago no bancarizados o mixtos, incluso para sus compras más grandes. Esto tiene un impacto directo en la logística y la seguridad del manejo de dinero en la empresa.

### 3. Gráfico de Barras Horizontales de Top 10 Productos Más Vendidos
Este gráfico de barras horizontales muestra los 10 productos que han acumulado la mayor cantidad de unidades vendidas en el período analizado. Su objetivo es transformar la métrica de frecuencia (Moda) en una lista priorizada para el control de stock.

**Propósito y Observación (Orientada al Inventario)**
El objetivo es identificar los productos de mayor demanda para optimizar la gestión de inventario, que es parte del problema central del proyecto.

* Identificación de Productos "Estrella": La gráfica revela inmediatamente qué productos tienen la mayor rotación. Se observa, por ejemplo, que productos como "Salsa de Tomate 500g" y "Queso Rallado 150g" se venden en cantidades significativamente mayores que el resto.

* Prioridad de Stock: La gran diferencia en las longitudes de las barras subraya que la demanda no es uniforme. Los productos en el Top 3 deben tener un stock de seguridad superior, ya que su agotamiento (quedarse sin stock) representa una pérdida de venta inmediata y un impacto negativo en la satisfacción del cliente.

### 5. Gráfico de Líneas de Evolución Temporal de Ventas (Mensual)

Este gráfico de líneas muestra la variación del número de transacciones ($id\_venta$) a lo largo del tiempo, agrupando los datos mensualmente. Es esencial para identificar tendencias, estacionalidad o el impacto de campañas de marketing.

**Propósito y Observación (Orientada a la Optimización de Ventas)**
El objetivo es analizar la tendencia histórica para mejorar la planificación de la estrategia comercial y de marketing.

* Tendencia General: Se observa una tendencia general ascendente o al menos estable en el número de ventas desde enero hasta junio. Esto indica que la Tienda Aurelion está en crecimiento o mantiene su base de clientes mes a mes.

* Identificación de Picos y Valles: Si el gráfico muestra un pico notable (un mes con muchas más ventas), esto debe correlacionarse con alguna acción de marketing o estacionalidad (ej. promociones por una fecha especial). Si muestra valles (caídas), la tienda debe investigar los factores que lo causaron (ej. problemas en la plataforma o competencia).

* Conclusión: Este gráfico es crucial para la proyección de la demanda. Permite a la tienda anticipar las necesidades de stock y planificar las campañas de publicidad en los meses con menor rendimiento para estabilizar el flujo de ventas.

## Interpretación de resultados orientada al problema

Esta última sección de la documentación conecta todos los hallazgos estadísticos y visuales obtenidos en el Sprint 2 con el Problema Central del proyecto: la optimización de ventas y la gestión de inventario de la Tienda Aurelion. Los datos analizados revelan información crucial para la toma de decisiones estratégicas en el entorno de E-commerce.



### 1. La Cantidad es el Principal Motor del Ingreso

**Origen del Hallazgo**

El análisis de Correlación y el Gráfico de Dispersión (Scatter Plot) mostraron una relación positiva entre la cantidad de productos vendidos y el importe total de la línea de venta.

**Implicación - Optimización de Ventas**

Aunque la correlación no es perfecta (debido a la variación en los precios unitarios), la tendencia es clara: a mayor cantidad de unidades vendidas por transacción, mayor es el ingreso generado.

Esto orienta la estrategia de ventas hacia:

* Promociones de Volumen: Diseñar ofertas que incentiven a los clientes a agregar más productos al carrito (ejemplo: 3x2, descuentos por packs).

* Venta Cruzada (Cross-Selling): Implementar recomendaciones en el E-commerce para sugerir productos complementarios justo antes de finalizar la compra, buscando aumentar la cantidad en cada orden.

* Ticket Promedio: El foco debe ser aumentar el ticket promedio (el valor total de cada compra) mediante el incremento de la cantidad de ítems vendidos.

### 2. Foco en la Experiencia de Pago Digital

**Origen del Hallazgo**

El Gráfico de Barras por Medio de Pago reveló que el Efectivo es el medio que acumula la mayor parte del valor total de las transacciones (dinero ingresado), seguido por QR, Transferencia y, por último, Tarjeta.

**Implicación - Prioridad de la Experiencia E-commerce Mixta**

Dado que la Tienda Aurelion es un E-commerce, la experiencia de checkout (proceso de pago) es crítica. El predominio del Efectivo y la menor participación de la Tarjeta obligan a reevaluar la estrategia, pasando de un enfoque puramente digital a un modelo de experiencia de pago Mixto-Prioritario.

* Gestión del Flujo de Caja (Efectivo): La mayor preocupación debe ser la seguridad y eficiencia del proceso de cobro en efectivo. La tienda debe invertir en logística para asegurar el manejo, conteo y depósito seguro del dinero, dado que el Efectivo genera el mayor volumen de ingresos monetarios.

* Impulso Digital (QR): Si bien el Efectivo domina, el QR es el segundo más importante. La estrategia debe buscar incentivar la migración de los clientes de Efectivo hacia el QR. Esto reduciría la fricción logística y mejoraría la inmediatez de la transacción.

* Optimización de Recursos Digitales: La Tarjeta, al generar el menor importe, podría indicar problemas con las pasarelas de pago, altas comisiones o una desconfianza percibida. Se debe revisar el costo-beneficio de los pagos con Tarjeta, asegurando que la infraestructura sea robusta, pero reconociendo que no es el motor principal de los ingresos. La tienda debe garantizar que las opciones digitales más usadas (QR) sean lo más rápido y simple posible para aumentar la conversión.


### 3. Estrategia de Inventario basada en la Prioridad de Demanda

**Origen del Hallazgo**

El Gráfico de Barras de Top 10 Productos Más Vendidos identificó a los productos con mayor demanda por cantidad de unidades vendidas (ej. "Salsa de Tomate 500g").

**Implicación - Gestión de Inventario (Solución)**

La principal preocupación del problema era la gestión de inventario. Este análisis proporciona una solución directa a esa preocupación, transformando la planeación de stock de una tarea genérica a una tarea priorizada.

* Foco en la Rotación Rápida: La estrategia de inventario debe enfocarse en los productos del Top 3 o Top 5 de la lista, ya que estos generan la mayor cantidad de movimientos logísticos. La Tienda Aurelion debe establecer un Stock de Seguridad alto para estos productos y negociar acuerdos de compra por volumen con sus proveedores para reducir costos y evitar quiebres de stock (agotamiento).

* Alerta Temprana: Los productos en la base del Top 10 o fuera de él pueden tener una demanda más baja, lo que permite una estrategia de inventario Just-In-Time (justo a tiempo), ordenando solo lo que se necesita, ya que la prioridad de almacenamiento y recursos debe estar en los artículos de alta rotación. Esto optimiza el capital inmovilizado.

### 4. Planificación Comercial basada en la Tendencia de Ventas

**Origen del Hallazgo**

El Gráfico de Líneas de Evolución Temporal de Ventas mostró la tendencia del número de transacciones a lo largo de los meses.

**Implicación - Optimización de Ventas (Problema y Solución)**

La identificación de patrones temporales es esencial para la optimización de ventas (que es la otra parte del problema central). Entender la evolución permite pasar de una reacción a los eventos a una planificación proactiva.

* Identificación de Estacionalidad y Tendencia: Si la tendencia es ascendente, la tienda debe asegurar que la capacidad logística y de atención al cliente crezca al mismo ritmo. Si existen picos, estos deben estudiarse para replicar las condiciones (ej. campañas de email marketing específicas) en otros meses.

* Acciones Preventivas: Los meses con menor número de ventas deben ser objeto de una intervención comercial. La Tienda Aurelion puede planificar promociones fuertes, lanzamientos de nuevos productos o campañas de publicidad dirigidas justo antes o durante esos valles de ventas para estabilizar el flujo de ingresos y reducir la dependencia del rendimiento de un solo mes.

* Conclusión: La evolución de las ventas proporciona el marco para medir la efectividad de la Solución del proyecto: la implementación de análisis de datos. La tienda puede usar esta línea de tiempo para ver si las estrategias implementadas (ej. descuentos por volumen o cross-selling) logran aumentar el número total de transacciones en los meses siguientes.