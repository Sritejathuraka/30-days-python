# Open the file in read mode
with open("day_25_read_file.txt", "r") as file:
    
    # Read the entire content of the file at once
    entire_content = file.read()
    print("=== Entire Content ===")
    print(entire_content)

    # Try to read one more line (but this won't work because the file pointer is already at the end)
    one_line_content = file.read()
    print("=== One Line After Full Read ===")
    print(one_line_content)  # This will print an empty string

    # Now trying to read lines again – this will also give an empty list because the file is exhausted
    content = file.readlines()
    print("=== Line-by-Line Content ===")
    for line in content:
        print(line.strip())  # Nothing will print, since content is empty
