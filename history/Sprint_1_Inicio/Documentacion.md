# Tienda Aurelion
## Tema: Tienda Aurelion como E-commerce 
El tema central de nuestro proyecto es definir el contexto de la Tienda Aurelion como una plataforma de E-commerce (Comercio Electrónico). Al elegir el E-commerce, establecemos que la tienda opera completamente en el entorno digital, sin la limitación de una ubicación física, lo que abre un mundo de posibilidades y, a la vez, de desafíos únicos que la distinguen del Retail tradicional.

En el mundo del E-commerce, el éxito no solo depende de tener buenos productos, sino de entender la experiencia digital del cliente. A diferencia de una tienda física donde un vendedor puede observar y guiar al cliente, en el entorno digital, esa guía y personalización debe ser gestionada por los datos. Nuestra base de datos es, de hecho, el rastro digital de cada interacción: cada fila en el archivo Ventas y Detalle_ventas es una visita y una compra que se concretó en línea; cada registro en Clientes es una persona que decidió confiar en la plataforma.

Establecer este contexto como E-commerce implica que el objetivo principal de nuestro proyecto será potenciar la estrategia digital de la tienda, utilizando los datos para informar y mejorar los procesos centrales del negocio. Es decir, aprovecharemos la información de las ventas para dirigir de forma más inteligente la inversión en campañas de marketing (publicidad), para asegurar que tengamos en stock los productos más demandados (gestión de inventario) y, fundamentalmente, para construir una relación duradera y rentable con cada cliente.

## Problema: Reflexiones y Desarrollo de Inconvenientes Clave 
Para llegar a problemas concretos y relevantes, es fundamental primero hacer un ejercicio de reflexión y cuestionamiento sobre la operación de la Tienda Aurelion. Esto nos permite conectar los datos disponibles con las necesidades reales de negocio.

### Preguntas de Reflexión
Antes de definir un problema, nos preguntamos:

* **Sobre el Cliente** (Archivos Clientes y Ventas): 
    * ¿Existe un perfil de cliente ideal para Tienda Aurelion? 
    * ¿Los clientes de una ciudad en particular (columna ciudad en Clientes) son más valiosos o compran con mayor frecuencia que otros? 
    * ¿Qué diferencia a un cliente que compra una sola vez de uno que vuelve a los tres meses?
    * ¿Cuánto tiempo, en promedio, transcurre entre la fecha de alta de un cliente (fecha_alta en Clientes) y su primera compra?
    * ¿Existe una correlación entre la fecha_alta del Cliente y el tipo de productos que compra (categorías de Productos)?

* **Sobre el Producto** (Archivos Productos y Detalle_ventas): 
    * ¿Cómo impacta la categoría del producto en el volumen de ventas?  
    * ¿Cuáles son los productos que más se compran juntos (más allá de la simple cantidad) y que podríamos promocionar en un "pack"?
    * ¿Hay productos específicos que tienen un precio_unitario alto pero se venden muy poco? Permite identificar artículos de "lujo" o aquellos que necesitan un impulso en marketing.
    * ¿Hay alguna categoría de productos que tiende a comprarse en grandes cantidades (en Detalle_ventas) en una sola transacción, independientemente de su precio_unitario?
    * ¿Cuáles son los 5 productos individuales (nombre_producto en Productos) más vendidos en términos de cantidad total de unidades, y cuáles son los 5 con el menor número de ventas?

* **Sobre la Venta** (Archivo Ventas y Detalle_ventas): 
    * ¿El medio_pago (tarjeta, QR, efectivo, transferencia) influye en el importe total de la compra? 
    * ¿Las ventas tienen picos o valles en ciertas fechas (fecha en Ventas) que la tienda podría aprovechar con ofertas?
    * ¿En qué días de la semana (Lunes, Martes, etc.) se registra la mayor cantidad de ventas?
    * ¿Los clientes que compran muchos productos a la vez suelen usar un medio_pago específico (como tarjeta, QR o transferencia)?

### Desarrollo de Problemas Clave Vinculados a los Datos
A partir de estas reflexiones, identificamos dos problemas principales que la tienda enfrenta y que pueden ser atacados con nuestros datos:

#### Problema 1: El Problema de No Conocer a Nuestros Mejores Clientes
La Tienda Aurelion posee los datos de sus clientes (id_cliente, email, fecha_alta), pero no está utilizando esta información para segmentar o identificar a sus clientes más valiosos. El problema es la falta de un sistema para clasificar a los clientes según su comportamiento de compra. Sin saber quién es el cliente que más gasta o que compra con mayor frecuencia (datos extraíbles de Ventas y Detalle_ventas), la tienda gasta los mismos recursos de marketing en todos. Esto lleva a:

* Campañas de marketing genéricas e ineficientes.

* Pérdida de la oportunidad de fidelizar a los mejores compradores.

* Falta de predicción sobre qué clientes están a punto de dejar de comprar (clientes inactivos).

#### Problema 2: Ineficiencia en la Oferta de Productos (Gestión de Inventario y Promoción)

El catálogo de la tienda (Productos) es extenso y contiene diferentes categorías. El problema es que se desconoce el rendimiento real y combinado de los productos. La tienda sabe cuánto vende de cada artículo, pero no sabe si está promocionando los productos correctos en el momento correcto. Esto se traduce en:

* Desperdicio de espacio digital/publicitario en productos que rara vez se compran.

* Falta de estrategias de venta cruzada (sugerir productos complementarios). Por ejemplo, si los datos de Detalle_ventas muestran que el producto A y el producto B se compran siempre juntos, no promocionarlos juntos es una pérdida de venta segura.

*** 
## Solución: Primera Fase de Proyecto: El Diseño de un Marco de Análisis de Datos
El objetivo de esta fase de Solución es establecer el Plan Metodológico que transformará los datos brutos en conocimiento útil. Nuestra solución, por lo tanto, consiste en la definición precisa de las métricas clave y los pasos lógicos que guiarán el desarrollo del proyecto. Este proceso es conocido como la Fase de Descubrimiento y Definición dentro de cualquier proyecto de Inteligencia Artificial y es el cimiento para garantizar que el trabajo futuro resuelva los problemas de negocio identificados.

La solución propuesta es el desarrollo de un Marco de Análisis Descriptivo que resuelva las preguntas y problemas planteados, centrándose en el proceso para transformar los datos sin procesar (Datos) en conocimiento útil (Insights).
***

### 1. Marco de Medición para el Cliente (Atacando el Problema 1)
Para atacar el Problema 1, proponemos crear un marco de medición simple que use las columnas numéricas de nuestros archivos. Este marco se centrará en obtener tres métricas clave para cada cliente, que luego usaremos para clasificar a la clientela.

#### A.Transformación del Dato en Información (Definición de Métricas):

* **Frecuencia (F):** Con base en el archivo Ventas, calcularemos la cantidad de veces que cada cliente (id_cliente) ha realizado una compra. Esto nos dirá quién compra más a menudo.

* **Monto Monetario (M):** Utilizando el archivo Detalle_ventas y el campo importe, calcularemos el gasto total acumulado de cada cliente a lo largo del tiempo. Esto nos dirá quién es el que más dinero deja en la tienda.

* **Producto (P) / Preferencia de Categoría:** Usando el archivo Productos (columna categoría) y Detalle_ventas, identificaremos qué tipo de categoría domina en las compras de cada cliente. Esto nos dirá qué tipo de oferta debemos enviar a ese cliente.

#### B. Generación de la Solución Conceptual (La Clasificación):
Una vez que tengamos estas métricas F, M y P, la solución consiste en clasificar a los clientes en grupos muy sencillos:

* **Grupo "VIP":** Clientes con alta Frecuencia y alto Monto Monetario. La solución de negocio será crear un programa de lealtad para ellos.

*  **Grupo "Promesa":** Clientes con alta Frecuencia pero bajo Monto Monetario. Es decir, Clientes que compran muy seguido pero gastan poco dinero en cada compra. La solución será incentivar la compra de productos de mayor valor para que aumenten su gasto promedio.

* **Grupo "Dormido":** Clientes que compraron hace mucho tiempo (mirando la fecha en Ventas) y tienen baja Frecuencia. La solución será enviarles ofertas especiales para reactivarlos.
***
### 2. Marco de Análisis para el Producto (Atacando el Problema 2)

Para resolver el Problema 2 (Ineficiencia en la Oferta de Productos), definiremos dos análisis descriptivos clave. Estos análisis nos darán la información necesaria para saber qué productos promocionar y cómo manejar el inventario de forma más eficiente.

#### A. Análisis de Desempeño de Inventario (Productos Más y Menos Vendidos)

* **Métrica Clave:** Unidades Vendidas por Producto.

* **Procedimiento:** Identificar y clasificar los 5 productos (nombre_producto en Productos) con la mayor cantidad total de unidades vendidas y los 5 productos con la menor cantidad de ventas. Esto se logra sumando la columna cantidad del archivo Detalle_ventas para cada producto.

* **Explicación Sencilla:** Este análisis nos muestra qué productos son los favoritos de los clientes y cuáles apenas se están vendiendo. Es una vista esencial para la gestión de inventario.

* **Solución de Negocio:** La tienda puede usar esta información para asegurar el stock de los productos más vendidos y evitar quiebres. Para los menos vendidos, puede decidir si debe descontinuarlos o crear ofertas agresivas y promociones especiales para liquidar ese stock.

#### B. Análisis de Productos Comprados Juntos (Venta Cruzada)

* **Métrica Clave:** Frecuencia de Compra Conjunta (Productos que aparecen juntos en una venta).

* **Procedimiento:** Analizar el archivo Detalle_ventas para determinar qué pares o grupos de productos son comprados consistentemente juntos en la misma id_venta. Esto implica agrupar las ventas y buscar patrones en los productos que las componen.

* **Explicación Sencilla:** Buscamos patrones de compra, por ejemplo, si el cliente que compra "Café Molido" también compra casi siempre "Leche Entera". Al encontrar esta asociación, podemos "empacar" o sugerir los productos complementarios.

* **Solución de Negocio:** Este resultado permite crear estrategias de venta cruzada ("pack") efectivas. Si se identifican productos que se compran juntos, se deben promocionar en conjunto en el sitio web (ej. "otros clientes compraron esto") o en correos de marketing para aumentar el importe total de cada venta.
***

### Resumen de la Solución Conceptual

La solución en esta primera fase es el modelo conceptual y las métricas basadas en los datos (F,M y P para Cliente y Asociación/Desempeño para Producto) que la Tienda Aurelion debe usar para transformar sus archivos planos en información útil y accionable, resolviendo sus principales problemas de negocio.

***
***
***
***
## Estructura de Datos: Fuente, Definición, Tipos y Escala

Esta sección es el plano fundamental de nuestro proyecto, tal como se define en la Fase de Fundamentos del Dato. Comprender la Fuente, Estructura, Tipos y Escala de la información es el primer paso crítico para asegurar la calidad del dato y evitar errores en los cálculos. Aquí documentamos exactamente cómo están organizados los archivos brutos de Tienda Aurelion.

En resumen, nuestra base de datos es como el registro total de la tienda digital (e-commerce) de Tienda Aurelion. Guarda la información de quién compra (la lista de Clientes), qué artículos se venden (la lista de Productos), y cada vez que alguien hace una compra (las tablas Ventas y Detalle_ventas) en la plataforma digital.

### Fuente de Datos (Origen)

La información que alimenta nuestro análisis proviene de los dos sistemas operativos principales de la tienda:

- **Sistema de Punto de Venta (POS):** Aporta las transacciones diarias, generando las tablas Ventas, Detalle_ventas y Productos. Estos datos son dinámicos y reflejan la actividad comercial constante.
- **Base de Datos de Gestión de Clientes (CRM):** Proporciona la tabla Clientes, con la información estática (nombres, emails, fechas de registro) necesaria para personalizar las ofertas.

### Estructura y Definición (Modelo Relacional)

Los datos se organizan en cuatro archivos (tablas) en formato CSV, que en conjunto forman un modelo relacional simple. Este diseño es clave: en lugar de tener un solo archivo gigante y repetitivo, las tablas se enlazan mediante Claves Principales (PK) y Claves Foráneas (FK). Por ejemplo:

- La tabla **Ventas** se conecta con **Clientes** a través de **id_cliente**.
- La tabla **Detalle_ventas** se conecta con **Ventas** (por **id_venta**) y con **Productos** (por **id_producto**).

Este modelo nos permite obtener la información detallada (ej. el Monto Monetario) uniendo de manera eficiente todos los archivos que describen quién compra, qué compra y cuándo lo hace.

A continuación, se detalla la estructura de campos de cada uno de los cuatro archivos CSV:

### 1. Clientes
**Definición:** Tabla maestra que almacena todos los datos de las personas registradas en la tienda. 

**Estructura de Campos**

1. id_cliente
    * **Definición:** Código único que identifica a cada persona.
    * **Tipo de Dato (Python):** Entero (int)
    * **Escala de Medida:** Nominal
    * **Rol en la BD:** Clave Principal (PK)
2. nombre_cliente
    * **Definición:** Nombre completo de la persona.
    * **Tipo de Dato (Python):** Texto (str)
    * **Escala de Medida:** Nominal
    * **Rol en la BD:** Atributo
3. email
    * **Definición:** Correo electrónico de contacto.
    * **Tipo de Dato (Python):** Texto (str)
    * **Escala de Medida:** Nominal
    * **Rol en la BD:** Atributo
4. ciudad
    * **Definición:** Ubicación geográfica donde reside el cliente.
    * **Tipo de Dato (Python):** Texto (str)
    * **Escala de Medida:** Nominal
    * **Rol en la BD:** Atributo
5. fecha_alta
    * **Definición:** Fecha en que el cliente se registró en el sistema.
    * **Tipo de Dato (Python):** Fecha (date)
    * **Escala de Medida:** Intervalo
    * **Rol en la BD:** Atributo

### 2. Ventas
**Definición:** Es la "cabecera" de cada transacción. Contiene información general de la compra, como la fecha y el método de pago. Se relaciona con la tabla Clientes a través de id_cliente.

**Estructura de Campos**

1. id_venta
    * **Definición:** Código único que identifica a cada transacción de compra.
    * **Tipo de Dato (Python):** Entero (int)
    * **Escala de Medida:** Nominal
    * **Rol en la BD:** Clave Principal (PK)
2. fecha
    * **Definición:** Fecha y hora en que se realizó la venta.
    * **Tipo de Dato (Python):** Fecha (date)
    * **Escala de Medida:** Intervalo
    * **Rol en la BD:** Atributo
3. id_cliente
    * **Definición:** Código del cliente que realizó la compra.
    * **Tipo de Dato (Python):** Entero (int)
    * **Escala de Medida:** Nominal
    * **Rol en la BD:** Clave Foránea (FK)
4. nombre_cliente 
    * **Definición:** Nombre del cliente (presente en la fuente original).
    * **Tipo de Dato (Python):** Texto (str)
    * **Escala de Medida:** Nominal
    * **Rol en la BD:** Atributo
5. email 
    * **Definición:** Email del cliente (presente en la fuente original).
    * **Tipo de Dato (Python):** Texto (str)
    * **Escala de Medida:** Nominal
    * **Rol en la BD:** Atributo
6. medio_pago
    * **Definición:** Forma en que se efectuó el pago (ej. tarjeta, efectivo, QR).
    * **Tipo de Dato (Python):** Texto (str)
    * **Escala de Medida:** Nominal
    * **Rol en la BD:** Atributo

### 3. Productos
**Definición:** Tabla maestra que contiene el catálogo de artículos que vende la tienda.

**Estructura de Campos**

1. id_producto
    * **Definición:** Código único que identifica a cada artículo.
    * **Tipo de Dato (Python):** Entero (int)
    * **Escala de Medida:** Nominal
    * **Rol en la BD:** Clave Principal (PK)
2. nombre_producto
    * **Definición:** Nombre descriptivo del artículo (ej. 'Leche Entera 1L').
    * **Tipo de Dato (Python):** Texto (str)
    * **Escala de Medida:** Nominal
    * **Rol en la BD:** Atributo
3. categoria
    * **Definición:** Clasificación del producto (ej. 'Alimentos', 'Limpieza').
    * **Tipo de Dato (Python):** Texto (str)
    * **Escala de Medida:** Nominal
    * **Rol en la BD:** Atributo
4. precio_unitario
    * **Definición:** Precio de venta del producto antes de descuentos o cantidad.
    * **Tipo de Dato (Python):** Entero (int)
    * **Escala de Medida:** Razón
    * **Rol en la BD:** Atributo

### 4. Detalle_ventas
**Definición:** El corazón de los datos. Esta tabla relaciona cada venta con los productos específicos que se llevaron, las cantidades y los ingresos generados. Permite los cálculos de Monto Monetario y Asociación de Productos.

**Estructura de Campos**

1. id_venta
    * **Definición:** Código de la transacción.
    * **Tipo de Dato (Python):** Entero (int)
    * **Escala de Medida:** Nominal
    * **Rol en la BD:** Clave Compuesta (PK/FK)
2. id_producto
    * **Definición:** Código del producto comprado en esta transacción.
    * **Tipo de Dato (Python):** Entero (int)
    * **Escala de Medida:** Nominal
    * **Rol en la BD:** Clave Compuesta (PK/FK)
3. nombre_producto 
    * **Definición:** Nombre del producto (presente en la fuente original).
    * **Tipo de Dato (Python):** Texto (str)
    * **Escala de Medida:** Nominal
    * **Rol en la BD:** Atributo
4. cantidad
    * **Definición:** Número de unidades de ese producto compradas.
    * **Tipo de Dato (Python):** Entero (int)
    * **Escala de Medida:** Razón
    * **Rol en la BD:** Atributo
5. precio_unitario 
    * **Definición:** Precio al que se vendió la unidad (presente en la fuente original).
    * **Tipo de Dato (Python):** Entero (int)
    * **Escala de Medida:** Razón
    * **Rol en la BD:** Atributo
6. importe
    * **Definición:** Importe total de ese producto dentro de la venta (cantidad x precio_unitario).
    * **Tipo de Dato (Python):** Entero (int)
    * **Escala de Medida:** Razón
    * **Rol en la BD:** Métrica




## Sugerencias y mejoras aplicadas con Copilot


### Sugerencias de Optimización de Código (Programa.py)

#### Refactorización de Constantes de Formato

**¿Por qué es una mejora?**

Actualmente, los anchos de columna están definidos individualmente al inicio de la función `print_esquema_tabla`. Es mejor práctica definirlos como constantes globales o en un diccionario de configuración.
```python
# Antes de la función, definir:
ANCHOS_COLUMNAS = {
    'campo': 20,
    'tipo': 15,
    'escala': 20,
    'rol': 25
}
```

#### Optimización de Manejo de Tiempo en Menús

**¿Por qué es una mejora?**

El uso de `time.sleep(3)` en diferentes partes del código crea una experiencia de usuario inconsistente. Se sugiere implementar una función centralizada para el manejo de pausas:
```python
def pausa_interfaz(duracion=3):
    print("\nPresione Enter para continuar...")
    return input()
```

#### Estructura de Datos Eficiente para Tablas

**¿Por qué es una mejora?**

Las tablas están definidas como listas de listas independientes. Se recomienda usar diccionarios para relacionar la descripción con sus campos, mejorando la cohesión y mantenibilidad del código:
```python
tabla_clientes = {
    'descripcion': tabla_clientes_desc,
    'campos': tabla_clientes_campos
}
```

### Sugerencias de Mejora de Documentación (Documentacion.md)

#### Estructuración de Métricas

**¿Por qué es una mejora?**

En la sección "Marco de Medición para el Cliente", las métricas F, M y P están presentadas en una lista simple. Se sugiere usar una tabla markdown para mejorar la visualización:

| Métrica | Significado | Fuente de Datos |
|---------|-------------|-----------------|
| F (Frecuencia) | Cantidad de compras | Ventas |
| M (Monto) | Gasto total | Detalle_ventas |
| P (Producto) | Categoría preferida | Productos |

#### Jerarquía Visual de Problemas

**¿Por qué es una mejora?**

Los problemas clave (Problema 1 y 2) podrían beneficiarse de una estructura más visual. Se sugiere agregar un resumen ejecutivo en forma de diagrama o lista con viñetas al inicio de cada problema, seguido por el detalle:

##### Problema 1: No Conocer a Nuestros Mejores Clientes

> **Resumen Ejecutivo**
> * **Situación Actual:** Datos sin clasificación
> * **Impacto:** Marketing ineficiente
> * **Métrica Afectada:** ROI de campañas

Desarrollo detallado del problema...

---

Con estas sugerencias, el código será más mantenible y la documentación más clara y profesional, manteniendo la simplicidad requerida sin depender de bibliotecas externas.

## Información, pasos y pseudocódigo 
### Información del Programa

El archivo Programa.py no es un script de análisis de datos tradicional, sino una Interfaz Interactiva de Consulta.

Su función principal es servir como un lector dinámico y navegable de toda la documentación del proyecto (Tema, Problema, Solución, Estructura de Datos y Sugerencias de Copilot), permitiendo al usuario acceder a las distintas secciones a través de un Menú principal que se ejecuta en la consola.

De esta forma, se cumple con el requerimiento de tener un programa Python que permita obtener la información del proyecto de manera interactiva.

### Pasos del Programa

1. El flujo de ejecución del programa es simple y cíclico:

2. Inicio: La función principal (main()) inicializa el programa.

3. Menú: El programa entra en un bucle infinito que imprime el Menú Principal con 7 opciones.

4. Captura de Opción: El usuario ingresa un número.

5. Lógica Condicional: Una estructura IF-ELSE evalúa la opción:

    *   Si la opción es 1, se muestra un Submenú para navegar por Tema, Problema y Solución.

    *   Si es de 2 a 6, se llama a la función correspondiente para imprimir la información estática (ej., mostrar_estructura_tablas).

    *   Si la opción es 7, se rompe el bucle y el programa finaliza.

6. Pausa/Espera: Después de mostrar la información, el programa espera un tiempo (time.sleep) o solicita una nueva acción, volviendo al paso 2.

### Pseudocódigo 

```

REPETIR
    // 2.1. Mostrar opciones del Menú
    IMPRIMIR "**************************************************"
    IMPRIMIR "    MENÚ DE CONSULTA - PROYECTO TIENDA AURELION"
    IMPRIMIR "**************************************************"
    IMPRIMIR "1. Mostrar Documentación General"
    IMPRIMIR "2. Fuente de datos y Descripción"
    IMPRIMIR "3. Mostrar Estructura de Tablas"
    IMPRIMIR "4. Mostrar Metodología y Pasos"
    IMPRIMIR "5. Mostrar Sugerencias de Copilot"
    IMPRIMIR "6. Mostrar Integrantes de equipo"
    IMPRIMIR "7. Salir del Programa"

    
    LEER OPCION

   
    SI OPCION = '1' ENTONCES
        LEER OPCION_SUBMENU

            SI OPCION_SUBMENU = '1' ENTONCES
                IMPRIMIR SALTO_DE_LINEA + "Tema: Análisis de Datos de la Tienda Aurelion"
                ESPERAR 3 SEGUNDOS
            SINO SI OPCION_SUBMENU = '2' ENTONCES
                IMPRIMIR SALTO_DE_LINEA + "Problema: Optimización de ventas y gestión de inventario"
                ESPERAR 3 SEGUNDOS
            SINO SI OPCION_SUBMENU = '3' ENTONCES
                IMPRIMIR SALTO_DE_LINEA + "Solución: Implementación de análisis de datos para mejorar decisiones comerciales"
                ESPERAR 3 SEGUNDOS
            SINO SI OPCION_SUBMENU = '4' ENTONCES
                ROMPER BUCLE // Volver al Menú Principal
            SINO
                IMPRIMIR MENSAJE DE ERROR: "Opción de submenú no válida."
                ESPERAR 1 SEGUNDO
            FIN SI

        FIN REPETIR
    SINO SI OPCION = '2' ENTONCES
        LLAMAR FUNCIÓN MOSTRAR_FUENTE_DATOS
    SINO SI OPCION = '3' ENTONCES
        LLAMAR FUNCIÓN MOSTRAR_ESTRUCTURA_TABLAS
    SINO SI OPCION = '4' ENTONCES
        LLAMAR FUNCIÓN MOSTRAR_METODOLOGIA_PASOS
    SINO SI OPCION = '5' ENTONCES
        LLAMAR FUNCIÓN MOSTRAR_COPILOT_SUGERENCIAS
    SINO SI OPCION = '6' ENTONCES
        IMPRIMIR LISTA DE INTEGRANTES
        ESPERAR 3 SEGUNDOS
    SINO SI OPCION = '7' ENTONCES
        IMPRIMIR MENSAJE DE SALIDA
        ROMPER BUCLE // Detiene el bucle y termina el programa
    SINO
        IMPRIMIR MENSAJE DE ERROR: "Opción no válida."
        ESPERAR 1 SEGUNDO
    FIN SI

FIN REPETIR
```





