import sys
import os

# Obtener la ruta absoluta del directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Agregar la ruta al directorio src a la ruta de búsqueda de módulos
sys.path.append(os.path.join(current_dir, 'src'))

#from get_data import info

if __name__ == "__main__":
    print("Llamando a la función de get_data.py...")
    #info()
    print("Proceso finalizado.")