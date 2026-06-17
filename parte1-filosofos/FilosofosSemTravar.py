import threading
import time
import random

filo = 5
garfos = []

for i in range(filo):
    garfos.append(threading.Lock())

def funcao(i):
    while True:
        print("Filosofo", i, " pensando")
        time.sleep(random.randint(4, 10))  

        print("Filosofo", i, "com fome")

        garfo_esquerda = i
        garfo_direita = (i + 1) % filo
  
        menor = min(garfo_esquerda, garfo_direita)
        maior = max(garfo_esquerda, garfo_direita)

        garfos[menor].acquire()
        garfos[maior].acquire()

        print("Filosofo", i, " comendo")
        time.sleep(random.randint(4, 10))  

        garfos[maior].release()
        garfos[menor].release()

        print("Filosofo", i, "terminou de comer")

lista = []

for i in range(filo):
    t = threading.Thread(target=funcao, args=(i,))
    lista.append(t)

for t in lista:
    t.start()

for t in lista:
    t.join()
