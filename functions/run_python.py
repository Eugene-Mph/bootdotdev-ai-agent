import os
import subprocess


def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:

    try:
        
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))
        
        is_valid = os.path.commonpath([abs_working_dir, abs_file_path]) == abs_working_dir

        if not is_valid:
            return f"Error: Cannot execute \"{file_path}\" as it is outside the permited workig directory"

        if not os.path.isfile(abs_file_path):
            return f"Error: \"{file_path}\" does not exist or is not a regular file"


        if not abs_file_path.endswith(".py"):
            return f"Error: \"{file_path}\" is not a Python file"
        
        command = ["python", file_path]

        if args:
            command.extend(args)

        
        result = subprocess.run(
            command,
            cwd=abs_working_dir,
            capture_output=True,
            text=True,
            timeout=30
        )
        

        
        stderr = result.stderr
        stdout = result.stdout

        output: list[str] = []

        if result.returncode != 0:
            output.append(f"Error: Process exited with code {result.returncode}")

        if not stdout and not stderr:
            output.append(f"No output produced")

        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")

        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")

        return "\n".join(output)

    except Exception as err:
        
        return f"Error: executing python file: {err}"


schema_run_python_file = {
    "type" : "function",
    "function" : {
        "name": "run_python_file",
        "description" : "Execute a specified python file withing the working directory and returns its output",
        "parameters" : {
            "type" : "object",
            "properties" : {
                "file_path" : {
                    "type" : "string",
                    "description" : "The path of of the file to execute, relative to the working directory",
                },
                "args" : {
                    "type" : "array",
                    "items" : "string",
                    "description" : "Optional list of arguments to pass to the python script",
                },
            },
        }, "required" : ["file_path"]
    },
}