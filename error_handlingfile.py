def modify_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Example modification: convert content to uppercase
        modified_content = content.upper()

        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print("Error: Problem reading or writing the file.")

# Example usage
modify_file('input.txt', 'output.txt')

def read_user_file():
    filename = input("Enter the filename to read: ")
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print("\nFile content:\n")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        print(f"Error: Could not read the file '{filename}'.")

# Run the function
read_user_file()
