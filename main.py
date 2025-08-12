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
    print("2.MOstrar particiapantes por edad")
    print("3.mostarr particiapantes por nombre")
    print("0. salir")
    seleccion = int(input())

    match seleccion:
        case 1:
            cantidad=int(input("\nIngrese la cantidad de participantes: "))
            for i in range(cantidad):
                print(f"\nIngrese los datos de participante {i+1}:")
                dorsal=int(input("ingrese NO. dorsal: "))
                participantes[dorsal]={}
                participantes[dorsal]["nombre"]=input("Ingres el nombre: ")
                participantes[dorsal]["edad"]=int(input("Ingrese la edad: "))
                participantes[dorsal]["categoria"]=input("Ingrese la categoria: ")


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