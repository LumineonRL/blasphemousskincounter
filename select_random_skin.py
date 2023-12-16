import os
import random
import json
import sys

def get_random_directory(path: str) -> str:
    os.chdir(path)
    directories = [d for d in os.listdir('.') if os.path.isdir(d)]
    if not directories:
        raise ValueError("No skins found in the specified directory.")
    random_directory = random.choice(directories)
    return random_directory

def extract_name_from_info_file(directory: str) -> str:
    info_file_path = os.path.join(directory, 'info.txt')
    if not os.path.exists(info_file_path):
        raise FileNotFoundError(f"info.txt not found in directory: {directory}")
    with open(info_file_path, 'r', encoding='utf-8') as info_file:
        info = json.load(info_file)
        name = info['name']
    return name

def main():
    default_directory_path = r'C:\Program Files (x86)\Steam\steamapps\common\Blasphemous\Modding\skins'
    directory_path = sys.argv[1] if len(sys.argv) > 1 else default_directory_path
    try:
        random_dir = get_random_directory(directory_path)
        extracted_name = extract_name_from_info_file(random_dir)
        print(f"Skin to use: {extracted_name}")
    except ValueError as ve:
        print(str(ve))
        print("Please verify that the path to your skins folder is set correctly.")
    except FileNotFoundError as fe:
        print(str(fe))
        print("Please verify that the path to your skins folder is set correctly and that an 'info.txt' file is present in the specified directory.")

if __name__ == "__main__":
    main()