from machine import Pin
from time import sleep

dp = Pin(0, Pin.OUT)
cl = Pin(1, Pin.OUT)
la = Pin(2, Pin.OUT)
clr = Pin(3, Pin.OUT, Pin.PULL_UP)

dp.value(0)
cl.value(0)
la.value(0)

num_0 = 0b00000011
num_1 = 0b10011111
num_2 = 0b00100101
num_3 = 0b00001101
num_4 = 0b10011001
num_5 = 0b01001001
num_6 = 0b01000001
num_7 = 0b00011111
num_8 = 0b00000001
num_9 = 0b00001001


def clear():
    clr.low()
    clr.high()


clear()


def tick():
    cl.low()
    cl.high()


def latch():
    la.high()
    la.low()


def write(value, n_of_bits):
    for i in range(n_of_bits):
        data = value >> i & 1
        if data == 0:
            dp.high()
        else:
            dp.low()
        tick()
    latch()
    sleep(0.5)


while True:
    write(num_1 << 8 | num_0, 16)
    sleep(1)
    write(num_1 << 8 | num_1, 16)
    sleep(1)
    write(num_1 << 8 | num_2, 16)
    sleep(1)
    write(num_1 << 8 | num_3, 16)
    sleep(1)
