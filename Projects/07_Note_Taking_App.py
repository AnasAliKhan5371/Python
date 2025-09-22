
import os
import sys

# Define a constant for the directory where notes will be stored.
NOTES_DIR="notes"

def check():
    """
    Checks if the notes directory exists. If not, it creates it.
    This ensures the application has a place to store note files.
    """
    # os.path.exists() checks if a file or directory exists at the given path.
    if not os.path.exists(NOTES_DIR):
        print(f"Creating a directory at: '{NOTES_DIR}/'")
        # os.makedirs() creates the directory, including any necessary parent directories.
        os.makedirs(NOTES_DIR)

def show():
    """
    Displays a list of all existing notes.
    It reads the filenames from the notes directory.
    Returns a list of note filenames or an empty list if none are found.
    """
    print("\n----Your Notes----")
    try:
        # Create a list of files in the NOTES_DIR that end with ".txt".
        notes=[f for f in os.listdir(NOTES_DIR) if f.endswith(".txt") ]
        # If the list of notes is empty, inform the user.
        if not notes:
            print("No notes found.")
            return []

        # Enumerate through the list of notes to display them with a number.
        # The '1' starts the numbering from 1 instead of the default 0.
        for i,note in enumerate(notes,1):
            # os.path.splitext() splits the filename from its extension. [0] gets the name part.
            print(f"{i}.{os.path.splitext(note)[0]}")
        return notes
    except FileNotFoundError:
        # This block runs if the NOTES_DIR does not exist.
        print("Notes directory not found.\nIt will be created for you. ")
        # Call check() to create the directory for future use.
        check()
        return []

def create():
    """
    Guides the user through creating a new note.
    It prompts for a title, sanitizes it for use as a filename,
    and then takes multi-line input for the note's content.
    """
    print("\n----Create a New Note----")
    title=input("Create a title for your note: ")

    # Check if the title is just whitespace.
    if not title.strip():
        print("ERROR: Title must have at least 1 character .")
        return

    # Sanitize the title to create a valid filename.
    # It keeps alphanumeric characters and underscores.
    corrected="".join(c for c in title if c.isalnum() or c in ('','_')).rstrip()
    if not corrected:
        print("ERROR: Title contains only invalid characters.")
        return

    # Construct the full filename and filepath.
    filename=corrected+".txt"
    filepath=os.path.join(NOTES_DIR,filename)

    # Check if a note with the same filename already exists to prevent overwriting.
    if os.path.exists(filepath):
        print(f"ERROR: A note with title '{corrected}' already exists.")
        return

    print("Enter content of your note. Type 'END' on a new line to save.")
    content_lines=[]
    # Loop indefinitely to capture multiple lines of input from the user.
    while True:
        line=sys.stdin.readline()
        # The loop breaks when the user types 'END' on a new line.
        if line.strip().upper()=='END':
            break
        content_lines.append(line)

    # Join the list of lines into a single string for the file content.
    content="".join(content_lines)

    try:
        # Use a 'with' statement to open the file, which handles closing it automatically.
        # 'w' mode means write mode, which will create the file if it doesn't exist.
        # 'encoding='utf-8'' is good practice for text files.
        with open(filepath,'w',encoding='utf-8') as f:
            f.write(content)
        print(f"\nSuccessfully created note: '{corrected}'")
    except IOError as e:
        # Catch potential errors during file writing.
        print(f"\nERROR: Could not write to file. {e}")

def view():
    """
    Allows the user to view the content of a specific note.
    It first lists the notes and then prompts the user to choose one.
    """
    # Get the list of available notes.
    notes=show()
    # If there are no notes, exit the function.
    if not notes:
        return

    try:
        # Get the user's choice and convert it to an integer.
        choice=int(input("\nEnter number of note you view: "))
        # Validate that the choice is within the valid range of note numbers.
        if 1<=choice<=len(notes):
            # Select the chosen note file from the list (adjusting for zero-based index).
            view_note=notes[choice-1]
            filepath=os.path.join(NOTES_DIR,view_note)

            # Open the selected note file in read mode ('r').
            with open(filepath,'r',encoding='utf-8') as f:
                content=f.read()

            # Print the title and content of the note.
            print(f"\n---Viewing: {os.path.splitext(view_note)[0]}---")
            print(content)
            print("----End of Note----")
        else:
            print("Invalid number. Please choose a number from list.")
    except ValueError:
        # This handles cases where the input is not a number.
        print("Invalid input. Please enter a number.")
    except FileNotFoundError:
        # This handles the unlikely case the file was deleted after being listed.
        print("ERROR: Selected note file does not exist.")
    except IOError as e:
        # This handles other file reading errors.
        print(f"Error reading note: {e}")

def delete():
    """
    Allows the user to delete a specific note.
    It lists the notes, asks for a selection, and requires confirmation.
    """
    # Get the list of available notes.
    notes=show()
    # If there are no notes, exit the function.
    if not notes:
        return
    try:
        # Get the user's choice and convert it to an integer.
        choice = int(input("\nEnter number of note you want to delete: "))
        # Validate the user's choice.
        if 1 <= choice <= len(notes):
            # Select the note to be deleted from the list.
            delete_note = notes[choice - 1]
            filepath = os.path.join(NOTES_DIR, delete_note)

            # Ask for confirmation before deleting.
            confirm=input(f"Are you sure you want to delete '{os.path.splitext(delete_note)[0]}'(y/n)?")
            if confirm.lower()=='y':
                # os.remove() deletes the file at the specified path.
                os.remove(filepath)
                print(f"Successfully deleted note: '{os.path.splitext(delete_note)[0]}'")
            else:
                print("Deletion cancelled.")
        else:
            print("Invalid number. Please choose number from list.")
    except ValueError:
        # This handles cases where the input is not a number.
        print("Invalid input. Please enter a number.")
    except FileNotFoundError:
        # This handles the case where the file might have been deleted by another process.
        print("ERROR: Selected note file does not exist. It might have been already deleted.")
    except IOError as e:
        # This handles other file deletion errors.
        print(f"Error deleting note: {e}")

def menu():
    """
    Displays the main menu of options to the user and captures their choice.
    Returns the user's input as a string.
    """
    print("\n--------------------")
    print("  Note Taking App")
    print("--------------------")
    print("1. Create new note")
    print("2. View note")
    print("3. Show all notes")
    print("4. Delete note")
    print("5. Exit")
    print("--------------------")
    return input("Choose an option: ")

def main():
    """
    The main function that runs the application loop.
    It checks for the notes directory, then continuously
    displays the menu and executes the chosen action.
    """
    # First, ensure the notes directory exists.
    check()
    # This is the main application loop. It runs until the user chooses to exit.
    while True:
        # Display the menu and get the user's choice.
        choice=menu()
        # Branch to the appropriate function based on the user's choice.
        if choice == '1':
            create()
        elif choice == '2':
            view()
        elif choice == '3':
            show()
        elif choice == '4':
            delete()
        elif choice == '5':
            # If the choice is 5, print a goodbye message and break the loop.
            print("Exiting the application. Goodbye!")
            break
        else:
            # Handle any invalid input.
            print("Invalid option, please try again.")

        # Pause the application until the user presses Enter, making the flow more readable.
        input("\nPress Enter to return to the menu...")

# This is a standard Python construct.
# It ensures that the main() function is called only when the script is executed directly,
# not when it's imported as a module into another script.
if __name__ == "__main__":
    main()