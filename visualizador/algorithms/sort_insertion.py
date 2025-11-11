# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0
j = None

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1
    j = None

def step():
    
    global items, n, i, j

    if i >= n:
        return {"done": True}
# Si por casualidad hay un solo número y descartar números menores a uno (si existiera)

    if j == None:
        j = i
        return {"a": j - 1 , "b": j, "swap": False, "done": False}
# Si el while no entra, pasamos al siguiente elemento

    while j > 0 and items[j - 1] > items[j]:
        items[j - 1], items[j] = items[j], items[j - 1]
        j -= 1
        return {"a": j, "b": j + 1, "swap": True, "done": False}
# Usamos un while para que los valroes se muevan a la izquierda. Terminado, reordenamos para repetir la operación
    i += 1
    j = None
    return {"a": None, "b": None, "swap": False, "done": False}

"""
Pseudocódigo:
El insertion funciona seleccionando un número y luego usándolo para ordenar todos los siguientes números
Ejemplo

Tengo una lista [2,7,4,1,3,5,6,8,9] y quiero que todos los números se ordenen a partir del número "7".

Es decir, pasaré por la lista y compararé cada número con el 7, y en base a ese número es que lo ordenaré.

Empiezo ¿2 es mayor que 7?No, entonces cambio la posición de 2 por el 7
Generaremos una lista nueva donde se contendrá el [2,7]
Ya elijo la subposición que tendrá el numero en la nueva lista.

Es decir, en este algoritmo insertion, voy  tener que ubicar el número en una lista y elegir su posición relativa respecto de mi número elegido.

Entonces, de esa lista, tengo que insertar ese número y ordenarle que desde el número elegido, avance hacía la izquierda (si es menor) y hacia la derecha (si es mayor ) en la posición de la nueva lista


"""
