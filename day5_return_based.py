#In this code we willl not print but focus on return the value as this will help in the automation 
service = {"name":"auth", "status":"running"}

def evaluate_service(service):
    if service["status"] == "running":
        return "healthy"
    else:
        return "unhealthy"
    
result = evaluate_service(service)

if result == "unhealthy":
    print("ALERT: Take action")
else:
    print("Everything OK")

#######################
### Storing the result in the emppty list #######
def evaluate_services(service_list):
    results = []

    for service in service_list:
        if service["status"] == "running":
            results.append({
                "name": service["name"],
                "health": "healthy"
            })
        else:
            results.append({
                "name": service["name"],
                "health": "unhealthy"
            })

    return results