
import os
import config

def get_file_content(working_directory: str, file_path: str) -> str:

    try:

        abs_working_dir = os.path.abspath(working_directory)
        abs_target_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))

        is_filepath_valid = os.path.commonpath([abs_working_dir, abs_target_file_path]) == abs_working_dir

        if not is_filepath_valid:
            return f"Error: Cannot read {file_path} as it is outside the permited working directory"

        if not os.path.isfile(abs_target_file_path):
            return f"Error: File not found or is not a regular file: \"{file_path}\""


        with open(abs_target_file_path) as file:
            content = file.read(config.MAX_CHARS)

            if file.read(1):
                content += (f"[...File \"{file_path}\" truncated at {config.MAX_CHARS} characters]")
    except Exception as err:

        return f"Error reading file \"{file_path}\": {err}"
    
    return content


schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Read the text content of the specified file relative to the working directory, proving a string of the file content",
        "parameters": {
            "type" : "object",
            "properties" : {
                "file_path" : {
                    "type": "string",
                    "description" : "The path of the file to read from",
                },
                
            }
        }
    }
}