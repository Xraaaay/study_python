"""
@Description: python doc: https://docs.python.org/zh-cn/3/library/functions.html#open
@Author: Xraaaay
@Time: 2024/7/11
"""


def _open() -> None:
    """
    open() : Open file and return a corresponding file object.
    """
    with open(r'D:\Temp\test.txt', 'r', encoding='utf-8') as f:
        data = f.read()
        print(data)
