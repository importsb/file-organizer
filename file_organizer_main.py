import os

def is_folder(folder):
    """
    Checks if a folder with that name exists
    Returns True if it does and returns False if it does not
    """
    if os.path.isdir(folder):
        return True
    else:
        return False

def is_valid_dir(full_path):
    """
    """
def bank(file_name, file_ext):
    """
    """

def move(full_path, tar_dir, file_name):
    """
    """
def scanner(folder):
    """
    Scans the files within the folder specified.
    Gets name, file_name, file_ext
    prints what is found and loops through the files
    """
    for name in os.listdir(folder):
        full_path = os.path.join(folder, name)
        if os.path.isfile(full_path):
            file_name, file_ext = os.path.splitext(name)
            file_ext = file_ext.lower()
            print(f"Found file: {name}, extension: {file_ext}")
        else:
            print(f"Skipping folder: {name}")

def fancy_printer(folder):
    """
    Prints in a fancy way.
    """
    print(f"Folder: " + folder + str(os.path.splitext(folder)[0]))



def main():
    """
    Gets user input
    Calls is_folder
    """
    while True:
        folder = input("What folder do you need organized?(Enter the folder path): ")
        if is_folder(folder):
            fancy_printer(folder)
        else:
            print("The folder doesn't exist")




if __name__ == "__main__":
     main()
