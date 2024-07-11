"""
@Description: python doc: https://docs.python.org/zh-cn/3/library/functions.html#getattr
@Author: Xraaaay
@Time: 2024/7/11
"""


class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def _getattr() -> None:
    """
    getattr() : Return the value of the named attribute of object.
    If the named attribute does not exist, default is returned if provided,
    otherwise AttributeError is raised.
    """
    user = User('adele', 35)
    print(f'Hello, {getattr(user, 'name')}')

    nationality = getattr(user, 'nationality', 'France')
    print(f'Are you from {nationality}?')
