
print("Guía de primeros auxilios")
print("Responder sí o no a las preguntas")
verificacion1 = input("¿Responde a estímulos? ")

if verificacion1.lower()=="si" or verificacion1.lower()=="sí":
    print("Valorar la necesidad de llevarlo al hospital mas cercano")
    print("Fin de la guía de primeros auxilios")
else:
    print("Abrir vía Aérea")

    verificacion2 = input("¿Respira? ")

    if verificacion2.lower()=="si" or verificacion2.lower()=="sí":
        print("Permitirle posición de suficiente ventilación")
        print("Fin de la guía de primeros auxilios")
    else:
        print("Administrar 5 Ventilaciones y llamar a ambulancia")

        while True:
            respuesta = input("¿Hay signos vitales? ")
                    
            if respuesta.lower() == "si" or respuesta.lower() == "sí":
                print("Reevaluar a la espera de la Ambulancia")
            else:
                print("Administrar Compresiones Torácicas hasta que llegue ambulancia")

            respuesta2 = input("¿Llegó la ambulancia? ")
            if respuesta2.lower() == "no":
                continue
            else:
                print("Fin de la guía de primeros auxilios")
                break

