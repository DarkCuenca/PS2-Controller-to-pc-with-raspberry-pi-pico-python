import usb_hid

class Gamepad:
    def __init__(self):
        self._device = None
        for d in usb_hid.devices:
            if d.usage_page == 0x01 and d.usage == 0x05:
                self._device = d
                break
        if not self._device:
            raise RuntimeError("No HID gamepad device found")

        self._buttons = 0
        self._hat = 0 # 0=Neutral, 1=Arriba, 2=Arriba-Der, 3=Der, etc.
        self._axes = [0, 0, 0, 0] # X, Y, Rx, Ry

    def press_buttons(self, *buttons):
        for b in buttons:
            self._buttons |= (1 << (b - 1))
        self._send()

    def release_buttons(self, *buttons):
        for b in buttons:
            self._buttons &= ~(1 << (b - 1))
        self._send()
        
    def set_hat(self, value):
        self._hat = value
        self._send()

    def move_joysticks(self, x=0, y=0, rx=0, ry=0):
        self._axes = [x, y, rx, ry]
        self._send()

    def _send(self):
        report = bytearray(7) # Ahora son 7 bytes
        # Byte 0 y 1: Botones
        report[0] = self._buttons & 0xFF
        report[1] = (self._buttons >> 8) & 0xFF
        
        # Byte 2: Hat Switch (solo toma los primeros 4 bits)
        report[2] = self._hat & 0x0F
        
        # Bytes 3 a 6: Ejes (X, Y, Z, Rz)
        for i in range(4):
            val = max(-127, min(127, self._axes[i]))
            report[3 + i] = val & 0xFF
            
        try:
            self._device.send_report(report)
        except Exception as e:
            print("Error enviando reporte USB:", e)