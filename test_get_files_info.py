

import os
from functions.get_files_info import get_files_info




def test() -> None:
    result = get_files_info("calculator")
    print(result)

    # test if a given argument is in the scope of the working directory


    result = get_files_info("calculator", "/bin")
    print(result)


    result = get_files_info("calculator", "../")
    print(result)


    
    result = get_files_info("calculator", "main.py")
    print(result)




if __name__ == "__main__":
    test()