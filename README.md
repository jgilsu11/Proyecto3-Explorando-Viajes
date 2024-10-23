

![Mallorca vs Tenerife](imagen.webp)


**Elección de mejor destino para vacaciones en solitario**


***Descripción:***
El proyecto 3 consiste en la extracción, exploración, limpieza, y análisis de los datos de vuelos, alojamientos y actividades haciendo uso de archivos.py y Jupyter notebook.

Las técnicas usadas durante el proyecto son en su mayoría aquellas enseñadas durante la tercera semana de formación (Uso de APIs, web scrapping,creación de gráfica y formateos entre otros).

Adicionalmente, se usaron recursos obtenidos mediante research en documentación especializada, vídeos de YouTube e IA como motor de búsqueda y apoyo al aprendizaje.


***Estructura del Proyecto:***

El desarrollo del proyecto se gestionó de la siguiente manera:

- _En Primer lugar_, haciendo uso de JupyterNotebook como primer paso donde realizar ensayos con el código.  
 Estos jupyter se dividen en extracción y limpieza, exploración y visualización.

- _En Segundo Lugar_, se creó una presentación basada en los datos.

- _Finalmente_, se realizó la documentación del proyecto en un archivo README (documento actual).

Por todo lo anterior, el usuario tiene acceso a:

        ├── notebooks/           # Notebooks de Jupyter 
        ├── src/                 # Scripts (.py)
        ├── README.md            # Descripción del proyecto
        ├── Presentación         # Presentcaión del proyecto
***Requisitos e Instalación🛠️:***

Este proyecto usa Python 3.11.9 y bibliotecas que se necesitarán importar al principio del código como:
datetime, 
    - [pandas](https://pandas.pydata.org/docs/) para manipulación de datos 🧹
    - [numpy](https://numpy.org/doc/2.1/) para cálculos numéricos 🔢
    - [matplotlib](https://matplotlib.org/stable/index.html) y [seaborn](https://seaborn.pydata.org/) para visualización de datos 📊
    - [requests](https://requests.readthedocs.io/en/latest/) y [beautifulsoup4](https://beautiful-soup-4.readthedocs.io/en/latest/)

***Aportación al Usuario🤝:***

El doble fin de este proyecto incluye tanto el aprendizaje y formación por parte del desarrollador como la intención de servir de recomendación y orientación a un viajero solitario.
Este viajero podrá elegir entre presupuestos altos, medios y bajos para ambas ciudades para que elija el que más le satisfaga.

***Próximos pasos:***

En un futuro, se puedan implementar mejoras tanto a nivel de tratamiento y limpieza de datos como en la elaboración de gráficos más representativos y análisis más exahustivos. (Incluyendo machine learning, inteligencia artificial o más opciones). De hecho, los nulos no se imputaron ni eliminaron ya que imputarlos causaba un desbordamiento y eliminarlos sería un error puesto que corresponden al 30%. Finalmente se usaron gráficos sns que ignoran los nulos.
