# <h1 align=center> **BOOTCAMP DATA SCIENCE - PROYECTO INDIVIDUAL** </h1>

<br/>

## **Del caso a solucionar**

Una empresa relacionada al mundo del entretenimiento via streaming, desea mejorar su propuesta de valor, para ello nos acaba de contratar a nuestra consultora para desarrollar un Sistema de Recomendacion con Machine Learning.

Se llevaron a cabo las diferentes sesiones para entender que querian realmente, poder entrenar al modelo y asi poder resolver las consultas al modelo de prediccion 

El caso fue que al entregarnos la data, nuestro data Engineer se percato que la informacion no estaba totalmente limpia, por lo que habia que curar la data y dejar los archivos listos para la fase de creacion de la API, hacer el EDA y finalmente entrenar el modelo.

De entre lo mas relevante y en reunion con el cliente se propusieron hacer las siguiente transformaciones, siendo acompañados de un product owner de parte de cliente, para hacer las consultas puntuales campo por campo del negocio.

<br/>

## TRANSFORMACIONES A REALIZAR
Para esta primera etapa se acordo realizar las transformaciones de los siguiente campos, se detalla: 

+ Generar campo **`id`**: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = **`as123`**)

+ Los valores nulos del campo rating deberán reemplazarse por el string “**`G`**” (corresponde al maturity rating: “general for all audiences”

+ De haber fechas, deberán tener el formato **`AAAA-mm-dd`**

+ Los campos de texto deberán estar en **minúsculas**, sin excepciones

+ El campo ***duration*** debe convertirse en dos campos: **`duration_int`** y **`duration_type`**. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)

Este proceso entregaria dos archivos transformados, los cuales serian utilizados para desarrollar las consultas de a API, en una primera etapa en un jupiter notebook, usando Colab y con todos los resultados OK, se pasarian a probar desde VSC en un programa llamado main.py, ademas se usaria fastAPI de forma local para certificar que el API esta funcionando correctamente.

**CODIGO ETL**
Aqui dejamos el codigo ETL realizado:
https://github.com/RickDev31/PI_01_MLOPs_DATA08/blob/main/ETLMLOps.ipynb

<br/>



## DESARROLLO DE LA API
En trabajo en conjunto, se propusieron elaborar las siguientes consultas de la API, la cual detallamos:


+ Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse get_max_duration(year, platform, duration_type))

+ Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (la función debe llamarse get_score_count(platform, scored, year))

+ Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función debe llamarse get_count_platform(platform))

+ Actor que más se repite según plataforma y año. (La función debe llamarse get_actor(platform, year))

**Codigo Consulta API**
Aqui dejamos el codigo de las consultas desarrolladas y probadas:
https://github.com/RickDev31/PI_01_MLOPs_DATA08/blob/main/DesarrolloAPIMLOps.ipynb


**Codigo API**
Aqui dejamos el codigo de la API probadas con FastAPI:
https://github.com/RickDev31/PI_01_MLOPs_DATA08/blob/main/main.py

<br/>

## DEPLOYMENT
Para esta fase se propuso usar RENDER

<br/>

## EDA - ANALISIS EXPLORATORIO DE DATOS

Si bien entre el ETL hasta el EDA, se consume entre un 70% a 80% del tiempo del proyecto, es importante hacerlo porque se aprende de los datos, del como estan, que se pueden mejorar y en algunos casos proponer soluciones para que los datos sean grabados de forma correcta y asi no invertir tanto tiempo en la limpieza de las mismas. Tambien se busca entender como estan relacionados toda la informacion, posiblemente corregir algunos errores que se encuentren a mas detalle y finalmente tener la data curada. Finalmente dar unas conclusiones.

Esta etapa culmina con la generacion de dos archivos listos para entrenar a nuestro modelo de machine learning. Procediendo a la entrega de estos dos archivos al cliente via DRIVE.


**Codigo Consulta API**
Aqui dejamos el codigo de las consultas desarrolladas y probadas:
https://github.com/RickDev31/PI_01_MLOPs_DATA08/blob/main/EDAMLOps.ipynb

<br/>

## SISTEMA DE RECOMENDACION - MODELO MACHINE LEARNING


Una vez que toda la data es consumible por la API ya lista para consumir para los departamentos de Analytics y de Machine Learning, y nuestro EDA bien realizado entendiendo bien los datos a los que tenemos acceso, es hora de entrenar nuestro modelo de machine learning para armar un sistema de recomendación de películas para usuarios, donde dado un id de usuario y una película, nos diga si la recomienda o no para dicho usuario. De ser posible, este sistema de recomendación debe ser deployado para tener una interfaz gráfica amigable para ser utilizada, utilizando Gradio para su deployment o bien con alguna solución como Streamlit o algo similar en local (tener el deployment del sistema de recomendación o una interfaz gráfica es un plus al proyecto).

**Codigo modelo machine learning - sistema de recomendacion**
Aqui dejamos el codigo del modelo entrenado de machine learning:
https://github.com/RickDev31/PI_01_MLOPs_DATA08/blob/main/DesarrolloSISRECMLOps.ipynb

<br/>


## **Fuente de datos proporcionada por el cliente**

+ [Dataset](https://drive.google.com/drive/folders/1b49OVFJpjPPA1noRBBi1hSmMThXmNzxn): archivos originales, con ellos se realizo todo el presente proyecto
<br/>


## ENTREGABLES FINALES:
https://github.com/RickDev31/PI_01_MLOPs_DATA08/tree/main/datasetsML

