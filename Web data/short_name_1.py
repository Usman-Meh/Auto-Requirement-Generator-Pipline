import os

def shorten_filename(name, max_length=30):
    """Shortens a filename if it exceeds the max length."""
    if len(name) > max_length:
        base, ext = os.path.splitext(name)
        shortened_name = base[:max_length - len(ext) - 3] + "..." + ext
        return shortened_name
    return name

def rename_files_in_folder(folder_path, max_length=50):
    """Renames files in the given folder with shorter names."""
    for root, _, files in os.walk(folder_path):
        for file in files:
            old_path = os.path.join(root, file)
            new_name = shorten_filename(file, max_length)
            new_path = os.path.join(root, new_name)
            
            # Check if the new file name already exists and append a counter if necessary
            counter = 1
            while os.path.exists(new_path):
                name, ext = os.path.splitext(new_name)
                new_name = f"{name}_{counter}{ext}"
                new_path = os.path.join(root, new_name)
                counter += 1
            
            # Rename the file if the name is changed
            if old_path != new_path:
                os.rename(old_path, new_path)
                print('Successfully renamed:')
                print(f"Renamed: {old_path} -> {new_path}")

# Specify the folder containing the files
folder_path = r"B:\check_Dat"

# Call the function to rename files
rename_files_in_folder(folder_path)
