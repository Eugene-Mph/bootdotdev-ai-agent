

from functions.write_file import write_file


def test() -> None:

    res = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(res)

    res = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum doler sit amet")
    print(res)

    res = write_file("calculator", "/tmp/tmp.txt", "this should not be allowed")
    print(res)

if __name__ == "__main__":
    test()
