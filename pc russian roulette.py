import random
import os

# List of all files in the specified directory and its subdirectories
def get_all_files(directory):
    all_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            all_files.append(os.path.join(root, file))
    return all_files

# Start the roulette
def start_roulette():
    # List of all files on your PC (customise the directory as needed)
    all_files = get_all_files("C:\\")
    
    # Randomly decide whether to delete a file or System32 (1% chance)
    if random.randint(1, 100) == 1:
        # Redirection: instead of targeting System32, target a harmless directory
        target = "C:\\Windows\\Temp"
    else:
        # Randomly select a file to delete
        target = random.choice(all_files)
    
    # Remove the selected file or directory
    try:
        if os.path.isfile(target):
            os.remove(target)
            print(f"Deleted file: {target}")
        elif os.path.isdir(target):
            os.rmdir(target)
            print(f"Deleted directory: {target}")
        else:
            print(f"Invalid target: {target}")
    except FileNotFoundError:
        print(f"File not found: {target}")
    except PermissionError:
        print(f"Permission denied: {target}")
    except OSError as e:
        print(f"Error deleting {target}: {e}")

# Ask user if they want to start the roulette
start = input("Would you like to start (y/n)? ").lower()

# Check user's response
if start == "y":
    start_roulette()
elif start == "n":
    print("Roulette aborted.")
else:
    print("Invalid input. Please enter 'y' for yes or 'n' for no.")
