import requests


def find_empty_groups():
    empty_groups = []

    # Set the minimum and maximum group IDs to search within
    min_group_id = 100000
    max_group_id = 200000

    session = requests.Session()  # Use a session object for improved performance

    for group_id in range(min_group_id, max_group_id + 1):
        try:
            url = f"https://groups.roblox.com/v1/groups/{group_id}"
            response = session.get(url)  # Reuse the session for multiple requests

            if response.status_code == 200:
                group_data = response.json()

                member_count = group_data.get('memberCount', 0)
                is_public_entry_allowed = group_data.get('publicEntryAllowed', True)

                if member_count == 0 and is_public_entry_allowed:
                    empty_groups.append(group_id)
                    print("Succesfully found a group:")
                    print(group_id)
                    min_group_id = max_group_id
                    break

            print(f"Processed Group ID: {group_id}")
        except (requests.exceptions.RequestException, ConnectionError) as e:
            print(f"An error occurred while processing Group ID: {group_id}")
            print(str(e))
            print(empty_groups_list)
            pass

    return empty_groups


# Call the function to find empty groups
empty_groups_list = find_empty_groups()

# Print the list of empty groups
print("Empty Groups:")
for group_id in empty_groups_list:
    print(group_id)
