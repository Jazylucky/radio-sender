

def on_forever2():
    radio.set_group(1)
    if input.button_is_pressed(Button.A):
        radio.send_string("f")
        basic.show_string("f")
        pass
    if input.button_is_pressed(Button.B):
        radio.send_string("b")
        basic.show_string("b")
        pass
    if input.pin_is_pressed(TouchPin.P1):
        radio.send_string("s")
        basic.show_string("s")
        pass
    
    if input.pin_is_pressed(TouchPin.P0):
        radio.send_string("l")
        basic.show_string("l")
        pass
    if input.pin_is_pressed(TouchPin.P3):
        radio.send_string("r")
        basic.show_string("r")
        pass

    
    def on_received_string(receivedString):
        pass
    radio.on_received_string(on_received_string)
basic.forever(on_forever2)