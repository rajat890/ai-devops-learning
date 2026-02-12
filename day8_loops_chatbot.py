def simple_reply(message):

    if "docker" in message.lower():
        reply = "Docker is a container platform."
    elif "kubernetes" in message.lower():
        reply = "Kubernetes manages containers."
    else:
        reply = "I don't know about that yet."

    return {
        "choices": [
            {
                "message": {
                    "role": "assistant",
                    "content": reply
                }
            }
        ]
    }

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    ai_data = simple_reply(user_input)

    reply = ai_data["choices"][0]["message"]["content"]

    print("Bot:", reply)