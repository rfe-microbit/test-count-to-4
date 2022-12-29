x = 0

def on_button_pressed_a():
    global x
    x = 1
    for index in range(4):
        basic.show_number(x)
        x += 1
input.on_button_pressed(Button.A, on_button_pressed_a)
