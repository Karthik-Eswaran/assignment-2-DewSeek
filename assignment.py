import os
import importlib as il

def read_file(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(file_path: str, content: str) -> None:
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def list_files_in_directory(directory_path: str) -> list:
    return [file for file in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, file))]

def generate_numbers(n: int) -> iter:
    return iter(range(n))

def use_function_from_module(module_name: str, function_name: str, *args) -> any:
    return getattr(il.import_module(module_name), function_name)(*args)
