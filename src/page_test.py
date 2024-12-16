import tkinter as tk
from tkinter import filedialog, ttk, PhotoImage
import get_info_files as gt
from get_info_files import Getinfo

archivos = []
# Función para seleccionar un archivo y actualizar la etiqueta con el nombre del archivo
def seleccionar_archivo(label, i): 
    
    archivo = filedialog.askopenfilename(title="Seleccionar Archivo")
    archivos.insert(i , archivo)
    nombre_archivo = archivo.split("/")[-1]  # Extraer solo el nombre del archivo
         
    label.config(text=nombre_archivo, foreground="green")
    return archivos


# Crear la ventana principal
root = tk.Tk()

root.title("Master PCT Tracker Generator")
root.iconbitmap("./visuals/icon.ico")  # Asegúrate de que el archivo exista
root.geometry("700x500")  # Tamaño ajustado
root.resizable(False, False)

# Crear el encabezado con un Frame
header_frame = tk.Frame(root, bg="#0052a6", height=80)
header_frame.pack(fill="x")

# Cargar la imagen
try:
    imagen = PhotoImage(file="./visuals/icon.png")
    imagen = imagen.subsample(8, 8)  # Redimensionar la imagen
except Exception as e:
    print(f"Error al cargar la imagen: {e}")
    imagen = None

# Agregar la imagen al encabezado
if imagen:
    img_label = tk.Label(header_frame, image=imagen, bg="#0052a6")
    img_label.pack(side="left", padx=10, pady=10)

# Agregar el título centrado
header_label = tk.Label(header_frame, text="BIENVENIDOS", font=("Arial", 24, "bold"), bg="#0052a6", fg="white")
header_label.pack(side="left", expand=True)

# Texto de instrucciones
label_instrucciones = tk.Label(root, text="Agregue los archivos necesarios", font=("Arial", 12, "bold"), fg="#333")
label_instrucciones.pack(pady=15)

# Crear el marco principal para las entradas
frame_inputs = ttk.Frame(root, padding=20, relief="groove", borderwidth=2)
frame_inputs.pack(padx=20, pady=10, fill="x")

# Crear las etiquetas y botones en dos columnas
labels = []
for i in range(6):
    # Crear un sub-frame para cada fila (para mejor alineación)
    row_frame = tk.Frame(frame_inputs)
    row_frame.pack(fill="x", pady=5)

    # Etiqueta para mostrar el nombre del archivo
    label = tk.Label(row_frame, text="Archivo no seleccionado", font=("Arial", 10), width=30, anchor="w")
    label.pack(side="left", padx=10)
    labels.append(label)

    # Botón para cargar archivo
    btn_cargar = ttk.Button(row_frame, text="Cargar Archivo", command=lambda lbl=label: seleccionar_archivo(lbl, i))
    btn_cargar.pack(side="right", padx=10)

# Botón enviar
#btn_quitar = tk.Button(root, text="Remover archivos", font=("Arial", 12, "bold"),
#                       bg="gray",  # Color de fondo rojo
#                       fg="white",    # Color del texto blanco
#                       activebackground="black",  # Color de fondo cuando se presiona
#                       activeforeground="white",  # Color del texto al presionar
#                       relief="raised")  # Efecto de relieve
#btn_quitar.pack(pady=20)

def get_data_from_repository():
    # activeArchivos = seleccionar_archivo
    gt.Getinfo(archivos)

btn_enviar = tk.Button(root, text="Enviar", font=("Arial", 12, "bold"),
                       bg="#ff0000",  # Color de fondo rojo
                       fg="white",    # Color del texto blanco
                       activebackground="#cc0000",  # Color de fondo cuando se presiona
                       activeforeground="white",  # Color del texto al presionar
                       relief="raised",command=get_data_from_repository)  # Efecto de relieve
btn_enviar.pack(pady=20)





# Estilo para el botón enviar
# style = ttk.Style()
# style.configure("Custom.TButton", font=("Arial", 12, "bold"), background="#0052a6", foreground="white")

# Ejecutar la aplicación
root.mainloop()
