import serial
import time

def enviar_comando_arduino(comando, puerto="/dev/ttyACM0", velocidad=9600 ):
    " Envia un comando a Arduino y espara respuesta Ejemplo: respuesta = enviar_comando_arduino(LED_ON) print(respuesta) #Imprime: LED encendido"

    try:
        arduino = serial.Serial(puerto, velocidad, timeout=1)
        time.sleep(2)

        arduino.write((comando + "\n").encode())

        respuesta = arduino.readline().decode().strip()

        arduino.close()

        return respuesta
    except Exception as error:
        return f"Error de comicacion: {error}"

print("--- Prueba de LED ---")
print("Escribe comandos:")
print(" LED_ON  - Enciende el LED")
print(" LED_OFF - Apaga el LED")
print(" exit    - Salir")

while True:
    comando = input("YO: ")

    if comando.lower() == "exit":
        print("Prueba terminada")
        break

    if comando in ["LED_ON", "LED_OFF"]:
        print(f"Enviado: {comando}")
        respuesta = enviar_comando_arduino(comando)
        print(f"Arduino respondio: {respuesta}\n")
    else:
        print("Comando no reconocido. Intenta: LED_ON o LED_OFF \n")