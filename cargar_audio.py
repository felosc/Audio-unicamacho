import pathlib
import os 
import pygame

inputdit = 'audios'

intial_count = 0

for path in pathlib.Path(inputdit).iterdir():
    if path.is_file():intial_count += 1

print('aqui hay ',intial_count,' archivos de uadios\n')

list = os.listdir(inputdit)
print(list)

song = input('\n ingrese la cancion que quiere reproducir: ')
file = os.path.join(inputdit, song)

pygame.init()
pygame.mixer.music.load(file)

while True:
    n = input("escriba Play or Stop reproducir o detener la cancion. \nescriba Exit para detener el programa:\n")
    if n == "play":
        pygame.mixer.music.play()
    elif n ==  "stop":
        pygame.mixer.music.pause()
    elif n == "exit":
        exit()

#esto fue sacado de caht gpt ---> es codigo para graficar las ondas del archivo mp3
import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment

# Cargar el archivo MP3
file_path = "audios/Gary B.B. Coleman - The Sky is Crying.mp3"  # Reemplaza con la ruta de tu archivo MP3
audio = AudioSegment.from_mp3(file_path)

# Convertir a mono (si es estéreo)
if audio.channels == 2:
    audio = audio.set_channels(1)

# Obtener los datos de audio en formato de muestra (en bytes)
samples = np.array(audio.get_array_of_samples())

# Crear un eje temporal para la gráfica
time = np.linspace(0, len(samples) / audio.frame_rate, num=len(samples))

# Graficar la onda
plt.figure(figsize=(10, 6))
plt.plot(time, samples)
plt.title(f'Onda de audio de {file_path}')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.show()