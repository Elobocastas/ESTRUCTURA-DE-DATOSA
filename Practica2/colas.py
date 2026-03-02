
def enque(lista, elemento):
    lista.append(elemento)

def deque(lista):
    return lista.pop(0)

def is_empty(lista):
    if lista == []:
        return True
    else:
        return False


def procesar_retiro(cola_saldos, cola_retiros):
    s = deque(cola_saldos)
    r = deque(cola_retiros)
    nuevo_s = s - r
    enque(cola_saldos, nuevo_s)
    print("s:", s, " r:", r, " nuevo s:", nuevo_s)

def procesar_deposito(cola_saldos, cola_depositos):
    s = deque(cola_saldos)
    d = deque(cola_depositos)
    nuevo_s = s + d
    enque(cola_saldos, nuevo_s)
    print("s:", s, " d:", d, " nuevo s:", nuevo_s)

saldo = [1000, 1000, 1000, 1000, 1000]
retiros = [500, 500, 500, 500, 500]
depositos = [300, 300, 300, 300, 300]

print("RETIROS:")
while not is_empty(retiros):
    procesar_retiro(saldo, retiros)

print("DEPOSITOS:")
while not is_empty(depositos):
    procesar_deposito(saldo, depositos)

print("s final:", saldo)