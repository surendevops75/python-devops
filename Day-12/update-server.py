
# Function to update a specific setting in a server configuration file
def update_server_config(file_path, key, value):

    # Step 1: Open the configuration file in read mode
    with open(file_path, 'r') as file:

        # Read all lines and store them in a list
        lines = file.readlines()

    # Step 2: Open the same file in write mode
    # Existing content will be cleared, so we rewrite every line
    with open(file_path, 'w') as file:

        # Step 3: Check each line in the configuration file
        for line in lines:

            # Check whether the required configuration key exists
            if key in line:

                # Write the key with its new value
                file.write(key + "=" + value + "\n")

            else:

                # Keep all other configuration lines unchanged
                file.write(line)


# Configuration file name
server_config_file = 'server.conf'

# Configuration key that needs to be updated
key_to_update = 'MAX_CONNECTIONS'

# New value for the configuration key
new_value = '600'

# Call the function to update the configuration file
update_server_config(server_config_file, key_to_update, new_value)

print("Server configuration updated successfully!")
