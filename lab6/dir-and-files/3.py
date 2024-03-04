import os

def analyze_path(path):
    if os.path.exists(path):
        print("Path exists.")

        directory, filename = os.path.split(path)
        print("Directory:", directory)
        print("Filename:", filename)
    else:
        print("Path does not exist.")

path = "C:/Users/mrfra/OneDrive/Documents/pp2/lab6/dir-and-files"
analyze_path(path)