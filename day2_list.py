# List store multiple variables 
# You can store anything in list basically it is an container so you can put anything you want 
# list are modifiable 
servers = ["webs1", "web2","db1"]

servers[1] = "db2" #To update the list 

servers.append("redis1") # For adding the items in the list, we can append in the end only 

# Below is the function created to pass the list into the function 
def show_servers(server_list):
    print("Server list is :", server_list) 

show_servers(servers)

print ("All servers:", servers)
print ("name of 1st server:", servers[0])
print ("name of last server:", servers[2])
print ("name of mid server:", servers[1])