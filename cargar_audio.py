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

