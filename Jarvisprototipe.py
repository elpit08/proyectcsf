def talk_to_jarvis(mensaje):
    url = "http://localhost:11434/api/generate"


    data = {
        "model": "granite4.1:8b",
        "prompt": mensaje,
        "stream": False
    }