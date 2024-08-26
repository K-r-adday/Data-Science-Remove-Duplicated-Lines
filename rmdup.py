import sys

def remove_duplicate_lines(filename):
    # Use a set to track unique lines
    seen_lines = set()
    unique_lines = []

    # Read the contents of the file
    with open(filename, 'r') as file:
        for line in file:
            if line not in seen_lines:
                unique_lines.append(line)
                seen_lines.add(line)

    # Write the unique lines back to the file
    with open(filename, 'w') as file:
        file.writelines(unique_lines)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python remove_duplicates.py <filename>")
    else:
        filename = sys.argv[1]
        remove_duplicate_lines(filename)
