import matplotlib.pyplot as plt
import librosa
import numpy as np

# Cargar audio
y, sr = librosa.load("audios/ad05.mp3")

# Detectar pitch
pitches = librosa.yin(y, fmin=librosa.note_to_hz('C2'),
                      fmax=librosa.note_to_hz('C7'), sr=sr)
times = librosa.frames_to_time(np.arange(len(pitches)), sr=sr)

# Convertir a notas MIDI
midi_notes = [librosa.hz_to_midi(p) if not np.isnan(p) else None for p in pitches]

# Crear gráfica tipo piano roll
plt.figure(figsize=(14, 5))
for i, note in enumerate(midi_notes):
    if note:
        plt.scatter(times[i], note, color='purple', s=10)

plt.xlabel("Tiempo (s)")
plt.ylabel("Nota MIDI")
plt.title("Piano Roll simplificado (notas detectadas)")
plt.grid(True)
plt.tight_layout()
plt.savefig("mi_grafica_piano_roll.png", dpi=300)
plt.show()
