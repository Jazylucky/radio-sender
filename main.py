
send = "s"
def on_forever2():
    radio.set_group(1)
    if input.button_is_pressed(Button.A):
        send = "f"
        basic.show_string("f")
        pass
    if input.button_is_pressed(Button.B):
        send = "b"
        basic.show_string("b")
        pass
    if input.pin_is_pressed(TouchPin.P1):
        send = "s"
        basic.show_string("s")
        pass
    
    if input.pin_is_pressed(TouchPin.P0):
        send = "l"
        basic.show_string("l")
        pass
    if input.pin_is_pressed(TouchPin.P3):
        send = "r"
        basic.show_string("r")
        pass

    
    def on_received_number(receivedNumber):
        if receivedNumber <= 20:
            send = "s"
            basic.show_string("fs")
    radio.on_received_number(on_received_number)


    radio.send_string(send)

    def on_received_string(receivedString):
        pass
    radio.on_received_string(on_received_string)
basic.forever(on_forever2)