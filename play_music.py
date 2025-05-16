import os
import pathlib
import librosa
import librosa.display
import matplotlib.pyplot as plt
import pygame
import sys



# Contar archivos en el directorio
inputdit = "audios"
intial_count = sum(1 for path in pathlib.Path(inputdit).iterdir() if path.is_file())

print(f"Aquí hay {intial_count} archivos de audio\n")

archivos = os.listdir(inputdit)
print(archivos)

# Pedir al usuario qué canción reproducir
song = input("\nIngrese la canción que quiere reproducir: ")
file = os.path.join(inputdit, song)

if not os.path.exists(file):
    print("Archivo no encontrado.")
    sys.exit()

# Inicializar pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)

while True:
    n = input("Escriba 'play' para reproducir, 'stop' para pausar o 'exit' para salir:\n").strip().lower()
    
    if n == "play":
        pygame.mixer.music.play()
    elif n == "stop":
        pygame.mixer.music.pause()
    elif n == "exit":
        pygame.mixer.music.stop()
        pygame.quit()
        sys.exit()
    else:
        print("Comando no válido. Intente de nuevo.")