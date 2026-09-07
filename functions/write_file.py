import os



def write_file(working_directory: str, file_path: str, content: str) -> str:

    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))

        is_valid = os.path.commonpath([abs_working_dir, abs_file_path]) == abs_working_dir

        if not is_valid:
            return f"Error: Cannot write to \"{file_path}\" as it is outside the permitted working directory"

        if os.path.isdir(file_path):
            return f"Error: Cannot Write to \"{file_path}\" as it is a directory"

        # if os.path.isdir(abs_working_dir):

        os.makedirs(abs_working_dir, exist_ok=True)

        with open(abs_file_path, "w") as file:
            file.write(content)

    except Exception as err:
        return f"Error: {err}"

    return f"Succesfully wrote to \"{file_path}\" ({len(content)} characters written)"


schema_write_file = {
    "type" : "function",
    "function" : {
        "name" : "write_file",
        "description": "Writes text provided to the funtcion in the specified file relative to the working directory (overwrites the file if it exists)",
        "parameters" : {
            "type" : "object",
            "properties" : {
                "file_path" : {
                    "type": "string",
                    "description": "The path of the file to write to, relative to the working directory"
                },
                "content": {
                    "type": "string",
                    "description" : "The values to be written inside the given file"
                },
            }, 
        }, 
        "required" : ["file_path", "content"]
    }, 
}