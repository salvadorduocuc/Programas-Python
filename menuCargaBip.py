#CargaTarjetaBip
sw = 1
saldo = 0
while sw==1:
    print("1. Ver mi Saldo")
    print("2. Cargar Saldo")
    print("3. Salir")
    op=int(input("Seleccione una opción: "))
    try:
        if(op > 0 and op < 4):
            if op == 1:
                print(f"Tiene un saldo de {saldo}")
                continu = int(input("presione 1) para volver atrás, presione 2) para salir "))
                if continu==2:
                    print("Cierre de sesión exitoso, adiós")
                    sw=0
            if op == 2:
                print("¿Cuánto desea cargar?")
                print("1.-  $1.000")
                print("2.-  $5.000")
                print("3.- $20.000")
                continu = int(input("Seleccione la opción"))
                if continu==1:
                    saldo = saldo+1000
                    print(f"Carga exitosa, su saldo es de: ${saldo}")
                if continu==2:
                    saldo = saldo+5000
                    print(f"Carga exitosa, su saldo es de: ${saldo}")
                if continu==3:
                    saldo = saldo+20000
                    print(f"Carga exitosa, su saldo es de: ${saldo}")
            if op == 3:
                print("Muchas gracias por ocupar el servicio, adiós")
                sw=0
        else: 
            print("Selección fuera de rango")
    except:
        print("Ingreso Erróneo")