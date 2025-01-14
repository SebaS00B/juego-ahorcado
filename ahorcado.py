import random

palabra_secreta = ["python", "django", "tecnologia", "curso"]
palabra_elegida = random.choice(palabra_secreta)
palabra_elegida = palabra_elegida.lower()
longitud_palabra = len(palabra_elegida)
letras = ["_"] * longitud_palabra

def ahorcado():
    intentos = 6
    while intentos > 0 and "_" in letras:
        print(" ".join(letras))
        print(f"Intentos restantes: {intentos}")
        letra = input("Ingrese una letra: ").lower()

        if len(letra) != 1:
            print("Ingrese solo una letra")
            continue
        
        if letra in palabra_elegida:
            for i in range(longitud_palabra):
                if palabra_elegida[i] == letra:
                    letras[i] = letra
        else:
            print("La letra no existe en la palabra secreta")
            intentos -= 1

    if "_" not in letras:
        print(" ".join(letras))
        print("¡Felicidades, adivinaste la palabra secreta!")
    else:
        print(" ".join(letras))
        print("Lo siento, no adivinaste la palabra secreta")

ahorcado()



