# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0

# Estado interno
stack = []          # Pila para simular recursión (tuplas (low, mid, high, fase))
temp = []           # Lista temporal para mezclar
i = j = k = 0       # Índices usados en fase de merge
phase = "split"     # Puede ser "split" o "merge"
current = None      # Segmento actual (low, mid, high)

def init(vals):
    """
    Inicializa el estado del algoritmo.
    """
    global items, n, stack, temp, i, j, k, phase, current
    items = list(vals)
    n = len(items)
    temp = [0] * n
    stack = [(0, n - 1, "split")]  # empezamos con todo el rango
    phase = "split"
    current = None
    i = j = k = 0

def step():
    """
    Ejecuta un micro-paso del algoritmo Merge Sort.
    Devuelve {"a": int, "b": int, "swap": bool, "done": bool}.
    """
    global items, n, stack, temp, i, j, k, phase, current

    # Si no quedan tareas pendientes, terminó
    if not stack:
        return {"done": True}

    # Tomar el subproblema actual
    if current is None:
        low, high, phase = stack.pop()
        mid = (low + high) // 2
        current = (low, mid, high)
        i = low
        j = mid + 1
        k = low

    low, mid, high = current

    # --- Fase 1: dividir ---
    if phase == "split":
        # Si ya está reducido a un solo elemento
        if low >= high:
            current = None
            return {"a": low, "b": high, "swap": False, "done": False}
        
        # Primero procesar la mitad derecha, luego la izquierda (LIFO)
        stack.append((low, mid, "merge"))       # Después se mezclan
        stack.append((mid + 1, high, "split"))  # Primero se divide derecha
        stack.append((low, mid, "split"))       # Luego se divide izquierda
        
        current = None
        return {"a": low, "b": high, "swap": False, "done": False}

    # --- Fase 2: mezclar ---
    if phase == "merge":
        # Si todavía quedan elementos en ambas mitades
        if i <= mid and j <= high:
            a, b = i, j
            if items[i] <= items[j]:
                temp[k] = items[i]
                i += 1
            else:
                temp[k] = items[j]
                j += 1
            k += 1
            return {"a": a, "b": b, "swap": False, "done": False}

        # Si queda algo en la mitad izquierda
        elif i <= mid:
            temp[k] = items[i]
            a = i
            i += 1
            k += 1
            return {"a": a, "b": high, "swap": False, "done": False}

        # Si queda algo en la mitad derecha
        elif j <= high:
            temp[k] = items[j]
            b = j
            j += 1
            k += 1
            return {"a": low, "b": b, "swap": False, "done": False}

        # Si ya se completó la mezcla, copiar de temp a items
        else:
            for x in range(low, high + 1):
                items[x] = temp[x]
            current = None
            return {"a": low, "b": high, "swap": True, "done": False}
