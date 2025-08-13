participantes ={}

print("Menu principal")

def quic_sorter(lista):
    if len(lista) <=1:
        return lista

    pivot = lista[0]
    mayor =[x for x in lista[1:] if x[1]["edad"] >= pivot[1]["edad"]]
    menor =[x for x in lista[1:] if x[1]["edad"] < pivot[1]["edad"]]

    return quic_sorter(mayor) + [pivot] + quic_sorter(menor)

def quick_sorterN(lista):
    if len(lista) <=1:
        return lista
    pivot = lista[0]
    menor=[x for x in lista[1:] if x[1]["nombre"] <= pivot[1]["nombre"]]
    mayor=[x for x in lista[1:] if x[1]["nombre"] > pivot[1]["nombre"]]
    return quic_sorter(menor) + [pivot] + quic_sorter(mayor)

seleccion = ""
while seleccion != 0:
    print("\n1.Agregar participante")
    print("2.Mostrar particiapantes por edad")
    print("3.Mostarr particiapantes por nombre")
    print("0.salir")

    try:
        seleccion = int(input())

    except ValueError:
        print("\nIngrese numero valido" )
        continue


    match seleccion:
        case 1:
            salir = input("¿Desea volver al menú principal? (S/N): ").strip().upper()
            if salir == "S":
                continue

            while True:
                try:
                   cantidad=int(input("\nIngrese la cantidad de participantes: "))
                   break
                except ValueError:
                    print("\nIngrese numero valido")

            for i in range(cantidad):
                print(f"\nIngrese los datos de participante {i+1}:")

                while True:
                    try:
                        dorsal=int(input("ingrese NO. dorsal: "))
                        if dorsal in participantes:
                            print("No ya registrado")
                            continue
                        break
                    except ValueError:
                        print("\nIngrese numero valido")


                while True:
                        nombre=input("Ingrese nombre: ")
                        if nombre:
                            break
                        else:
                            print("\nIngrese nombre invalido")

                while True:
                    try:
                        edad = int(input("Ingrese edad: "))
                        if edad > 0:
                            break
                        else:
                            print("\nIngrese edad invalido")
                    except ValueError:
                        print("\nIngrese edad invalido")

                while True:
                    categoria=input("Ingrese categoria:  (M=master, A=adulto, J=juvenil)")
                    if categoria in ["M", "A", "J"]:
                        break
                    else:
                        print("\nDeber ingresar M o A o J")

            print("Participante ingresado correctamente")





        case 2:
            salir = input(" volver a l menu principal:  (S/N)").strip().upper()
            if salir == "S":
                continue

            print("Participantes ordenados por nombre")
            lista_participantes = list(participantes.items())
            participantes_ordenados = quic_sorter(lista_participantes)

            for dorsal,info in participantes_ordenados:
                print(f"Dorsal: {dorsal}, Nombre: {info['nombre']}, Edad: {info['edad']}, Categoris: {info['categoria']}")




        case 3:
            salir = input(" volver a l menu principal:  (S/N)").strip().upper()
            if salir == "S":
                continue

            print("Participantes ordenados por edad")
            lista_participantes=list(participantes.items())
            participantes_ordenados = quic_sorter(lista_participantes)
            for dorsal,info in participantes_ordenados:
                print(f"dorsal: {dorsal}, Nombre: {info['nombre']} , Edad: {info['edad']}, Categoris: {info['categoria']}")

        case 0:
            print("saliendo")