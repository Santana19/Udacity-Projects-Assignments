import os

def renombrar_filas():
    lista_filas=os.listdir(r"C:\Users\Jayson\Downloads\prank\prank")
    print(lista_filas)
    ruta_original= os.getcwd()
    os.chdir(r"C:\Users\Jayson\Downloads\prank\prank")

    for nombre_filas in lista_filas:
        os.rename(nombre_filas, nombre_filas.translate(None,"0123456789"))
    os.chdir(ruta_original)
renombrar_filas()