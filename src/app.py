import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Cargar las variables del archivo .env
load_dotenv()

# Obtener las credenciales de Spotify desde el archivo .env
client_id = os.getenv('CLIENT_ID', 'd8a3cf848e7a48cd8168181bdbb93e8f')
client_secret = os.getenv('CLIENT_SECRET', 'bfbc45f666eb40bcb0e7b4ea0e8d90fa')

# Manejo seguro de Spotipy para evitar errores al finalizar el script
try:
    # Conexión con la API de Spotify utilizando Spotipy
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    
    # ID de artista de Taylor Swift
    artist = 'spotify:artist:06HL4z0CvFAxyc27GXpf02'
    
    # Obtener las canciones más populares del artista
    artist_tracks = sp.artist_top_tracks(artist)
    
    # Crear un DataFrame con la información relevante
    tracks = pd.DataFrame(artist_tracks['tracks'])
    tracks['duration_sec'] = tracks['duration_ms'] / 1000  # Convertir la duración de ms a segundos
    
    # Seleccionar y limpiar las columnas necesarias
    tracks = tracks[['name', 'popularity', 'duration_sec']]
    
    # Ordenar por popularidad en orden descendente
    tracks = tracks.sort_values('popularity', ascending=False)
    
    # Mostrar las 3 canciones más populares
    print("Top 3 canciones más populares de Taylor Swift:")
    print(tracks.head(3))
    
    # Graficar un scatter plot para analizar la relación entre duración y popularidad
    plt.figure(figsize=(12, 12))
    plt.title("Relación entre la duración y la popularidad de las canciones de Taylor Swift")
    plt.xlabel("Duración en segundos")
    plt.ylabel("Popularidad")
    sns.scatterplot(data=tracks, x='duration_sec', y='popularity', hue='name', legend='brief')
    plt.legend(loc='lower center')
    plt.show()

finally:
    # Cerrar explícitamente la instancia de Spotipy
    del sp

