let send = "s"
basic.forever(function on_forever2() {
    let send: string;
    radio.setGroup(1)
    if (input.buttonIsPressed(Button.A)) {
        send = "bf"
        basic.showString("f")
        
    }
    
    if (input.buttonIsPressed(Button.B)) {
        send = "bb"
        basic.showString("b")
        
    }
    
    if (input.pinIsPressed(TouchPin.P1)) {
        send = "bs"
        basic.showString("s")
        
    }
    
    if (input.pinIsPressed(TouchPin.P0)) {
        send = "lf"
        basic.showString("l")
        
    }
    
    if (input.pinIsPressed(TouchPin.P3)) {
        send = "rf"
        basic.showString("r")
        
    }
    
    radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
        let send: string;
        if (receivedNumber <= 20) {
            send = "bs"
            basic.showString("fs")
        }
        
    })
    radio.sendString(send)
    radio.onReceivedString(function on_received_string(receivedString: string) {
        
    })
})
