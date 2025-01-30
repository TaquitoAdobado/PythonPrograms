'''La diferencia entre una ruta relativa y absoluta es que en la ruta relativa se basa en el directorio actual, no se
especifica la ruta completa, en cambio, en la ruta absoluta se especifica la ruta completa'''
from pathlib import Path

#En el siguiente ejemplo se muestra como se crea una ruta relativa.
ruta_relativa = Path("carpeta1", "carpeta2", "archivo.txt")
print(ruta_relativa)

#En el siguiente ejemplo se muestra como se crea una ruta absoluta. La cual incluye la ruta completa.
base = Path.home()
ruta_absoluta = Path(base, ruta_relativa)
print(ruta_absoluta)