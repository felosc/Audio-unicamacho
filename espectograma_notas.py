import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Cargar el audio
archivo_audio = "audios/ad05.mp3"
y, sr = librosa.load(archivo_audio)

# Calcular el espectrograma
S = librosa.stft(y)
S_db = librosa.amplitude_to_db(abs(S))

# Extraer pitch
pitches = librosa.yin(y, fmin=librosa.note_to_hz('C2'),
                      fmax=librosa.note_to_hz('C7'), sr=sr)
times = librosa.frames_to_time(np.arange(len(pitches)), sr=sr)
notas = [librosa.hz_to_note(p) if not np.isnan(p) else None for p in pitches]

# Graficar espectrograma
plt.figure(figsize=(14, 6))
librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='log')
plt.colorbar(format="%+2.0f dB")
plt.title("Espectrograma con notas musicales")

# Superponer algunas notas (cada medio segundo, por claridad)
for i in range(0, len(times), int(sr / 512)):
    if notas[i] is not None:
        plt.text(times[i], pitches[i], notas[i], fontsize=7, color='white', rotation=45)

plt.tight_layout()
plt.savefig("mi_grafica_Espectrograma.png", dpi=300)
plt.show()
