import os


def get_file_paths_from_folder(folder_path: str) -> list[str]:
    file_paths: list[str] = []
    for filename in os.listdir(folder_path):
        filepath: str = os.path.join(folder_path, filename)
        if os.path.isfile(filepath):
            file_paths.append(filepath)
    return file_paths
