# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0
j = 0

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 0
    j = 0

def step():
    global items, n, i, j

    if i >= n - 1:
        return {"done": True}
    a = j
    b = j + 1
    swap = False

    if items[a] > items[b]:
        items[a], items[b] = items[b], items[a]
        swap = True

    j += 1
    if j >= n - i - 1:
        j = 0
        i += 1
    return {"a": a, "b": b, "swap": swap, "done": False}

"""
En pseudocodigo:
Tengo una lista [5,6,4,2,1]
La lista no se repite
un número es mayor que otro.

Tengo que lograr comparar dos números y si el de la derecha es menor, ubicarlo en la posición del número que comparo inicialmente.
Es decir, para (for) una lista de números (in range lista) Si el primer número es mayor comparado con el siguiente número de la lista  (posición > posición +1) entonces cambiar de posición
Entonces buscamos el mayor número de la lista (menos uno porque no hay uno mayor) y dentro de esa búsqueda comparar si son mayores.

"""


