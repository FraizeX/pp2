def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            line_count = sum(1 for line in file)
        return line_count
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return -1
    except Exception as e:
        print(f"Error: {e}")
        return -1

filename = "4.py"
line_count = count_lines(filename)
if line_count != -1:
    print(f"Number of lines in '{filename}': {line_count}")