try:
    x = int(input("introducen un numero:"))
    y =10/x
except ValueError:
    
    print("deve intruducir u numero valido.")
except ZeroDivisionError:
    print("NO SE PUEDE DIVIDIR ENTRE CERO ")