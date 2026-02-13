conversation = []

def simple_reply(conversation):
 
    last_message = conversation[-1]["content"].lower()


    if "docker" in last_message:
        reply = "Docker is a container platform."
    elif "kubernetes" in last_message:
        reply = "Kubernetes manages containers."
    else:
        reply = "I don't know about that yet."

    return reply

# The while loop is used which is true always to run where we take the input from the user 
while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    # Add user message to memory
    conversation.append(
        {"role": "user", "content": user_input}
    )

    # Generate reply
    bot_reply = simple_reply(conversation)

    # Add bot reply to memory
    conversation.append(
        {"role": "assistant", "content": bot_reply}
    )

    print("Bot:", bot_reply)

    print("\nConversation memory:", conversation)