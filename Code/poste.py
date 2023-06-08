from machine import ADC, Pin, PWM
import time

servo = PWM(Pin(35), freq=50)
can = ADC(Pin(34))  # crée un objet ADC sur la broche 34
can.atten(ADC.ATTN_11DB)  # étendue totale : 3.3V
ADC.width(ADC.WIDTH_10BIT)

def pot_to_deg(pot):
    return pot*0.176

while True:
    pot = can.read()
    servo.duty(pot_to_deg(pot))
    time.sleep(0.1)
