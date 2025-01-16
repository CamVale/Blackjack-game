import os

def replace_underscores_with_spaces():

    current_dir = os.getcwd()

    files = os.listdir(current_dir)

    for filename in files:
        
        new_filename = filename.replace('_', ' ')

        os.rename(filename, new_filename)
        print(f"Renamed {filename} to {new_filename}")

if __name__ == "__main__":
    replace_underscores_with_spaces()