import os
import shutil

def organize_files(directory):
    # File type categories and their extensions
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx", ".csv"],
        "Audio": [".mp3", ".wav", ".aac"],
        "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Programs": [".py", ".java", ".cpp", ".c", ".js", ".html", ".css"],
        "Others": []  # Default for unknown file types
    }

    # Ensure the directory exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    # Get all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip if it's a folder
        if os.path.isdir(file_path):
            continue

        # Find file extension
        _, file_extension = os.path.splitext(filename)

        # Determine file type category
        folder_name = "Others"  # Default category
        for category, extensions in file_types.items():
            if file_extension.lower() in extensions:
                folder_name = category
                break

        # Create the folder if it doesn't exist
        folder_path = os.path.join(directory, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        # Move file to the appropriate folder
        shutil.move(file_path, os.path.join(folder_path, filename))

    print(f"Files in '{directory}' have been organized successfully.")

# Example usage
if __name__ == "__main__":
    # Replace with the path of the directory to organize
    directory_to_organize = "/path/to/your/directory"
    organize_files(directory_to_organize)
