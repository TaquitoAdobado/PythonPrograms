import os

# os.chdir  (Change Directory)
''' Permite abir archivos que no estén en la ruta actual, cambiando el directorio.
En este caso estoy en la ruta siguiente:    '''
ruta = os.getcwd()
print('\n'+ruta) #C:\Users\danie\Documents\ProgramasPython\Manipulacion Archivos\Modulo OS

'''si quiero abrir un archivo que se encuentre en otra ruta, debo cambiar de directorio:    '''
ruta = os.chdir('C:\\Users\\danie\\Documents\\ProgramasPython\\Manipulacion Archivos\\Modulo OS\\Carpeta')
ruta = os.getcwd()
print('\n'+ruta)
archivo = open('archivo.txt')
print('\n'+ archivo.read())