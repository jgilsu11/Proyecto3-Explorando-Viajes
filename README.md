

![Mallorca vs Tenerife](imagenes/A_comparison_of_Palma_de_Mallorca_and_Santa_Cruz_d.png)


**Elección de mejor destino para vacaciones en solitario**


***Descripción:***
El proyecto 3 consiste en la extracción, exploración, limpieza, y análisis de los datos de vuelos, alojamientos y actividades haciendo uso de archivos.py y Jupyter notebook.

Las técnicas usadas durante el proyecto son en su mayoría aquellas enseñadas durante la tercera semana de formación (Uso de APIs, web scrapping,creación de gráfica y formateos entre otros).

Adicionalmente, se usaron recursos obtenidos mediante research en documentación especializada, vídeos de YouTube e IA como motor de búsqueda y apoyo al aprendizaje.


***Estructura del Proyecto:***

El desarrollo del proyecto se gestionó de la siguiente manera:

- _En Primer lugar_, haciendo uso de JupyterNotebook como primer paso donde realizar ensayos con el código.  
 Estos jupyter se dividen en extracción y limpieza, exploración y visualización.

-_En Segundo Lugar_, se creo una presentación basada en los datos.

-_Finalmente_, se realizó la documentación del proyecto en un archivo README (documento actual).

Por todo lo anterior, el usuario tiene acceso a:

        ├── notebooks/           # Notebooks de Jupyter 
        ├── src/                 # Scripts (.py)
        ├── README.md            # Descripción del proyecto
        ├── Presentación         # Presentcaión del proyecto
***Requisitos e Instalación🛠️:***

Este proyecto usa Python 3.11.9 y bibliotecas como numpy, pandas, datetime, matplotlib.pyplot, seaborn, selenium, beutifulsoup y re  que se necesitarán importar al principio del código.


***Aportación al Usuario🤝:***

El doble fin de este proyecto incluye tanto el aprendizaje y formación por parte del desarrollador como la intención de servir de recomendación y orientación a un viajero solitario.

***Próximos pasos:***

Quizá en un futuro cuando como desarrollador se posea mayor conocimiento, se puedan implementar mejoras tanto a nivel de tratamiento y limpieza de datos como en la elaboración de gráficos más representativos y análisis más exahustivos. (Incluyendo machine learning, inteligencia artificial o más opciones). De hecho, los nulos no se imputaron ni eliminaron ya que imputarlos causaba un desbordamiento y eliminarlos sería un error. Por ello se usaron gráficos sns que ignoran los nulos

Además dado que en el análisis se eliminaron los nulos, en el futuro podría ser interesante analizar de manera independiente las filas que contengan nulos (independiente para que no distorsione el otro análisis) y de esta manera se conocería la infomación que aportarían esas filas que fueron borradas en el análisis actual.
