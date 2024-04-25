from machine import Pin, ADC

adc = ADC(Pin(26))

led_1 = Pin(12, Pin.OUT)
led_2 = Pin(12, Pin.OUT)
led_3 = Pin(12, Pin.OUT)
led_4 = Pin(12, Pin.OUT)


def null():
    led_1.off()
    led_2.off()
    led_3.off()
    led_4.off()


def first():
    led_1.on()
    led_2.off()
    led_3.off()
    led_4.off()


def second():
    led_1.on()
    led_2.on()
    led_3.off()
    led_4.off()


def third():
    led_1.on()
    led_2.on()
    led_3.on()
    led_4.off()


def fourth():
    led_1.on()
    led_2.on()
    led_3.on()
    led_4.on()


light_dict = {
    range(0, int(65535*0.25)): first,
    range(int(65535*0.25), int(65535*0.5)): second,
    range(int(65535*0.5), int(65535*0.75)): third,
    range(int(65535*0.75), 65535): fourth,


}

light_dict[adc.read_u16]()
