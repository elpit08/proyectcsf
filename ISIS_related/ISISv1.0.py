def talk_to_ISIS(mensaje):

    import serial
    import time
    import requests
    url = "http://localhost:11434/api/generate"
    system_prompt="""You are ISIS, 
    a personal AI assistant design to help with: Arduino, Robotics, Math and coding
    -You talk in a casual but technical language
    -Make questions if needed for a complete anwser
    a personal AI assistant design to help with: Arduino, Robotics, Math and coding
    -You talk in a casual but technical language
    -Make questions if needed for a complete anwser """


    data = {
        "model": "granite4.1:8b",
        "prompt": mensaje,
        "stream": False
    }
    anwser = requests.post(url,json=data)
    anwser_json = anwser.json()
    anwser_text = anwser_json["response"]

    return anwser_text

print("---ISIS v1.0---")
print("Write `exit` to finish the sesion\n")

while True:
    my_message = input("Yo: ")

    if my_message.lower() == "exit":
        print("ISIS is at your command")
        break
    anwser= talk_to_ISIS(my_message)
    print(f"ISIS: {anwser}\n")
