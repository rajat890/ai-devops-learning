# import is used to call the functions which are created by others and use in the code 
import requests

URL = "https://jsonplaceholder.typicode.com/users"

#the below fucntion will call the api and the reponse is string so we convert into json as python understand only list and dictonaries
def fetch_api_data(api_url):
    """
    Calls the external API and converts JSON response into Python data
    """
    response = requests.get(api_url)
    data = response.json()
    return data

# The below function will extract the required fields which we need from the raw data 
def extract_required_fields(users):
    """
    Takes raw API data and extracts only required fields
    """
    results = []

    for user in users:
        results.append(
            {
                "Name": user["name"],
                "Email": user["email"],
                "Username": user["username"]
            }
        )

    return results


# Step 2: Call API
raw_data = fetch_api_data(URL)

# Step 3: Process API data
processed_data = extract_required_fields(raw_data)

# Step 4: Display output (presentation only)
for item in processed_data:
    print(item)

print(type(raw_data))
print(type(processed_data))




#The below is the public url for which there is no login needed 
#url = "https://jsonplaceholder.typicode.com/users"

#response = requests.get(url) # this will give the data in string format and on which we cannot do the parsing 

#data = response.json()

#print(data)
#print(type(data))
#print(data[0]["name"])

#print(response) # this will just give the reponse code 
#print(type(response.text)) # this will give the object body of the url 

#def fetch_users(api_url):
#    response = requests.get(api_url)
#    data = response.json
#    return data

#result = fetch_users(url)
#print (result)