# Laberinto del Gato y el Ratón - Minimax

### Qué creé:
Hice un simulador donde un gato y un ratón se persiguen en un tablero con obstáculos. El ratón intenta llegar a la salida y el gato quiere atraparlo. Todo funciona con el algoritmo **Minimax** (el ratón maximiza y el gato minimiza).

### Qué funcionó bien:
- El tablero se genera bien con obstáculos aleatorios y emojis para mejorar la estetica de la consola.
- Los movimientos en 8 direcciones funcionan perfecto.
- El Minimax corre sin romperse.
- El tablero tambien puede ser generado aleatoriamente.
- Al final logré equilibrar el juego (el gato y el ratón ganan más o menos la misma cantidad de veces).

### Qué fue un desastre / me costó:
- Al principio el Minimax estaba totalmente roto porque modificaba el mismo tablero en todas las simulaciones (todo se pisaba).
- El gato ganaba casi siempre (era demasiado fuerte).
- Les costaba a ambos dejar de "bailar" en la persecucion.
- En tableros grandes se ponía re lento.
- Me peleé mucho con las evaluaciones del gato y el ratón.

### Mi mejor "¡Ajá!" del proceso:
- Fueron un par de momentos:
- Entender que si queria que se moviera tambien en diagonal, no debia usar la distancia Manhattan, sino la distancia Chebyshev.
- Entender que **no hace falta mucha profundidad**, sino que **la función de evaluación es más importante**. Cuando ajusté los números de las puntuaciones, el comportamiento del ratón y del gato mejoró muchísimo de un momento a otro.
