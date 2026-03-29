# 🎮 PS2 Controller to PC con Raspberry Pi Pico (Python)

Convierte un mando clásico de PlayStation 2 en un gamepad USB moderno y totalmente personalizable utilizando una Raspberry Pi Pico.

Este proyecto está especialmente optimizado para sistemas Linux (como Arch Linux con Hyprland), pero funciona en cualquier sistema que soporte dispositivos HID estándar.

---

## ✨ Características

* **🔌 Plug & Play**
  Reconocido automáticamente como un gamepad USB HID estándar.

* **🎯 D-Pad como Hat Switch**
  La cruceta funciona correctamente como POV (Point of View), no como botones independientes.

* **🏠 Botón Home Virtual**
  Detecta la combinación `Select + Start` y la envía como un botón dedicado (Botón 16).
  Ideal para abrir Steam Big Picture o launchers.

* **🎚️ Filtro de Precisión (Deadzone)**
  Reduce el drift en sticks analógicos desgastados mediante zonas muertas configurables.

* **⚡ Baja Latencia**
  Procesamiento directo con CircuitPython para una respuesta rápida en juegos exigentes.

---

## 🛠️ Requisitos de Hardware

* Mando de PS2 (original o compatible)
* Raspberry Pi Pico o clon (ej. YD-RP2040)

---

## 🔌 Diagrama de Conexión

| Mando PS2 | Color Cable | Raspberry Pi Pico |
| --------- | ----------- | ----------------- |
| DAT       | Café        | GP2               |
| CMD       | Naranja     | GP3               |
| ATT       | Amarillo    | GP4               |
| CLK       | Azul        | GP5               |
| VCC       | Rojo        | 3V3               |
| GND       | Negro       | GND               |

---

## 🚀 Instalación

1. Instala **CircuitPython** en la Raspberry Pi Pico.

2. Copia los siguientes archivos en la raíz del dispositivo:

   * `boot.py` → Configura el descriptor HID (7 bytes)
   * `gamepad.py` → Emulación del gamepad USB
   * `ps2controller.py` → Driver del protocolo PS2
   * `code.py` → Lógica principal y mapeo de botones

3. Conecta el mando PS2.

4. ¡Listo! El sistema debería reconocerlo automáticamente.

---

## ⚙️ Personalización

Puedes modificar fácilmente:

* 🎮 Mapeo de botones
* 🎚️ Deadzones de sticks
* 🧠 Combinaciones especiales (como el botón Home)

Edita el archivo `code.py` según tus necesidades.

---

## 📜 Licencia

Este proyecto está bajo la **Licencia MIT**.

Eres libre de:

* Usar
* Modificar
* Distribuir

Siempre que mantengas el aviso de copyright original.

---

## 🙏 Créditos

* Basado en una adaptación de la librería **CircuitPython_PS2Controller** de Tod Kurt
* Optimización HID y lógica desarrollada por **Cuenca**

---

💡 *Este proyecto es ideal para reutilizar hardware clásico y crear soluciones personalizadas de alto rendimiento.*

