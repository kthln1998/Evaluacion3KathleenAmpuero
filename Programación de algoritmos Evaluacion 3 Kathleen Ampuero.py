# El/la autor de este sistema es: Kathleen Ampuero


print("Bienvenido a Auto seguro")
print("----------------------------")
print("1. Grabar")
print("2. Buscar")
print("3. Imprimir certificados")
print("4. Salir")
print("----------------------------")

sw = 0

op = int(input("Elija una opción: "))

def grabar(tipo, patente, marca, precio, monto,fechamult, fecharegis, nombredueño):
        print()

if op == 1:
        print("Usted desea guardar datos: ")    
        print("----------------------------")
        print("1. Tipo de vehiculo")
        print("2. Patente de vehiculo")
        print("3. Marca del vehiculo")
        print("4. Precio del vehiculo")
        print("5. Multa/s del vehiculo")
        print("6. Fecha del registro del vehiculo")
        print("7. Nombre del dueño del vehiculo")
        print("8. Salir")
        print("----------------------------")

        op = int(input("¿Qué datos desea guardar? "))

        if op == 1:        
                
                tipo = []
                guardartipovehi = input("¿Cuál es el tipo de vehiculo? ")
                patente = []
                marca = []
                precio = []
                monto = []
                fecharegis = []
                nombredueño = []

                tipo.append(guardartipovehi)          
                
                print("Se ha guardado el tipo de vehiculo: ", tipo)

        elif op == 2:

                 
            patente = []
            guardarpatente = int(input("¿Cuál es la patente? "))
            patente.append(guardarpatente)               
                    
            print("Se ha guardado la patente", patente)

        elif op == 3: 
            
            marca = []
            guardarmarca = input("¿Que marca es el vehiculo? ")
            marca.append(guardarmarca)

        elif op == 4: 
            
            precio = []
            guardarprecio = input("¿Que precio es el vehiculo? ")
            precio.append(guardarprecio)

        elif op == 6: 
            
            fecharegis = []
            guardarfecharegis = input("¿Cuál es la fecha de registro del vehiculo? ")
            fecharegis.append(guardarfecharegis)

        elif op == 5:

            print("Para la multa debera guardar monto y fecha.")

            monto = []
            guardarmonto = input("¿Cuál es el monto de la multa? ")
            monto.append(guardarmonto)

            fechamult = []
            guardarfechamulta = int(input("Cuál es la fecha de la multa? "))
            fechamult.append(guardarfechamulta)

            print("Multa: ", monto, "Fecha multa: ", fechamult )

        elif op == 7:

            nombredueño = []
            guardarnombredueño = input("¿Cuál es el nombre del dueño del vehiculo? ")
            nombredueño.append(guardarnombredueño)

            print("Nombre dueño: ", nombredueño)

        elif op == 8:
            sw = 1

elif op == 2:

        BSCAR = int(input("Para buscar un auto y su información \n Por favor Ingrese la patente: "))
        BSCAR.upper()

        if BSCAR == patente[]:
        
            print("Datos del auto: \n ", nombredueño, "\n" fecharegis ,"\n" patente, "\n" marca )

        else:
            print("Ingrese bien la patente por favor.")
            
elif op == 3:
    certificado = input("Desea imprimir certificado: 1. SI 2. NO")
    if certificado == 2:
        print("Usted no deseó imprimir certificado.")

    elif certificado == 1: 
        print("1. Certificado de Emisión de contaminantes $3.000 ")
        print("2. Certificado de Anotaciones vigentes $1.500 ")
        print("3. Certificado de Multas $3.500 ")
        print("4. Salir")

        if op == 1:
            print("Se ha emitido su certificado de Emisión de contaminantes.")
            print("-------------------------------------------------------------")
            print(nombredueño)
            print(patente)
            print(fecharegis)

        elif op == 2:
            print("Se ha emitido su certificado de Anotaciones vigentes.")
            print("-------------------------------------------------------------")
            print(nombredueño)
            print(patente)
            print(fecharegis)

        elif op == 3:
            print("Se ha emitido su certificado de Multas.")
            print("-------------------------------------------------------------")
            print(nombredueño)
            print(patente)
            print(fecharegis)

        elif op == 4:
            sw = 1

elif op == 4: 
    print(" Vuelva pronto! ")
    sw = 1

        






    







        


        

            
    

    







