#This is for the condition learning for the loops 
status = "running"

if status == "running":
    print ("service is healthy")
else:
    print ("service is not healthy")

# Using the IF loop in function 
def status_check(status):
    if status == "running":
        return "service is up"
    else:
        return "service is down"

result = status_check("stopped")
print(result)

#Using the loop in list if dictionary 
servers = [
    {"name": "server1", "status":"running"},
    {"name": "server2", "status":"stopped"},
    {"name": "server3", "status":"running"},
]

for server in servers:
    if server["status"] == "running":
        print(f"{server['name']} is healthy")
    else:
        print(f"{server['name']} is unhealthy")