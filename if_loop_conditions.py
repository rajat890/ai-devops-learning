services = [
    {"name": "auth", "status": "running"},
    {"name": "payment", "status": "stopped"},
    {"name": "search", "status": "running"}
]

def service_status(service_list):
    for service in service_list:
        if service["status"]=="running":
            print (f"Service {service['name']} is running")
        else:
            print(f"service {service['name']} is not running")

service_status(services)