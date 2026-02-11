import requests

url = "https://httpbin.org/post"

payload = {
    "message": "Hello AI",
    "number": 42
}


response = requests.post(url, json=payload)

print("Status Code:", response.status_code)

data = response.json()

print("\nFull Response:")
print(data)

print("\nData We Sent (Echoed Back):")
print(data["json"])
