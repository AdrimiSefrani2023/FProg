import time
print("Bienvenido a Adrimi-Sefrani gamer")
nombre = input("¿Cómo te llamas? ")
print("Hola, " + nombre + ". Es hora de jugar al ahorcado por 1/4 de pollo")
print(" ")
time.sleep(1)

print("Comienza a adivinar")
time.sleep(0.5)

palabra = 'Sandia'
tupalabra = ''
vidas = 5

while vidas > 0:
    fallas = 0

    for letra in palabra:
        if letra.lower() in tupalabra.lower():
            print(letra, end="")
        else:
            print("*", end="")
            fallas += 1

    print("")  

    if fallas == 0:
        print("¡Felicidades " +nombre+ ", ganaste tu 1/4 de pollo!")
        break

    tuletra = input("Introduce una letra: ")
    tupalabra += tuletra

    if tuletra.lower() not in palabra.lower():
        vidas -= 1
        print("Equivocación")
        print("Tienes", vidas, "vidas restantes")

    if vidas == 0:
        print("¡Perdiste tu 1/4 de pollo! para la proxima será. La palabra correcta era:", palabra)
        break

print("Gracias por participar")