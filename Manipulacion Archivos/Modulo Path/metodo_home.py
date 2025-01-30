#El metodo '.home()' nos devuelve la ruta de la carpeta principal del usuario

from pathlib import Path

base = Path.home()
print(base) #En mi caso: C:\Users\danie