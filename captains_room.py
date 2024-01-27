# Function to find the captain's room number
def find_captains_room(group_size, room_numbers):
    # Create a dictionary to store the count of each room number
    room_count = {}

    # Iterate through the list of room numbers
    for room in room_numbers:
        # If the room number is already in the dictionary, increment its count
        if room in room_count:
            room_count[room] += 1
        # If the room number is not in the dictionary, add it with count 1
        else:
            room_count[room] = 1

    # Iterate through the dictionary items
    for room, count in room_count.items():
        # Check for the room with count 1, as it represents the captain's room
        if count == 1:
            # Return the captain's room number
            return room

# Example usage
# Input the group size
group_size = int(input())
# Input the list of room numbers as integers
room_numbers = list(map(int, input().split()))

# Call the function to find the captain's room
captains_room = find_captains_room(group_size, room_numbers)

# Output the captain's room number
print(captains_room)
