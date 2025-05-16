import librosa
import librosa.display
from collections import Counter


nombre_archivo = "ad05.mp3"
# Cargar el archivo de audio
archivo_audio = "audios/"+nombre_archivo
y, sr = librosa.load(archivo_audio)

# Extraer el tono fundamental (pitch) con librosa.yin
pitches = librosa.yin(y, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'), sr=sr)

# Convertir las frecuencias a nombres de notas (ej. C4, D#4, etc.)
notas_completas = [librosa.hz_to_note(freq) for freq in pitches]

# Reducir a notas básicas (Do, Re, etc.) eliminando sostenidos y octava
notas_basicas = []
conversion = {'C': 'Do', 'D': 'Re', 'E': 'Mi', 'F': 'Fa', 'G': 'Sol', 'A': 'La', 'B': 'Si'}
for nota in notas_completas:
    if nota:  # Evita errores si la nota es None
        nombre = nota[0]  # Tomar solo la letra (C, D, etc.)
        if nombre in conversion:
            notas_basicas.append(conversion[nombre])

# Contar cuántas veces aparece cada nota básica
conteo = Counter(notas_basicas)

# Mostrar el resultado
for nota, cantidad in conteo.items():
    print(f"{nota}: {cantidad} veces")