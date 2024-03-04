import os

def delete_file(path):
    try:
        if not os.path.exists(path):
            print(f"Error: File '{path}' does not exist.")
            return

        if not os.access(path, os.W_OK):
            print(f"Error: No write access to file '{path}'.")
            return

        os.remove(path)
        print(f"File '{path}' deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")

file_path = "file_to_delete.txt"
delete_file(file_path)