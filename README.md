# Proyecto Final de entrega para curso Data Scientist de CoderHouse

Proyecto Final Entrega para Coderhouse

## Índice
1. Introducción
2. Adquisición de datos
3. Análisis y Procesamiento
4. Documentación ejecutiva
5. Información adicional

## 1. Introducción

Este repositorio forma parte de la entrega final para el curso de Data Sciende de CoderHouse.

La idea general del proyecto es utilizar datos de la API de MercadoLibre, hacer análisis con esos datos y entrenar modelos de Machine Learning que solucionen un problema.

## 2. Adquisicion de datos

Para la adquisición de datos se utilizó la API pública de **MercadoLibre** y **Python**. Se puede acceder al código en su [sección del repositorio](https://github.com/SantiagoCarranza/entrega-final-data-science-coderhouse/tree/main/scrapping). Esta api presenta algunas limitaciones en cuanto al número de resultados que es posible obtener en una sola búsqueda, sin embargo, es posible aplicar diferentes filtros y obtener resultados diferentes cada vez. Teniendo esto en mente se consideró una diversa configuración de estos filtros con diferentes condiciones, de manera que en cada búsqueda se pudieran traer datos diferentes. Los datos fueron recolectados utilizando procesamiento paralelizado y almacenados como JSON. Una vez recolectados, se filtraron los datos para eliminar los duplicados.
De esta manera fue posible conseguir un dataset de unos **100.000 registros diferentes**, datos con los que se trabajó durante este proyecto.

## 3. Análisis y Procesamiento

Entre los análisis que se realizaron se encuentra análisis univariado, bivariado y multivariado.

Entrenamos también modelos de inteligencia artificial, principalmente de clasificación.

Estos datos pueden ser revisados [aquí](https://github.com/SantiagoCarranza/entrega-final-data-science-coderhouse/blob/main/Entrega_Proyecto_Final_Carranza_Delgado.ipynb).

## 4. Documentación ejecutiva

El enlace a la presentación en google slides puede ser encontrado haciendo [click aquí.](https://docs.google.com/presentation/d/163T3Jah_a1329sQAkT7A-dvmemtaUX5PeAbw-u3rzFA/edit#slide=id.p)

