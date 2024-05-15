"""
斐波那契额数列
"""


def fibonFun(nums: int) -> int:
    if nums == 1 or nums == 2:
        return nums - 1
    return fibonFun(nums - 1) + fibonFun(nums - 2)


if __name__ == "__main__":
    nums = int(input("请输入需要的位数:"))

    print(fibonFun(nums))
