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



def info_hoteles(request_jeison):
    """
    Extrae información relevante sobre hoteles a partir de una respuesta JSON de un servicio de búsqueda de hoteles.

    La función itera sobre los resultados del JSON y extrae información clave sobre cada hotel, 
    incluyendo el nombre, número de reseñas, rating, rango de precios, ciudad, servicios ofrecidos y un enlace al hotel.
    Calcula además el precio medio por noche basado en el rango de precios.

    Args:
        request_jeison (dict): Un diccionario que representa la respuesta en formato JSON de un servicio de búsqueda de hoteles.

    Returns:
        list[dict]: Una lista de diccionarios, donde cada diccionario contiene la información de un hotel con las siguientes claves:
            - nombre_hotel: El nombre del hotel.
            - reviews_hotel: Número de reseñas del hotel.
            - rating_hotel: Rating del hotel.
            - precio_rango_min: El precio mínimo por noche en USD.
            - precio_rango_max: El precio máximo por noche en USD.
            - precio_medio_por noche: Precio medio por noche calculado a partir del rango de precios.
            - ciudad: Ciudad donde se encuentra el hotel.
            - servicios: Lista de servicios que ofrece el hotel.
            - link: URL que enlaza a la página del hotel.
    """
    lista_dicch=[]
    respond=request_jeison
    for i in range(0,len(respond["results"])):

        nombre_hotel=respond["results"][i]["name"]
        reviews_hotel=respond["results"][i]["reviews"]
        rating_hotel=respond["results"][i]["rating"]
        precio_rango_min=respond["results"][i]["price_range_usd"]["min"]
        precio_rango_max=respond["results"][i]["price_range_usd"]["max"]

        if precio_rango_min is not None and precio_rango_max is not None:
            precio_medio = (precio_rango_max + precio_rango_min) / 2
        else:
            precio_medio = None
            
        ciudad=respond["results"][i]["detailed_address"]["city"]
        servicios=respond["results"][i]["amenities"]
        link=respond["results"][i]["link"]

        
        dicch= {"nombre_hotel":nombre_hotel,
                "reviews_hotel":reviews_hotel,
                "rating_hotel": rating_hotel,
                "precio_rango_min":precio_rango_min,
                "precio_rango_max":precio_rango_max,
                "precio_medio_por noche":precio_medio,
                "ciudad":ciudad,
                "servicios":servicios,
                "link":link
                }
        lista_dicch.append(dicch)
    return lista_dicch
        






def crearDF_formateado_hoteles(funcion_info_hoteles):
    """
    Crea y devuelve un DataFrame formateado a partir de la información de hoteles obtenida.

    La función recibe una lista de diccionarios generada por la función `info_hoteles`, 
    convierte esa lista en un DataFrame y elimina las columnas "precio_rango_min" y "precio_rango_max",
    manteniendo solo la información relevante para el análisis.

    Args:
        funcion_info_hoteles (list[dict]): Lista de diccionarios con información sobre hoteles, 
        obtenida de la función `info_hoteles`.

    Returns:
        pd.DataFrame: Un DataFrame con los datos de hoteles, excluyendo las columnas "precio_rango_min" y "precio_rango_max".
    """

    df_hotel= pd.DataFrame(funcion_info_hoteles).drop(columns= ["precio_rango_min", "precio_rango_max"])
    df_hotel
    return df_hotel