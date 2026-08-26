import requests
import time
from test_led import enviar_comando_arduino

def talk_to_ISIS(mensaje):
    "ISIS transforma mis comandos naturales y ejecuta esas acciones en Arduino"

    url = "http://localhost:11434/api/generate"

    system_prompt = """Eres ISIS, una IA especializada en robotica y arduino. Tu trabajo es responder a mis preguntas y cuando se te ordene hacer un comando en arduino interpreta los comandos del usuario y ejecutalos en Arduino. Cuando el usuario pida encender/ apagar el LED responde con "Ejecutando: LED_ON" o "Ejecutando: LED_OFF". Despues de "Ejecutando: " siempre va el comando Arduino."""

    prompt_completo = system_prompt + "\n\nUsuario: " + mensaje + "\n\nISIS:"

    data = {
        "model": "granite4.1:8b",
        "prompt": prompt_completo,
        "stream": False
    }

    respuesta_ISIS = requests.post(url, json=data).json()["response"]

    comando_arduino = extraer_comando(respuesta_ISIS)

    if comando_arduino:
        resultado = enviar_comando_arduino(comando_arduino)
        return f"{respuesta_ISIS}\n[Arduino: {resultado}]"

    return respuesta_ISIS

def extraer_comando(texto):
    "busca un comando Arduino en el texto de ISIS. Busca patrones como: LED_ON, LED_OFF"

    palabras = texto.split()

    for palabra in palabras:
        if palabra.startswith("LED_"):
            return palabra

    return None
print("--- ISIS con arduino test1 ---")
print("Di comandos como: Eciende el led o apaga el led")
print("Escribe  exit  para salir\n")

while True:
    mensaje = input("Yo: ")

    if mensaje.lower() == "exit":
        print("ISIS a tus ordenes")
        break

    respuesta = talk_to_ISIS(mensaje)
    print(f"ISIS: {respuesta}\n")
    