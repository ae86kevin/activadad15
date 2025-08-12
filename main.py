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
            while True:
                try:
                   cantidad=int(input("\nIngrese la cantidad de participantes: "))
                   break
            for i in range(cantidad):
                print(f"\nIngrese los datos de participante {i+1}:")
                dorsal=int(input("ingrese NO. dorsal: "))
                participantes[dorsal]={}
                participantes[dorsal]["nombre Y apellido"]=input("Ingres el nombre: ")
                participantes[dorsal]["edad (utilize solo numeros)"]=int(input("Ingrese la edad: "))
                participantes[dorsal]["Tipo de categoria: (M=master, A=adulto = J=Juvenil)"]=input("Ingrese la categoria: ")


            print("Participante registrada exitosamente")



        case 2:
            print("Participantes ordenados por nombre")
            lista_participantes = list(participantes.items())
            participantes_ordenados = quic_sorter(lista_participantes)

            for dorsal,info in participantes_ordenados:
                print(f"Dorsal: {dorsal}, Nombre: {info['nombre']}, Edad: {info['edad']}, Categoris: {info['categoria']}")




        case 3:
            print("Participantes ordenados por edad")
            lista_participantes=list(participantes.items())
            participantes_ordenados = quic_sorter(lista_participantes)
            for dorsal,info in participantes_ordenados:
                print(f"dorsal: {dorsal}, Nombre: {info['nombre']} , Edad: {info['edad']}, Categoris: {info['categoria']}")

        case 0:
            print("saliendo")