import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Cargar el archivo de audio
archivo_audio = "audios/ad05.mp3"
y, sr = librosa.load(archivo_audio)

# Extraer el pitch usando el algoritmo YIN
pitches = librosa.yin(y, fmin=librosa.note_to_hz('C2'),
                      fmax=librosa.note_to_hz('C7'), sr=sr)

# Calcular los tiempos correspondientes a cada estimación de pitch
frames = range(len(pitches))
times = librosa.frames_to_time(frames, sr=sr)

# Convertir pitches a nombres de notas (ej: C4, D#4, etc.)
notas = [librosa.hz_to_note(p) if not np.isnan(p) else None for p in pitches]

# Crear la gráfica
plt.figure(figsize=(14, 6))
plt.plot(times, pitches, label="Pitch (Hz)", color='blue')
plt.xlabel("Tiempo (s)")
plt.ylabel("Frecuencia (Hz)")
plt.title("Pitch detectado con notas musicales")

# Superponer nombres de notas en puntos clave (cada medio segundo, por ejemplo)
for i in range(0, len(times), int(sr / 2)):
    if i < len(notas) and notas[i] is not None:
        plt.text(times[i], pitches[i], notas[i], fontsize=8, color='red', rotation=45)

plt.grid()
plt.tight_layout()
plt.savefig("mi_grafica_curva.png", dpi=300)
plt.show()
