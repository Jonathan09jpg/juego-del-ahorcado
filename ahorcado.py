import random

palabras = ["python", "bucle", "software", "variable", "codigo",
    "programador", "hardware", "algoritmo", "funcion"]

pistas = {"python": "Lenguaje de programacion muy popular y facil de aprender",
    "bucle": "Estructura que repite instrucciones varias veces",
    "software": "Conjunto de programas que le dicen a la computadora que hacer",
    "variable": "Espacio en memoria que guarda un valor",
    "codigo": "Instrucciones escritas en un lenguaje de programacion",
    "programador": "Persona que escribe codigo para crear programas",
    "hardware": "Partes fisicas de una computadora",
    "algoritmo": "Serie de pasos ordenados para resolver un problema",
    "funcion": "Bloque de codigo que realiza una tarea especifica"}

jugar_de_nuevo = "s"

while jugar_de_nuevo == "s":

    indice = random.randint(0, len(palabras) - 1)
    palabra = palabras[indice]
    pista = pistas[palabra]
    letras_adivinadas = []
    letras_incorrectas = []
    errores = 0
    max_errores = 6

    print("   EL AHORCADO")
    print("Pista:", pista)
    print("La palabra tiene", len(palabra), "letras")

    ganaste = False

    while errores < max_errores and not ganaste:

        if errores == 0:
            print("""
           -----
           |   |
               |
               |
               |
               |
        ==========""")
        elif errores == 1:
            print("""
           -----
           |   |
           O   |
               |
               |
               |
        ==========""")
        elif errores == 2:
            print("""
           -----
           |   |
           O   |
           |   |
               |
               |
        ==========""")
        elif errores == 3:
            print("""
           -----
           |   |
           O   |
          /|   |
               |
               |
        ==========""")
        elif errores == 4:
            print("""
           -----
           |   |
           O   |
          /|\  |
               |
               |
        ==========""")
        elif errores == 5:
            print("""
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        ==========""")

        palabra_mostrada = ""
        for letra in palabra:
            if letra in letras_adivinadas:
                palabra_mostrada += letra + " "
            else:
                palabra_mostrada += "_ "

        print("\nPalabra:", palabra_mostrada)
        print("Letras incorrectas:", letras_incorrectas)
        print("Intentos restantes:", max_errores - errores)

        if "_" not in palabra_mostrada:
            ganaste = True
            print("\n¡¡¡GANASTE!!!")
            print("La palabra era:", palabra)
            break

        letra = input("\nIngresa una letra: ").lower()

        if len(letra) != 1:
            print("Por favor ingresa solo una letra.")
            continue

        if letra in letras_adivinadas or letra in letras_incorrectas:
            print("Ya ingresaste esa letra, intenta con otra.")
            continue

        if letra in palabra:
            letras_adivinadas.append(letra)
            print("¡Bien! La letra", letra, "esta en la palabra.")
        else:
            letras_incorrectas.append(letra)
            errores += 1
            print("Incorrecto. La letra", letra, "no esta en la palabra.")

    if not ganaste:
        print("""
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        ==========""")
        print("\n¡PERDISTE! La palabra era:", palabra)

    jugar_de_nuevo = input("\n¿Quieres jugar de nuevo? (s/n): ").lower()

print("\n¡Hasta luego!")