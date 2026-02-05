import requests

url = "https://jsonplaceholder.typicode.com/posts"

def get_user_data(api_url):
    response = requests.get(api_url)
    data = response.json()
    return data

def filter_user_data(user_list):
    results = []
    for user in user_list:
        results.append(
            {
                "ID": user["id"],
                "Title": user["title"]
            }
        )
    return results

user_data = get_user_data(url)

final_data = filter_user_data(user_data)

for item in final_data:
    print(item)

