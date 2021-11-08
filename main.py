from machine import Pin
from time import sleep
import _thread

dp = Pin(0, Pin.OUT)
cl = Pin(1, Pin.OUT)
la = Pin(2, Pin.OUT)
clr = Pin(3, Pin.OUT, Pin.PULL_UP)

dots = Pin(4, Pin.OUT)

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

numbers = [num_0, num_1, num_2, num_3, num_4, num_5, num_6, num_7, num_8, num_9]


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


def write(value):
    for i in range(16):
        data = value >> i & 1
        if data == 0:
            dp.high()
        else:
            dp.low()
        tick()
    latch()
    sleep(0.5)


def toBit(number):
    if number < 10:
        return numbers[0] << 8 | numbers[number]
    elif number > 9 & number < 100:
        digits = toDigits(number)
        return numbers[digits[0]] << 8 | numbers[digits[1]]
    else:
        return numbers[0] << 8 | numbers[0]


def toDigits(number):
    return list(map(int, ' '.join(str(number)).split()))


def blink_clock_dots():
    dots_high = False
    while True:
        if dots_high:
            dots.low()
        else:
            dots.high()
        dots_high = not dots_high
        sleep(1)


_thread.start_new_thread(blink_clock_dots, ())

while True:
    for i in range(99):
        write(toBit(i))
        sleep(1)
