"""
@Description: python doc: https://docs.python.org/zh-cn/3/library/functions.html#id
@Author: Xraaaay
@Time: 2024/7/11
"""


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
