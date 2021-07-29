import os

#Creacion de todos los directorios para el sistema de archivos

def initialize_filesystem():
    try:
        if not os.path.isdir('root'):  
            os.system("mkdir root")
        os.chdir('root')
        if not os.path.isdir('binarios'):
            os.system("mkdir binarios")
        if not os.path.isdir('temporal'):
            os.system("mkdir temporal")
        if not os.path.isdir('arranque'):
            os.system("mkdir arranque")
        if not os.path.isdir('librerias'):
            os.system("mkdir librerias")
        if not os.path.isdir('usuario'):
            os.system("mkdir usuario")
        os.chdir('usuario')
    except Exception as e: 
        pass