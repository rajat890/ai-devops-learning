# This is for the learning of coding 

def greet_user(name):   #greet_user is a function name
    message = f"Hello {name}, welcome to DevOps + AI learning"
    return message

user_name = input("Enter your name:")
result = greet_user(user_name)
print(result)