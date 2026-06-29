# 🎮 Juego Del Ahorcado

> **Proyecto Integrador Fundamentos de Programación**
> 
> **Estudiante:** Jonathan Quezada Miguez  
> **Fecha:** Junio 2026

---   

## 📌 Objetivo del sistema

Desarrollar un juego interactivo de "El Ahorcado" en Python que permita al usuario adivinar palabras relacionadas con la programación, aplicando los conceptos fundamentales aprendidos durante el curso: estructuras condicionales, bucles, listas y entrada/salida de datos.

---

## 📋 Descripción del proyecto

El programa selecciona aleatoriamente una palabra del mundo de la informática y le proporciona al jugador una pista para adivinarla letra por letra. El jugador tiene un máximo de **6 intentos** antes de que el ahorcado quede completo. Al final de cada partida, el usuario puede optar por jugar nuevamente.

---

## ⚙️ Funcionalidades principales

| Funcionalidad | Descripción |
|---|---|
| Selección aleatoria de palabra | El sistema elige una palabra de un listado predefinido usando `random.randint` |
| Sistema de pistas | Cada palabra tiene una pista descriptiva que se muestra al inicio |
| Visualización del ahorcado | Se dibuja el ahorcado en consola progresivamente según los errores |
| Control de letras | Detecta letras repetidas y letras ya usadas |
| Contador de intentos | Muestra los intentos restantes en cada turno |
| Jugar de nuevo | Al terminar, el jugador puede iniciar una nueva partida |

---

## 🗂️ Estructura del repositorio

```
juego-del-ahorcado/
│
├── ahorcado.py                  # Código fuente principal del juego
├── diagrama de flujo.png        # Diagrama de flujo del programa
├── diagrama de arquitectura.png # Diagrama de arquitectura del sistema
└── README.md                    # Este archivo
```

---

## 🐍 Tecnologías utilizadas

- **Lenguaje:** Python 
- **Control de versiones:** Git + GitHub

---

## ▶️ ¿Cómo ejecutar el programa?

1. Asegúrate de tener Python 3 instalado en tu computadora.
2. Clona este repositorio:
   ```bash
   git clone https://github.com/Jonathan09jpg/juego-del-ahorcado.git
   ```
3. Entra a la carpeta del proyecto:
   ```bash
   cd juego-del-ahorcado
   ```
4. Ejecuta el programa:
   ```bash
   python ahorcado.py
   ```

---

## 🧠 Contenidos de la asignatura aplicados

- **Unidad 1:** Introducción a la Resolución de Problemas y al Entorno de Programación
- **Unidad 2:** Entorno de Programación
- **Unidad 3:** Lógica de Programación
- **Unidad 4:** Estructura de Datos y Funciones

---

## 🌍 Impacto tecnológico

Este proyecto demuestra cómo la programación puede aplicarse al entretenimiento educativo. Un juego como El Ahorcado puede usarse en aulas para reforzar vocabulario técnico de manera interactiva, mostrando el impacto positivo de la tecnología en la educación.

