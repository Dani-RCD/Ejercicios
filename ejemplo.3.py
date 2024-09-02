try:
    x = int(input("Introducen un numero:"))
    y =10/x
except ValueError:
    
    print("Debes intruducir u numero valido.")
else:
    print(f"El numero es ´{x}")