import machine, time
from machine import Pin


pin1 = Pin(22, Pin.OUT)
pin2 = Pin(23, Pin.OUT)

poste_1 = machine.Pin(15, machine.Pin.IN)
poste_2 = machine.Pin(16, machine.Pin.IN)
poste_3 = machine.Pin(17, machine.Pin.IN)
induction = machine.Pin(18, machine.Pin.IN)

y = 100
position: int = 0

def left(vitesse):
    pin1.value(1)
    pin2.value(0)


def right(vitesse):
    pin1.value(0)
    pin2.value(1)

def stop():
    pin1.value(1)
    pin2.value(1)


while True:
    if poste_1 :
        if position == 1:
            stop()
            print("at the right post")
        else :
            while position > 1:
                right(y)
                if induction:
                    position -= 1
                    if position == 1:
                        stop()
                        print(" at the right post")

    if poste_2 :
        if position == 2:
            stop()
            print("at the right post")
        elif position == 1:
            left(y)
            if induction:
                position += 1
                if position == 2:
                    stop()
                    print(" at the right post")
        elif position == 3:
            right(y)
            if induction:
                position -= 1
                if position == 2:
                    stop()
                    print(" at the right post")

    if poste_3 :
        if position == 3:
            stop()
            print("at the right post")
        else :
            while position < 3:
                left(y)
                if induction:
                    position += 1
                    if position == 3:
                        stop()
                        print(" at the right post")