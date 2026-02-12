def debug_pipeline(message):
    if "timeout" in message.lower():
        reply = "Pipeline failed due to timeout. Check long-running jobs."
    elif "permission" in message.lower():
        reply = "Pipeline failed due to permission issue. Check IAM roles."
    elif "docker" in message.lower():
        reply = "Pipeline failed during Docker build stage."
    else :
        reply = "Unable to determine failure reason."
        
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
    user_input = input("YOU: ")
    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break
    
    ai_data = debug_pipeline(user_input)

    reply = ai_data["choices"][0]["message"]["content"]

    print("BOT: ", reply)

