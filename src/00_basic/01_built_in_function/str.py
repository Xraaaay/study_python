"""
@Description: python doc: https://docs.python.org/zh-cn/3/library/functions.html#str
@Author: Xraaaay
@Time: 2024/7/11
"""


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
