# Proyecto Final de entrega para curso Data Scientist de CoderHouse

Proyecto Final Entrega para Coderhouse

Índice

1. Adquisición de datos.
2. Análisis.
3. Información adicional.


## Adquisicion de datos

Para la adquisición de datos se utilizó la API pública de **MercadoLibre** y **Python**. Se puede acceder al código empleado haciendo click aquí. Esta api presenta algunas limitaciones en cuanto al número de resultados que es posible obtener en una sola búsqueda, sin embargo, es posible aplicar diferentes filtros y obtener resultados diferentes cada vez. Teniendo esto en mente se consideró una diversa configuración de estos filtros con diferentes condiciones, de manera que en cada búsqueda se pudieran traer datos diferentes. Los datos fueron recolectados utilizando procesamiento paralelizado y almacenados como JSON. Una vez recolectados, se filtraron los datos para eliminar los duplicados.
De esta manera fue posible conseguir un dataset de unos **100.000 registros diferentes**, datos con los que se trabajó durante este proyecto.