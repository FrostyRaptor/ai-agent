import os

def get_files_info(working_directory, directory=None):
    result = [f'Result for {"current" if directory == "." else f"'{directory}'"} directory:']
    end = False

    # Join directories to get the full path
    full_path = os.path.abspath(os.path.join(working_directory, directory))
    full_working_directory = os.path.abspath(working_directory)

    # Check if the path is within the working directory
    if not full_path.startswith(full_working_directory):
        result.append(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        end = True

    # Check if the path exists
    if not os.path.isdir(full_path):
        result.append(f'Error: "{directory}" is not a directory')
        end = True

    dir_lst = os.listdir(full_path)

    if not end:
        for file in dir_lst:
            if not os.path.isfile(os.path.join(full_path, file)) and not os.path.isdir(os.path.join(full_path, file)):
                continue

            result.append(f'- {file}: file_size={os.path.getsize(os.path.join(full_path, file))} bytes, is_dir={os.path.isdir(os.path.join(full_path, file))}')

    print("\n".join(result))
    return "\n".join(result)