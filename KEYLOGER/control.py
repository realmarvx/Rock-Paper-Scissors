from pynput.mouse import Controller

def controlMouse():
    mouse = Controller()
    mouse.position = (300,500)
    #left to right, then top to bottom
    #this starts from the top left movement
controlMouse()

# from pynput.keyboard import Controller

# def controlKeyboard():
#     keyboard = Controller()
#     x=0
#     while x < 5 :
#         keyboard.type("Jinmi is not smart")
#         x = x+1

# controlKeyboard()

