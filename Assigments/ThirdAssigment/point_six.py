# Example of With Statement (Handles files without needing to close them manually)
with open("example.txt", "w") as file:
    file.write("Line 1\nLine 2\nLine 3\n")

# Example of Seek and Tell
with open("example.txt", "r") as file:
    print("Current position:", file.tell())  # Shows the current position in the file (0)
    file.seek(9)  # Moves the pointer to position 9
    print("New position:", file.tell())  # Shows the new position
    print("Data read after seek:", file.readline())  # Reads from the new position

# Example of Readline (Reads one line at a time)
with open("example.txt", "r") as file:
    print("First line:", file.readline())  # Reads the first line
    print("Second line:", file.readline())  # Reads the second line

# Example of Readlines (Reads all lines and stores them in a list)
with open("example.txt", "r") as file:
    lines = file.readlines()
    print("All lines as a list:", lines)

# Example of Writelines (Writes a list of lines to the file)
new_lines = ["Line 4\n", "Line 5\n", "Line 6\n"]
with open("example.txt", "a") as file:
    file.writelines(new_lines)  # Writes multiple lines to the file

# Checking the final content of the file
with open("example.txt", "r") as file:
    print("Final file content:\n", file.read())
