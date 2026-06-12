import cv2
import numpy as np
import os

# Forzamos a OpenCV a usar el framebuffer de tu pantalla TFT
os.environ["SDL_FBDEV"] = "/dev/fb1"

LCD_W, LCD_H = 480 ,320

cap = cv2.VideoCapture(0)

print("Presiona 'q' en la terminal para cerrar el monitor")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.rotate(frame, cv2.ROTATE_180)
    frame = cv2.flip(frame, 1)
 # Redimensionar a la resolución de tu pantalla de 3.5" (comúnmente 480x320)
    frame_lcd = cv2.resize(frame, (LCD_W, LCD_H))

    # Mostrar en una ventana (si tienes entorno gráfico en la TFT)
    cv2.imshow('Ojos de Bmoo', frame_lcd)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
