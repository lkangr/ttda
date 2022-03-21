def on_data_received():
    message = serial.read_until('#')
    if message == '0':
        pins.digital_write_pin(DigitalPin.P1, 0)
    elif message == '1':
        pins.digital_write_pin(DigitalPin.P1, 1)
serial.on_data_received('#', on_data_received)

led.enable(False)

def on_forever():
    NPNBitKit.dht11_read(DigitalPin.P3)
    serial.write_string("!1:TEMP:" + ("" + str(NPNBitKit.dht11_temp())) + "#")
    serial.write_string("!1:HUMI:" + ("" + str(NPNBitKit.dht11_hum())) + "#")
    basic.pause(5000)
basic.forever(on_forever)
