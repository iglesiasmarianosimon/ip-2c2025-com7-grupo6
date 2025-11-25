# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
dist = 0
cof = 1.3
i = 0
j=0
huboswap=True

def init(vals):
    global items, n, dist, cof, i, j
    items = list(vals)
    n = len(items)
    dist = n
    i = 0

def step():
    global items, n, dist, cof, i, huboswap

    # para detener el bucle
    if i >= n - dist:

        # Si dist == 1 y NO hubo swaps es porque la lista ya está ordenada
        if dist == 1 and not huboswap:
            return {"a": None, "b": None, "swap": False, "done": True}
        
        dist = int(dist / cof)     # Reducimos distancia (dist)
        if dist < 1: # prueba para detectar si está ordenado
            dist = 1
        i = 0
        huboswap = False

        return {"a": None, "b": None, "swap": False, "done": False}
    
    a = i
    b = i + dist
    swap = False

    if items[a] > items[b]:
        items[a], items[b] = items[b], items[a]
        swap = True
        huboswap = True

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
