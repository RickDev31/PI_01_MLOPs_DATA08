from typing import Union
from fastapi import FastAPI
import pandas as pd
import numpy as np

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message" : "Here API... World"}

# ----------------------------------------------------------------------------------------
# DESARROLLO APIs
# las funciones fueron desarrolladas en Colab. Y se verifico su correcto funcionamiento
# dejamos link de acceso de las pruebas:
# https://colab.research.google.com/drive/1HdwYu128FkWdht0ab9PP7Mhbbiven4nq?usp=sharing
# ----------------------------------------------------------------------------------------


# ingestamos en el dataframe
df_peliculas = pd.read_csv("datasetsFinal\peliculas_final.csv", encoding="UTF8", sep=',')


"""
API 1
Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe # llamarse get_max_duration(year, platform, duration_type))
"""

#@app.get("/get_max_duration/{varanio}/{varplataforma}/{vartipo}")
#async def get_max_duration(varanio: int, varplataforma: str, vartipo: str):


@app.get('/get_max_duration')
async def get_max_duration(varanio: int, varplataforma: str, vartipo: str):
    dicc = {"netflix":"n","amazon":"a","hulu":"h","disney":"d"}

    df_x = df_peliculas[(df_peliculas.plataforma == dicc[varplataforma]) &  
                        (df_peliculas["type"] == "movie")    &
                        (df_peliculas["duration_type"] == vartipo) &
                        (df_peliculas["release_year"] == varanio) ]

    return df_x.duration_int.max()

### prueba de desarrollo
### get_max_duration(2021, "amazon", "min")
### rpta = 188



"""
API 2
Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (la función debe llamarse get_score_count(platform, scored, year))
"""
@app.get('/get_score_count')
async def get_score_count(varplataforma: str, varpuntaje: float, varanio: int):
    dicc = {"netflix":"n","amazon":"a","hulu":"h","disney":"d"}

    df_x = df_peliculas[(df_peliculas.plataforma == dicc[varplataforma]) &  
                        (df_peliculas["type"] == "movie")    &
                        (df_peliculas["score"] > varpuntaje) &
                        (df_peliculas["release_year"] == varanio) ]
            
    return len(df_x.index)

### prueba de desarrollo
### get_score_count("amazon", 3.6, 2021)
### rpta = 12



"""
API 3
Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función debe llamarse get_count_platform(platform))
"""
@app.get('/get_count_platform')
async def get_count_platform(varplataforma: str):
    dicc = {"netflix":"n","amazon":"a","hulu":"h","disney":"d"}

    df_x = df_peliculas[(df_peliculas.plataforma == dicc[varplataforma])   &   (df_peliculas["type"] == "movie")]
            
    return len(df_x.index)

### prueba de desarrollo
### get_count_platform("netflix")
### rpta = 6131



"""
API 4
Actor que más se repite según plataforma y año. (La función debe llamarse get_actor(platform, year))
"""
@app.get('/get_actor')
async def get_actor(varplataforma: str, varanio: int):

    dicc = {"netflix":"n","amazon":"a","hulu":"h","disney":"d"}

    df_x = df_peliculas[(df_peliculas.plataforma == dicc[varplataforma]) &  
                        (df_peliculas["release_year"] == varanio) ]

    df_y = df_x["cast"].str.split(',').explode().str.strip().value_counts()
    nombreactor = df_y.index[0]
    
    return nombreactor

### prueba de desarrollo
### get_actor("disney", 2021)
### rpta = "tress macneille"


