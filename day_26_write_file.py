# Open the file in write mode ("w") which will create the file or overwrite if it exists.
# Write "Text" to the file and print the number of characters written.
with open("day_27_read_file.txt", "w") as file:
    print(file.write("Text"))  # Output: 4

# Open the file in append mode ("a") to add content to the end without overwriting existing data.
# Write "Text" again and print the number of characters written.
with open("day_27_read_file.txt", "a") as file:
     print(file.write("Text"))  # Output: 4

# Define a list of strings to write.
lines = ["Text 1", "Text 2", "Text 3"]

# Append the list of strings to the file using writelines (no newline between items unless added manually).
with open("day_27_read_file.txt", "a") as file:
     print(file.writelines(lines))  # Output: None (writelines returns None)

# Attempt to open the file in exclusive creation mode ("x").
# This will raise a FileExistsError if the file already exists.
with open("day_27_read_file.txt", "x") as file:
     print(file.writelines(lines))  # Will raise FileExistsError

# Check if the file is writable (outside the context manager, this will raise a ValueError since the file is closed).
print(file.writable())  # Error: I/O operation on closed file
