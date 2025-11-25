# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
dist = 0
cof = 1.3
i = 0

def init(vals):
    global items, n, dist, cof, i, final
    items = list(vals)
    n = len(items)
    dist = n
    i = 0

def step():
    global items, n, dist, cof, i, final

   # para detener el bucle
    if i >= n - 1:
        return {"done": True}
    a = j
    b = j + 1
    swap = False

    if i + dist >= n:
        dist = int(dist / cof)     # Reducimos distancia (dist)
        if dist < 1: # prueba para detectar si está ordenado
            dist = 1
        i = 0
        return {"a": None, "b": None, "swap": False, "done": False}

    a = i
    b = i + dist
    swap = False

    if items[a] > items[b]:
        items[a], items[b] = items[b], items[a]
        swap = True

    i += 1
    return {"a": a, "b": b, "swap": swap, "done": False}

"""
En pseudocodigo:
Tengo una lista [5,6,4,2,1]
La lista no se repite
un número es mayor que otro.

Es similar al bubble, solo que utiliza un número (coeficiente) que se multiplica con el largo de la fila para definir la disttancia (disttancia) y posición con la que se compara.
Ese coeficiente (según lo visto) es 1.3
Al repetirse, el selector se vuelve a multiplicar por el coeficiente.

"""
