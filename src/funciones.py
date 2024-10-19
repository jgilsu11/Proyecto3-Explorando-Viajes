from datetime import datetime
from geopy.geocoders import Nominatim
import pandas as pd
import numpy as np
import requests
import json
from tqdm import tqdm
from time import sleep
import os






def info_vuelos(request_jeison):
    """
    Extrae información relevante sobre vuelos a partir de una respuesta JSON de un servicio de itinerarios de vuelos.

    La función itera sobre los vuelos y sus tramos (piernas) en el JSON de respuesta, extrayendo información
    como el precio, aeropuertos de origen y destino, tiempos de salida y llegada, duración del vuelo, escalas y aerolíneas.
    Luego organiza esta información en una lista de diccionarios.

    Args:
        request_jeison (dict): Un diccionario que representa la respuesta en formato JSON de un servicio de vuelos.

    Returns:
        list[dict]: Una lista de diccionarios, donde cada diccionario contiene la información de un tramo de vuelo con las siguientes claves:
            - id_origen: ID del aeropuerto de origen.
            - ciudad_origen: Nombre de la ciudad de origen.
            - id_destino: ID del aeropuerto de destino.
            - ciudad_destino: Nombre de la ciudad de destino.
            - salida: Hora y fecha de salida del vuelo.
            - llegada: Hora y fecha de llegada del vuelo.
            - duracion(min): Duración del vuelo en minutos.
            - escalas: Número de escalas del vuelo.
            - aerolinea: Nombre de la aerolínea que opera el vuelo.
            - precio: Precio del vuelo (formato raw).
    """
    lista_dicc=[]
    res= request_jeison["data"]

    for vuelo in range(0,len(res["itineraries"])): 
        precio= res["itineraries"][vuelo]["price"]["raw"]

        for i in range(0,2):
                id_origen= res["itineraries"][vuelo]["legs"][i]["origin"]["id"]
                origen= res["itineraries"][vuelo]["legs"][i]["origin"]["city"]

                id_destino= res["itineraries"][vuelo]["legs"][i]["destination"]["id"]
                destino= res["itineraries"][vuelo]["legs"][i]["destination"]["city"]

                duracion_minuts= res["itineraries"][vuelo]["legs"][i]["durationInMinutes"]
                escalas= res["itineraries"][vuelo]["legs"][i]["stopCount"]

                salida= res["itineraries"][vuelo]["legs"][i]["departure"]
                llegada= res["itineraries"][vuelo]["legs"][i]["arrival"]

                aerolinea= res["itineraries"][vuelo]["legs"][i]["carriers"]["marketing"][0]["name"]

                dicc= {"id_origen":id_origen,
                "ciudad_origen":origen,
                "id_destino": id_destino,
                "ciudad_destino":destino,
                "salida":salida,
                "llegada":llegada,
                "duracion(min)":duracion_minuts,
                "escalas":escalas,
                "aerolinea":aerolinea,
                "precio":precio
                }
                lista_dicc.append(dicc)
    return lista_dicc





def crearDF_formateado(funcion_info_vuelos):
    """
    Crea y devuelve un DataFrame formateado a partir de la información de vuelos obtenida.

    La función recibe una lista de diccionarios generada por la función `info_vuelos`, 
    convierte esa lista en un DataFrame y formatea las columnas de "salida" y "llegada" 
    como objetos datetime.

    Args:
        funcion_info_vuelos (list[dict]): Lista de diccionarios con información sobre vuelos, 
        obtenida de la función `info_vuelos`.

    Returns:
        pd.DataFrame: Un DataFrame con los datos de vuelos, donde las columnas "salida" y "llegada"
        están formateadas como datetime.
    """

    df_vuelos_ida_vuelta= pd.DataFrame(funcion_info_vuelos)
    df_vuelos_ida_vuelta["salida"]= pd.to_datetime(df_vuelos_ida_vuelta["salida"])
    df_vuelos_ida_vuelta["llegada"]= pd.to_datetime(df_vuelos_ida_vuelta["llegada"])
    return df_vuelos_ida_vuelta