import os
import pathlib
import librosa
import librosa.display
import matplotlib.pyplot as plt
import pygame
import sys

nombre_archivo = "ad03.mp3"
# Cargar el archivo de audio
archivo_audio = "audios/"+nombre_archivo
y, sr = librosa.load(archivo_audio)
print(archivo_audio)

# Graficar la forma de onda
plt.figure(figsize=(10, 4))
librosa.display.waveshow(y, sr=sr, alpha=0.7)
plt.title("Forma de onda del audio")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")

# Guardar la imagen
plt.savefig("onda_sonora"+nombre_archivo+".png")
plt.close()  # Cierra la figura para liberar memoria

print("Gráfico guardado como 'onda_sonora"+nombre_archivo+".png'")

tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
print(f"Tempo estimado: {tempo} BPM")


beat_times = librosa.frames_to_time(beats, sr=sr)
beat_times  # Guardar audio con beats

print(archivo_audio)
# Cargar el archivo de audio
y, sr = librosa.load(archivo_audio, sr=None)

# Extraer frecuencia fundamental (f0) con `pyin`
f0, voiced_flag, voiced_probs = librosa.pyin(y, fmin=librosa.note_to_hz('C2'), 
                                             fmax=librosa.note_to_hz('C7'))

# Convertir frecuencia a notas musicales
notas = librosa.hz_to_note(f0)

# Mostrar las primeras 20 notas detectadas
print("Notas detectadas:", notas[:20])

# Graficar la frecuencia fundamental
plt.figure(figsize=(10, 4))
times = librosa.times_like(f0, sr=sr)
plt.plot(times, f0, label="Frecuencia fundamental (Hz)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Frecuencia (Hz)")
plt.title("Detección de notas musicales")
plt.legend()
plt.show()






