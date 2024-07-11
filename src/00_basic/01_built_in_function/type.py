"""
@Description: python doc: https://docs.python.org/zh-cn/3/library/functions.html#type
@Author: Xraaaay
@Time: 2024/7/11
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
