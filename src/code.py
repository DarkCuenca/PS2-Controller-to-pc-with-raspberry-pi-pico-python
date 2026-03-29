import board
import ps2controller
from gamepad import Gamepad
import time

gp = Gamepad()

ps2 = ps2controller.PS2Controller(
    dat=board.GP2, 
    cmd=board.GP3, 
    att=board.GP4, 
    clk=board.GP5,
    enable_sticks=True
)

# Mapeo optimizado
mapeado = {
    14: 1,   # CROSS
    13: 2,   # CIRCLE
    15: 4,   # SQUARE
    12: 5,   # TRIANGLE
    10: 7,   # L1
    11: 8,   # R1
    8:  9,   # L2
    9:  10,  # R2
    0:  11,  # SELECT
    3:  12,  # START
    1:  14,  # L3
    2:  15,  # R3
}

def aplicar_deadzone(valor, zona_muerta=15):
    if abs(valor) < zona_muerta: return 0
    return valor

while True:
    events = ps2.update()
    
    # 1. Botones de acción
    if events:
        for ev in events:
            boton_usb = mapeado.get(ev.id)
            if boton_usb:
                if ev.pressed: gp.press_buttons(boton_usb)
                if ev.released: gp.release_buttons(boton_usb)

    # 2. Combinación para Botón 16 (HOME / Launcher)
    # Detectamos Select (0) y Start (3) físicos
    if ps2.button(0) and ps2.button(3):
        gp.press_buttons(16)
    else:
        gp.release_buttons(16)

    # 3. D-Pad (Hat Switch)
    up, right, down, left = ps2.button(4), ps2.button(5), ps2.button(6), ps2.button(7)
    hat_val = 0
    if up and right: hat_val = 2
    elif right and down: hat_val = 4
    elif down and left: hat_val = 6
    elif up and left: hat_val = 8
    elif up: hat_val = 1
    elif right: hat_val = 3
    elif down: hat_val = 5
    elif left: hat_val = 7
    gp.set_hat(hat_val)

    # 4. Sticks Analógicos con Filtro
    lx, ly = ps2.analog_left()
    rx, ry = ps2.analog_right()
    if lx != -1:
        gp.move_joysticks(
            aplicar_deadzone(int(lx - 128)), 
            aplicar_deadzone(int(ly - 128)), 
            aplicar_deadzone(int(rx - 128)), 
            aplicar_deadzone(int(ry - 128))
        )
    
    time.sleep(0.01)
