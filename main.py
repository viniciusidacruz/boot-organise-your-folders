import os
from tkinter.filedialog import askdirectory

source_folder = askdirectory(title="Source Folder");
destination_folder = askdirectory(title="Destination Folder");

file_rules = {
    "git": "Git",
    "oop": "OOP",
    "github": "Github",
    "nodejs": "Backend",
    "javascript": "Javascript",
    "react": "Frontend",
    "vite": "Frontend",
    "nextjs": "Frontend",
    "nestjs": "Backend",
    "boot": "Python"
};

file_list = os.listdir(source_folder);

for name_file in file_list:
    for key_rule in file_rules.keys():
        if key_rule in name_file:
            new_folder = file_rules[key_rule];
            full_new_folder_path = os.path.join(destination_folder, new_folder);
            full_original_path = os.path.join(source_folder, name_file);
            full_destination_path = os.path.join(destination_folder, new_folder, name_file);
            
            if not os.path.exists(full_new_folder_path):
                os.mkdir(full_new_folder_path);
            
            os.rename(full_original_path, full_destination_path)