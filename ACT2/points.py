# Librerías estándar
import os

# Librerías de terceros
import cv2

# Cargar la imagen original
painting_path = os.path.join("res", "painting.png")
image = cv2.imread(painting_path)

# Lista para guardar los puntos
points = []

# Función de callback para manejar los clics del ratón
def select_points(event, x, y, flags, param):
    global points
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(points) < 4:
            points.append((x, y))
            print(f"Punto seleccionado: ({x}, {y})")
            cv2.circle(image, (x, y), 5, (0, 0, 255), -1)
            cv2.imshow("Selecciona los puntos", image)

        if len(points) == 4:
            print("Se han seleccionado 4 puntos. Cerrando...")
            cv2.waitKey(1) 
            cv2.destroyAllWindows()

# Mostrar la imagen y registrar clics
cv2.namedWindow("Selecciona los puntos", cv2.WINDOW_NORMAL)
cv2.imshow("Selecciona los puntos", image)
cv2.setMouseCallback("Selecciona los puntos", select_points)

print("Haz clic en 4 puntos de origen en el orden: superior izquierdo, inferior izquierdo, superior derecho, inferior derecho.")
cv2.waitKey(0)

# Mostrar los puntos seleccionados
print("Puntos seleccionados:")
print(points)