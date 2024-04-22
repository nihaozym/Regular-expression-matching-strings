# Read content of output file and remove duplicates
def remove_duplicates_from_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    # Convert lines to set to remove duplicates
    unique_lines = set(lines)

    # Write unique lines back to output file
    with open(output_file_path, 'w') as file:
        file.writelines(unique_lines)

# Path to input file (output.txt)
input_file_path = 'output.txt'

# Path to output file without duplicates
output_file_path = 'output_no_duplicates.txt'

# Remove duplicates from output file
remove_duplicates_from_file(input_file_path, output_file_path)

print(" output_no_duplicates.txt")
