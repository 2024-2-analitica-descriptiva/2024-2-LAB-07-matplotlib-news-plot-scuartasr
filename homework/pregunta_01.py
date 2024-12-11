"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
from matplotlib import pyplot as plt
import os

#%%

def lectura_datos(direccion: str) -> pd.DataFrame:
    """
    Lee los datos que se encuentran en una dirección dada.

    Args:
        direccion: Ruta donde se encuentran los datos
    
    Returns:
        Marco de datos de pandas con los datos leídos
    """

    df = pd.read_csv(
        direccion,
        index_col=0,
        header=0,
        encoding='utf-8'
    )

    return df

#%%

def crear_carpeta(carpeta: str) -> None:
    """
    Guarda un objeto determinado en una ruta especificada por el usuario
    """

    os.makedirs(carpeta, exist_ok=True)



#%%

def grafico(df: pd.DataFrame) -> None:
    """
    Grafica los datos de un marco de datos entregado. Esta opción simplemente
    da una primera aproximación al gráfico.

    Args:
        df: Marco de datos con los datos a graficar
    """
    
    # Diccionario con los colores que se usarán en cada caso:
    colores = {
        'Television': 'dimgray',
        'Newspaper': 'grey',
        'Internet': 'tab:blue',
        'Radio': 'lightgrey',
    }

    # Prioridad en la graficación
    prioridad = {
        'Television': 1,
        'Newspaper': 1,
        'Internet': 2,
        'Radio': 1,
    }

    # Grosor de cada línea
    grosor = {
        'Television': 2,
        'Newspaper': 2,
        'Internet': 3,
        'Radio': 2,
    }  

    plt.Figure()

    for columna in df.columns:
        plt.plot(
            df[columna], label=columna,
            color=colores[columna],
            zorder=prioridad[columna],
            linewidth=grosor[columna],
        )
    
    plt.title('How people get their news', fontsize=16)
    #plt.legend(loc = 'upper right')

    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().get_yaxis().set_visible(False)

    for columna in df.columns:
        # Valores de referencia para la primera observación de cada categoría
        first_year = df.index[0]
        plt.scatter(
            x=first_year,
            y=df[columna][first_year],
            color=colores[columna],
            zorder=prioridad[columna],
        )

        plt.text(
            first_year - 0.2,
            df[columna][first_year],
            columna + " " + str(df[columna][first_year]) + "%",
            ha='right',
            va='center',
            color=colores[columna],
        )

        last_year = df.index[-1]
        plt.scatter(
            x=last_year,
            y=df[columna][last_year],
            color=colores[columna],
            zorder=prioridad[columna],
        )

        plt.text(
            last_year + 0.2,
            df[columna][last_year],
            columna + " " + str(df[columna][last_year]) + "%",
            ha='left',
            va='center',
            color=colores[columna],
        )

    carpeta_guardado = './files/plots/'
    nombre_archivo = 'news.png'
    ruta = os.path.join(carpeta_guardado, nombre_archivo)

    crear_carpeta(carpeta_guardado)

    plt.tight_layout()
    plt.savefig(
        ruta
    )



    plt.close()


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """

    direccion = './files/input/news.csv'
    df = lectura_datos(direccion)

    grafico(df)

    # return df

if __name__ == '__main__':
    pregunta_01()