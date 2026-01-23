# this is for the pratice 

Server = {
    "Hostname": "Ec2",
    "IP": "10.9.8.7",
    "Cloud": "AWS"
}

def server_details(info):
    return f"The name of the server is {info['Hostname']} p is {info['IP']} and cloud is {info['Cloud']}"

details = server_details(Server)
print(details)