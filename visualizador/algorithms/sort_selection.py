# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}
import time
items = []
n = 0
i = 0          # cabeza de la parte no ordenada
j = 0          # cursor que recorre y busca el mínimo
min_idx = 0    # índice del mínimo de la pasada actual
fase = "buscar"  # "buscar" | "swap"

#METRICAS
vecesQueCompara=0
vecesQueCambia=0

#MEDIDOR DE TIEMPO
inicioTiempo=0 
finTiempo=0

def init(vals):
    global items, n, i, j, min_idx, fase, vecesQueCompara, vecesQueCambia, inicioTiempo, finTiempo
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i
    fase = "buscar"
    inicioTiempo=time.time() #Guadra la hora en el que el algoritmo empezo (Cuenta los segundos desde el 1 de enero de 1970 hasta ahora)

def step():
    global items, n, i, j, min_idx, fase, inicioTiempo, finTiempo, vecesQueCompara, vecesQueCambia
    if i>=n-1: 
        print("Selection comparo:", vecesQueCompara, "y cambio", vecesQueCambia) #Luego de ordenar todo mostramos cuantas veces comparo y cambio
        finTiempo=time.time() - inicioTiempo #Guarda el tiempo en el que termina.
        print("Tardo", finTiempo, "segundos") #Al igual que las metricsa para ver el resultado de cuanto tardo este algoritmo en completar el visauliazador, presionamos f12 y "console"
        return {"done": True}
        
#Si ya esta todo ordenado, devolvemos "done", True para terminar el algoritmo
#Para ver el resultado de las metricas vamos al visualizador y pulsamos F12, alli se abrira una pequeña pestaña, donde nos aparecera una opcion que dice "Console", alli podemos ver los resultados
    
#Cambiamos a fase "buscar", reccoremos toda la lista para ver que numero es el mas pequeño
    if fase== "buscar":
        if j<n:
            vecesQueCompara=VecesQueCompara+1 #Le agregamos uno cada vez que este compara dos numeros
            if items[j]<items[min_idx]:
                min_idx=j
            j=j+1
            return {"a": min_idx, "b": j-1, "swap": False, "done": False}
        fase="swap"

#Cambiamos a fase "swap", una vez encontrado el valor mas chico, esta fase se encarga de intercambiar el mas chico actual para asi ponerlo primero
    
    if fase== "swap": 
        swap=False
        if min_idx !=i:
            items[i], items[min_idx] = items[min_idx], items[i]
            swap=True
            vecesQueCambia=vecesQueCambia+1 #Sumamos uno cada vez que dos numeros cambian de lugar

#Después de cambiar los valores, el algoritmo se prepara para seguir con el próximo movimiento (si es que todavia queda por ordenar), en simples palabras prepara todo para seguir con el siguiente valor  
        a=i
        b=min_idx
      
        i=i+1
        j=i+1
        min_idx=i
        fase="buscar"
        return{"a": a , "b": b, "swap": swap, "done": False}
    # TODO:
    # - Fase "buscar": comparar j con min_idx, actualizar min_idx, avanzar j.
    #   Devolver {"a": min_idx, "b": j_actual, "swap": False, "done": False}.
    #   Al terminar el barrido, pasar a fase "swap".
    # - Fase "swap": si min_idx != i, hacer ese único swap y devolverlo.
    #   Luego avanzar i, reiniciar j=i+1 y min_idx=i, volver a "buscar".
    #
    # Cuando i llegue al final, devolvé {"done": True}.
    
