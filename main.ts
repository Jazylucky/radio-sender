basic.forever(function on_forever2() {
    radio.setGroup(1)
    if (input.buttonIsPressed(Button.A)) {
        radio.sendString("f")
        basic.showString("f")
        
    }
    
    if (input.buttonIsPressed(Button.B)) {
        radio.sendString("b")
        basic.showString("b")
        
    }
    
    if (input.pinIsPressed(TouchPin.P1)) {
        radio.sendString("s")
        basic.showString("s")
        
    }
    
    if (input.pinIsPressed(TouchPin.P0)) {
        radio.sendString("l")
        basic.showString("l")
        
    }
    
    if (input.pinIsPressed(TouchPin.P3)) {
        radio.sendString("r")
        basic.showString("r")
        
    }
    
    radio.onReceivedString(function on_received_string(receivedString: string) {
        
    })
})
