conversation = []

def debug_pipeline(conversation):

    last_message = conversation[-1]["content"].lower()

    if "pipeline" in last_message:
        reply = "What error did you see?"
    elif "timeout" in last_message:
        reply = "Pipeline failed due to timeout. Check long-running jobs"
    else:
        reply = "This is not related to the CICD failure issue"
    
    return reply

while True:
    user_input = input("USER:")
    if user_input.lower() == "exit":
        print("Goodbye")
        break

    conversation.append(
        {"role": "user", "content": user_input}
    )
     
    ai_reply = debug_pipeline(conversation)

    conversation.append(
        {"role": "BOT", "content": ai_reply}
    )

    print("BOT:", ai_reply)
    print("converstation memory:", conversation)
    