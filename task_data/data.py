# Define the path to your existing file
input_file_path = '2.txt'
output_file_path = '2_sanitized.txt'

# Open the input file and read the lines
with open(input_file_path, 'r') as file:
    lines = file.readlines()

# Initialize an empty list to hold the modified content
modified_lines = []

# Loop through the original lines and insert a new line every 10 lines
for i, line in enumerate(lines):
    modified_lines.append(line)
    if (i + 1) % 10 == 0:  # After every 10 lines, append a new line
        modified_lines.append('\n')  # This adds a blank line

# Write the modified content back to a new file or overwrite the original
with open(output_file_path, 'w') as file:
    file.writelines(modified_lines)

print(f"Modified file saved as: {output_file_path}")
