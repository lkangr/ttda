f = 0
w = 0

def on_data_received():
    global f, w
    message = serial.read_until('#')
    if message == 'f0':
        pins.digital_write_pin(DigitalPin.P1, 0)
    elif message == 'f1':
        pins.digital_write_pin(DigitalPin.P1, 1)
        f = 30
    elif message == 'w0':
        pins.digital_write_pin(DigitalPin.P2, 0)
    elif message == 'w1':
        pins.digital_write_pin(DigitalPin.P2, 1)
        w = 30
serial.on_data_received('#', on_data_received)

def on_in_background():
    global f, w
    while True:
        if f != 0:
            f -= 1
            if f == 0:
                pins.digital_write_pin(DigitalPin.P1, 0)
        if w != 0:
            w -= 1
            if w == 0:
                pins.digital_write_pin(DigitalPin.P2, 0)
        basic.pause(1000)
control.in_background(on_in_background)

led.enable(False)

def on_forever():
    NPNBitKit.dht11_read(DigitalPin.P3)
    serial.write_string("!1:TEMP:" + ("" + str(NPNBitKit.dht11_temp())) + "#")
    serial.write_string("!1:HUMI:" + ("" + str(NPNBitKit.dht11_hum())) + "#")
    basic.pause(100000)
basic.forever(on_forever)
