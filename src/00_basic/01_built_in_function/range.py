"""
@Description: python doc: https://docs.python.org/zh-cn/3/library/functions.html#range
@Author: Xraaaay
@Time: 2024/7/11
"""


def _range_01() -> None:
    """
    range() : Return an object that produces a sequence of integers from start (inclusive)
    to stop (exclusive) by step.
    """
    for i in range(5):
        print(i)


def _range_02() -> None:
    for i in range(1, 9, 2):
        print(i)


def main() -> None:
    _range_01()
    _range_02()


if __name__ == '__main__':
    main()
