import os



def get_files_info(working_directory: str, directory: str =".") -> str:

    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

        if not valid_target_dir:
            return f"Error: Cannot list \"{directory}\" as it is outside the permited working directoty"

        is_dir_valid = os.path.isdir(target_dir)

        if not is_dir_valid:
            return f"Error: \"{directory}\" is not a directory"

        return get_file_data(target_dir)
        
    except Exception as err:
        return f"Error: {err}"
    
    return f"Success: \"{directory}\" is within the working directory"


def get_file_data(directory: str) -> str:

    try:
        files = os.listdir(directory)
        dir_summary: list[str] = []
        # print(files)

        for file in files:
            file_path = os.path.join(directory, file)
            filename = file
            size = os.path.getsize(file_path)
            is_dir = os.path.isdir(file_path)
            

            file_summary = f"- {filename}: file_size={size} bytes, is_dir={is_dir}"
            dir_summary.append(file_summary)
            
    except Exception as err:
        return f"Error: {err}"

    return "\n".join(dir_summary)

if __name__ == "__main__":
    pass