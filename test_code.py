services = [
    {"name": "auth", "status": "running"},
    {"name": "payment", "status": "stopped"},
    {"name": "search", "status": "running"},
    {"name": "email", "status": "stopped"}
]

def check_services(service_list):
    stopped_count = 0

    for service in service_list:
        if service["status"] == "running":
            print(f"service {service['name']} is healthy")
        else:
            print(f"service {service['name']} needs attention")
            stopped_count = stopped_count+1
            
    if stopped_count > 0:
        return "Issue found"
    else:
        return "All services healthy"

final_result=check_services(services)
print(final_result)
    