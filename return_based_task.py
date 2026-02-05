services = [
    {"name": "auth", "status": "running"},
    {"name": "payment", "status": "stopped"},
    {"name": "search", "status": "running"}
]

def analyze_services(service_list):
    result = []

    for service in service_list:
        if service["status"] == "running":
            result.append(
                {
                  "Name" :service["name"],
                  "Health" : "Healthy",
                  "Status" : service["status"]
                }
            )
        else:
            result.append(
                {
                    "Name" : service["name"],
                    "Health": "Unhealthy",
                    "Status" : service["status"]
                }
            )
    return result

Data = analyze_services(services)
for item in Data:
    print(item)
