import threading
import time


filosofos = 5
garfos = []
for i in range(filosofos):
    garfos.append(threading.Lock())

def funcao(i):
    while True:
        print("Filosofo", i, "pensando")
        time.sleep(2)


        print("Filosofo", i, "com fome")


        garfo_esquerda = i
        garfo_direita = (i + 1) % filosofos

#todos tentam pegar primeiro o garfo da esquerda
        garfos[garfo_esquerda].acquire()
        time.sleep(1)

        garfos[garfo_direita].acquire()


        print("Filosofo", i, "esta comendo")
        time.sleep(2)


        garfos[garfo_direita].release()
        garfos[garfo_esquerda].release()


        print("Filosofo", i, "terminou de comer")

lista = []
for i in range(filosofos):
    t = threading.Thread(target=funcao, args=(i,))
    lista.append(t)

for t in lista:
    t.start()

for t in lista:
    t.join()
