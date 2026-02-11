import requests

url = "https://httpbin.org/post"

# Step 1: Build payload (just like chatbot would)
payload = {
    "message": "Hello from Rajat"
}

# Step 2: Send POST request
response = requests.post(url, json=payload)

# Step 3: Convert response to Python dictionary
data = response.json()

print("Full Response:")
print(data)

print("\nServer Received This JSON:")
print(data["json"])

print("\nExtracted Message:")
print(data["json"]["message"])
