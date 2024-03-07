import threading
import time

led_A = threading.Lock()
led_B = threading.Lock()
led_C = threading.Lock()
leds = {"led_A": "LED A", "led_B": "LED B", "led_C": "LED C"}


def P1():
    while True:
        led_A.acquire()
        print("P1 a acquis la LED A")
        led_B.acquire()
        print("P1 a acquis la LED B")
        print("P1 configure les couleurs en vert")
        print("P1 émet des signaux")
        time.sleep(1)
        led_B.release()
        led_A.release()


def P2():
    while True:
        led_B.acquire()
        print("P2 a acquis la LED B")
        led_C.acquire()
        print("P2 a acquis la LED C")
        print("P2 configure les couleurs en orange")
        print("P2 émet des signaux")
        time.sleep(1)
        led_C.release()
        print("P2 a rendu la LED C")
        led_B.release()
        print("P2 a rendu la LED B")


def P3():
    while True:
        led_C.acquire()
        print("P3 a acquis la LED C")
        led_A.acquire()
        print("P3 a acquis la LED A")
        print("P3 configure les couleurs en rouge")
        print("P3 émet des signaux")
        time.sleep(1)
        led_A.release()
        print("P3 a rendu la LED A")
        led_C.release()
        print("P3 a rendu la LED C")

def p(prim,sec,ide):
    while True:
        prim.acquire()
        print("P"+str(ide),"à acquis",leds[prim])
        sec.acquire()
        print("P"+str(ide),"à acquis",leds[sec])
        time.sleep(1)
        sec.release()
        prim.release

t_P1 = threading.Thread(target=P1, args=[])
t_P2 = threading.Thread(target=P2, args=[])
t_P3 = threading.Thread(target=P3, args=[])

t_P4 = threading.Thread(target = p, args=[led_A,led_B,1])

t_P4.start()
