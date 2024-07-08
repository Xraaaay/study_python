"""
@Description: python doc: https://docs.python.org/zh-cn/3/library/functions.html#open
@Author: Xraaaay
@Time: 2024/7/2
"""


def _type() -> None:
    """
    type() : Return the type of the object.
    """
    int_type = type(10)
    str_type = type('str')
    dict_type = type({'key': 'value'})
    bool_type = type(True)

    print(f'{int_type=}')
    print(f'{str_type=}')
    print(f'{dict_type=}')
    print(f'{bool_type=}')


def _id() -> None:
    """
    id() : Return the address of an object in memory.
    """
    str1 = 'str'
    str2 = 'str'
    str3 = 'str'

    print(id(str1))
    print(id(str2))
    print(id(str3))


def _str() -> None:
    """
    str() : Return a string version of object.
    If object is not provided, returns the empty string.
    """
    f = 10.0
    s = str(f)
    print(type(s), f'{s=}')

    s = str()
    print(type(s), f'{s=}')
    print(id(''), id(s))


def _open() -> None:
    with open(r'D:\Temp\test.txt', 'r', encoding='utf-8') as f:
        data = f.read()
        print(data)


def main():
    _open()


if __name__ == '__main__':
    main()
