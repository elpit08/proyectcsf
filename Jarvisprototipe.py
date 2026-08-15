def talk_to_jarvis(mensaje):
    url = "http://localhost:11434/api/generate"


    data = {
        "model": "granite4.1:8b",
        "prompt": mensaje,
        "stream": False
    }
    anwser = requests.post(url,json=data)
    anwser_json = anwser.json()
    anwser_text = anwser_json["response"]

    return anwser_text

print("---Jarvis Prototipe---")
print("Write `exit` to finish the sesion\n")

while True:
    my_message = input("Yo: ")

    if my_message.lower() == "exit":
        print("Jarvis is at your service")
        break
    anwser= talk_to_jarvis(my_message)
    print(f"Jarvis: {anwser}\n")
