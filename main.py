from machine import ADC
from time import sleep

# TEMP Sensor
adc = ADC(4)


def calculateTemp():
    voltage = adc.read_u16() * 3.3 / 65535
    return 27 - (voltage - 0.706) / 0.001721


while True:
    print(calculateTemp())
    sleep(1)
