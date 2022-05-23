
send = "bs"
def on_forever2():
    radio.set_group(1)
    if input.button_is_pressed(Button.A):
        send = "bf"
        basic.show_string("f")
        pass
    if input.button_is_pressed(Button.B):
        send = "bb"
        basic.show_string("b")
        pass
    if input.pin_is_pressed(TouchPin.P1):
        send = "bs"
        basic.show_string("s")
        pass
    
    if input.pin_is_pressed(TouchPin.P0):
        send = "lf"
        basic.show_string("l")
        pass
    if input.pin_is_pressed(TouchPin.P3):
        send = "rf"
        basic.show_string("r")
        pass
        
    def on_received_string(receivedString):
        basic.show_string(receivedString)
    radio.on_received_string(on_received_string)
    
    
    


    radio.send_string(send)

    def on_received_string(receivedString):
        pass
    radio.on_received_string(on_received_string)
basic.forever(on_forever2)