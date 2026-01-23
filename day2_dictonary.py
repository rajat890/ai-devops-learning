# Dictonary is used to store the information in Key: value pair format 
# Think dictonary as ID card 
service = {
    "Name": "Rajat",
    "Age": "32",
    "Status": "Married"
}
service["Age"] = "28" # To update the existing value of the dictonary 

service["Job"] = "Software Engineer" # To add new value in the dictonary

def bio_data(info):
    return f"The name is {info['Name']} and the age is {info['Age']}"

data = bio_data(service)
print(data)

print(service)
print("the name is :", service["Name"])
print(service["Age"])
print(service["Job"])