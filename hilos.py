import threading
import time

def mainFunction(name):
    print("hola que tal "+name)
    time.sleep(5)

if __name__ == '__mian__':
    thread = threading.Thread(target=mainFunction,args=("Codi",))
    thread.start()
    thread.join()
    print("hola, un saludo desde el hilo principal del còdigo")