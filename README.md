# Russian Roulette File Deletion

This Python script, *russian_roulette_file_deletion.py*, is a game of chance where you risk deleting a file or directory from your computer. It's intended for entertainment purposes only and should be used with caution.

## How it Works

1. **get_all_files(directory):**
   - This function retrieves a list of all files in the specified directory and its subdirectories.

2. **start_roulette():**
   - Initiates the roulette game.
   - Retrieves a list of all files on the PC, customising the directory as needed.
   - Randomly decides whether to delete a file or target the System32 directory (with a 1% chance of targeting System32).
   - If not targeting System32, randomly selects a file from the list to delete.
   - Attempts to remove the selected file or directory, handling errors such as file not found, permission denied, or other OS-related errors.

3. **User Interaction:**
   - Asks the user if they want to start the roulette game.
   - Based on the user's response:
     - 'y': Initiates the roulette.
     - 'n': Aborts the roulette.
     - Any other input: Prompts the user to enter 'y' for yes or 'n' for no.

## Usage

1. **Clone Repository:**
   - Clone this repository to your local machine.

2. **Customise Directory (Optional):**
   - If you want to target a specific directory other than "C:\\", modify the `directory` parameter in the `start_roulette()` function call.

3. **Run the Script:**
   - Execute the script by running *russian_roulette_file_deletion.py*.
   - Follow the prompts to decide whether to start the roulette game.

4. **Proceed with Caution:**
   - Be cautious when running this script as it involves potential deletion of files or directories, which may cause irreversible damage to your system.

5. **Disclaimer:**
   - This script is for entertainment purposes only and should not be used on critical systems or without proper backups.
   - The developer is not responsible for any loss of data or damage caused by the use of this script.
