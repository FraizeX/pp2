import string

def generate_files():
    try:
        for letter in string.ascii_uppercase:
            filename = letter + ".txt"
            with open(filename, 'w') as file:
                file.write("This is file " + filename)
            print(f"File '{filename}' created successfully.")
    except Exception as e:
        print(f"Error: {e}")

generate_files()