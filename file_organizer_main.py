import os
import shutil

def is_folder(folder):
    """
    Checks if a folder with that name exists
    Returns True if it does and returns False if it does not
    """
    if os.path.isdir(folder):
        return True
    else:
        return False

def folder_factory(folder, file_ext):
    """
    Creates subfolder with ext if it does not exist
    If it does exist, do nothing
    declares
        ext = extension
        tar_dir = target directory(folder)
    returns tar_dir
    """
    ext = file_ext.lower().lstrip(".")
    if ext == "":
        ext = "other"
    tar_dir = os.path.join(folder, ext)
    if os.path.isdir(tar_dir):
        print(f'Using folder: {tar_dir}')
    else:
        os.makedirs(tar_dir)
        print(f'Created folder: {tar_dir}')
    return tar_dir

def move(full_path, tar_dir, name):
    """
     Moves files into tar_dir, uses incrementor to avoid overwriting
     declares
        end = destination folder
        base = source folder
        ext = file extension
        i = incrementor
    """
    end = os.path.join(tar_dir, name)
    base, ext = os.path.splitext(name)
    i = 1
    while os.path.exists(end):
        end = os.path.join(tar_dir, f'{base}({i}){ext}') #adds folder
        i += 1
    print(f'Moving: {full_path} to {end}')
    shutil.move(full_path, end)
    print(f'Moved: {full_path} to {end}')

def scanner(folder):
    """
    Scans the files within the folder specified.
    declares
        total = found number of files
        moved = moved files
        skipped = skipped files
        name = folder
        full_path = source folder path
        file_name = file
        file_ext = extension
        ext = extension with "." or ""
        tar_dir = target directory
    prints what is found and loops through the files
    calls folder_factory
    calls move
    """
    total = 0
    moved = 0
    skipped = 0
    print(f'Scanning: {folder}')
    for name in os.listdir(folder): #gets list of names inside folder
        full_path = os.path.join(folder, name) #sets full_path to path of user input folder
        if os.path.isfile(full_path): #if exists
            total += 1
            file_name, file_ext = os.path.splitext(name) #splits name and extension
            print(f'Found:{name} (ext:{file_ext})')
            tar_dir = folder_factory(folder, file_ext)
            move(full_path, tar_dir, name)
            moved += 1
        else:
            print(f'Skipping {name}')
            skipped += 1
    print(f'Found:{total}, Moved:{moved}, Skipped:{skipped}')

def main():
    """
    Gets user input
    Calls is_folder
        Reprompts if folder does not exist
    Calls scanner
    declares folder
    ends once completed
    """
    while True: #prompts for userinput for folder. ch
        folder = input("What folder do you need organized?(Enter the folder path): ")
        if is_folder(folder):
            scanner(folder)
            print("Completed all operations.")
            break
        else:
            print("The folder does not exist")




if __name__ == "__main__":
     main()
