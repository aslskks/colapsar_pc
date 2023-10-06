import shutil
nu = 0

while nu == 0:
    archivo = f"copynotopen.py"
    archivo_c = f"copynotopen{nu}.py"
    shutil.copy2(archivo, f"F:\programas\leer codigos\{archivo_c}")
    nu += 1
