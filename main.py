import requests

# Function to find empty Roblox groups within a specified range of group IDs
def find_empty_groups(min_group_id, max_group_id, max_requests=100):
    empty_groups = []  # List to store empty group IDs
    session = requests.Session()  # Create a session for improved performance
    total_requests = 0  # Counter for the total number of requests made

    for group_id in range(min_group_id, max_group_id + 1):
        try:
            if total_requests >= max_requests:
                print("Maximum requests reached. Exiting.")
                break

            url = f"https://groups.roblox.com/v1/groups/{group_id}"
            response = session.get(url)  # Send a GET request to the group URL
            total_requests += 1

            if response.status_code == 200:  # Check if the request was successful
                group_data = response.json()
                member_count = group_data.get('memberCount', 0)
                is_public_entry_allowed = group_data.get('publicEntryAllowed', True)

                # Check if the group is empty and allows public entry
                if member_count == 0 and is_public_entry_allowed:
                    empty_groups.append(group_id)
                    print("Successfully found an empty group:", group_id)
                    break  # Exit the loop after finding the first empty group

            print(f"Processed Group ID: {group_id}")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while processing Group ID: {group_id}")
            print(str(e))
            pass

    return empty_groups  # Return the list of empty group IDs

# Main function to set range and call the search function
def main():
    min_group_id = 100000  # Minimum group ID to start searching
    max_group_id = 200000  # Maximum group ID to end searching
    max_requests = 50  # Maximum number of requests to make

    empty_groups_list = find_empty_groups(min_group_id, max_group_id, max_requests)

    print("Empty Groups:")
    for group_id in empty_groups_list:
        print(group_id)

if __name__ == "__main__":
    main()  # Call the main function if the script is run directly
