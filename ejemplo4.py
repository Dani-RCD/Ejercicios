try:
    archivito=open(C:\Users\danie\OneDrive\Escritorio\Paradigmas)
    data=archivito.read()
    print(data)
except IOError:
    print("Error al leer el archivo")
finally:
    archivito.close()
    
