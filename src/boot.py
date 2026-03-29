import usb_hid

# Descriptor HID actualizado con Hat Switch
gamepad_report_descriptor = (
    b"\x05\x01"       # Usage Page (Generic Desktop)
    b"\x09\x05"       # Usage (Gamepad)
    b"\xA1\x01"       # Collection (Application)
    b"\x85\x01"       #   REPORT_ID (1)
    
    # 1. Botones (16 botones = 2 bytes)
    b"\x05\x09"       #   Usage Page (Button)
    b"\x19\x01"       #   Usage Minimum (Button 1)
    b"\x29\x10"       #   Usage Maximum (Button 16)
    b"\x15\x00"       #   Logical Minimum (0)
    b"\x25\x01"       #   Logical Maximum (1)
    b"\x95\x10"       #   Report Count (16)
    b"\x75\x01"       #   Report Size (1)
    b"\x81\x02"       #   Input (Data,Var,Abs)
    
    # 2. Hat Switch (Cruceta = 1 byte)
    b"\x05\x01"       #   Usage Page (Generic Desktop)
    b"\x09\x39"       #   Usage (Hat switch)
    b"\x15\x01"       #   Logical Minimum (1)
    b"\x25\x08"       #   Logical Maximum (8)
    b"\x95\x01"       #   Report Count (1)
    b"\x75\x04"       #   Report Size (4)
    b"\x81\x42"       #   Input (Data,Var,Abs,Null State)
    b"\x75\x04"       #   Report Size (4)  (Padding para completar el byte)
    b"\x95\x01"       #   Report Count (1)
    b"\x81\x03"       #   Input (Const,Var,Abs)
    
    # 3. Ejes Analógicos (4 ejes = 4 bytes)
    b"\x15\x81"       #   Logical Minimum (-127)
    b"\x25\x7F"       #   Logical Maximum (127)
    b"\x09\x30"       #   Usage (X)
    b"\x09\x31"       #   Usage (Y)
    b"\x09\x33"       #   Usage (Rx)
    b"\x09\x34"       #   Usage (Ry)
    b"\x95\x04"       #   Report Count (4)
    b"\x75\x08"       #   Report Size (8)
    b"\x81\x02"       #   Input (Data,Var,Abs)
    b"\xC0"           # End Collection
)

gamepad = usb_hid.Device(
    report_descriptor=gamepad_report_descriptor,
    usage_page=0x01,
    usage=0x05,
    report_ids=(1,),
    # AHORA SON 7 BYTES EN TOTAL:
    in_report_lengths=(7,), 
    out_report_lengths=(0,),
)

usb_hid.enable((gamepad,))