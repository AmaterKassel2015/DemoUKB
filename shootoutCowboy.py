import random  # Library for generating random numbers
import hashlib  # Library for cryptographic hashing
import json  # Library for working with JSON data
def simulate_shootout(num_cowboys):
    cowboys = ['Cowboy {}'.format(i) for i in range(1, num_cowboys + 1)]  # Create a list of cowboy names
    hp = {cowboy: 10 for cowboy in cowboys}  # Initialize health points for each cowboy to 10

    protocol = []  # List to store the protocol of shots fired

    while len(cowboys) > 1:  # Continue until only one cowboy is left
        shooter = random.choice(cowboys)  # Randomly select a shooter from the remaining cowboys
        target = cowboys[(cowboys.index(shooter) + 1) % len(cowboys)]  # Determine the target based on shooter's position
        shot_hp = random.randint(1, 5)  # Randomly generate health points lost in the shot

        hp[target] -= shot_hp  # Reduce target's health points

        protocol.append({'shooter': shooter, 'target': target, 'health_lost': shot_hp, 'remaining_hp': hp[target]})  # Add shot details to protocol

        if hp[target] <= 0:  # Check if the target is killed
            cowboys.remove(target)  # Remove the killed cowboy from the list of cowboys

    return protocol  # Return the shootout protocol

def write_protocol(protocol):
    with open('shootout_protocol.json', 'w', encoding='utf-8') as file:
        json.dump(protocol, file, ensure_ascii=False, indent=4)  # Write the protocol to a JSON file
def calculate_checksum(filename):
    hasher = hashlib.md5()  # Create an MD5 hash object
    with open(filename, 'rb') as file:
        buf = file.read()
        hasher.update(buf)  # Update the hash object with the file content
    return hasher.hexdigest()  # Get the hexadecimal digest of the hash

# Main program
num_cowboys = int(input('Enter the number of cowboys: '))  # Prompt the user to enter the number of cowboys
protocol = simulate_shootout(num_cowboys)  # Simulate the shootout and get the protocol
write_protocol(protocol)  # Write the protocol to a JSON file
checksum = calculate_checksum('shootout_protocol.json')  # Calculate the checksum of the protocol file

print('\nProtocol file created: shootout_protocol.json')
print('Checksum: {}'.format(checksum))