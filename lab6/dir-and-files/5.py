def write_list_to_file(filename, data):
    try:
        with open(filename, 'w') as file:
            for item in data:
                file.write(str(item) + '\n')
        print(f"List has been written to '{filename}' successfully.")
    except Exception as e:
        print(f"Error: {e}")

filename = "5.py"
data = ["apple", "banana", "orange", "grape"]

write_list_to_file(filename, data)