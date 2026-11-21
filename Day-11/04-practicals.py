
# Store configuration details of multiple servers
server_config = {

    'server1': {
        'ip': '192.168.1.1',
        'port': 8080,
        'status': 'active'
    },

    'server2': {
        'ip': '192.168.1.2',
        'port': 8000,
        'status': 'inactive'
    },

    'server3': {
        'ip': '192.168.1.3',
        'port': 9000,
        'status': 'active'
    }
}


# Function to retrieve the status of a specific server
def get_server_status(server_name):

    # Find the server and return its status
    # If the server does not exist, return "Server not found"
    return server_config.get(server_name, {}).get(
        'status', 'Server not found'
    )


# Specify the server whose status needs to be checked
server_name = 'server2'


# Call the function and store the returned status
status = get_server_status(server_name)


# Display the server name and its current status
print(f"{server_name} status: {status}")
