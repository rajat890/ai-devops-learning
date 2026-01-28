servers = [
    {"name": "server1", "status":"running"},
    {"name": "server2", "status":"stopped"},
    {"name": "server3", "status":"running"},
]

def server_status(server_list):
    for server in server_list:
        print(f"server name is {server['name']} and status is {server['status']}")

server_status(servers)