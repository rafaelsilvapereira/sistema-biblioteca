import os
from utils.utils import C
os.system('color') # Ativa suporte no Windows

def mapa_de_cores():
    print("\n--- MAPA DE CORES ANSI ---")
    for i in range(0, 8):
        for j in range(30, 38):
            estilo = f"\033[{i};{j}m"
            reset = "\033[0m"
            print(f"{estilo} Cod: {i};{j} {reset}", end=' ')
        print()

mapa_de_cores()