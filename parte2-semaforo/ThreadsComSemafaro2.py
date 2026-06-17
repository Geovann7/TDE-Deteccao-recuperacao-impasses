import threading
import time

contador = 0
semafaro = threading.Semaphore(1)
#------------
def incrementar():
    global contador
    for i in range(200000):
        semafaro.acquire()
        try:
            contador += 1
        finally:
            semafaro.release()

#----------
inicio = time.time()

thread1 = threading.Thread(target=incrementar)
thread2 = threading.Thread(target=incrementar)
thread3 = threading.Thread(target=incrementar)
thread4 = threading.Thread(target=incrementar)
thread5 = threading.Thread(target=incrementar)
thread6 = threading.Thread(target=incrementar)
thread7 = threading.Thread(target=incrementar)
thread8 = threading.Thread(target=incrementar)

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
thread6.join()
thread7.join()
thread8.join()

fim = time.time()

print("Com semáfaro")
print("Esperado: 1.600.000")
print("Resultado :", contador)
print("Tempo:", fim - inicio)