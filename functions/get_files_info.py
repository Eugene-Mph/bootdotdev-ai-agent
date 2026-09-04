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
        
    except Exception as err:
        return f"Error: {err}"
    
    return f"Success: \"{directory}\" is within the working directory"


if __name__ == "__main__":
    pass