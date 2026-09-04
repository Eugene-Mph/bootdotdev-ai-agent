

import os
from functions.get_files_info import get_files_info




def test() -> None:

    result = get_files_info("calculator")
    print("Result for current directory")
    print(result)



    result = get_files_info("calculator", "pkg")
    print("Result for pkg directory")
    print(result)


    result = get_files_info("calculator", "/bin")
    print("result for /bin")
    print(result)


    
    result = get_files_info("calculator", "../")
    print("result for ../")
    print(result)




if __name__ == "__main__":
    test()