"""
冒泡排序+时间复杂度演示
"""


def bubbleSort(param: list) -> list:
    lens_ = len(param) - 1

    if lens_ <= 0:
        return param

    for i in range(lens_, 0, -1):
        for j in range(i):
            if param[j] > param[j + 1]:
                temp = param[j]
                param[j] = param[j + 1]
                param[j + 1] = temp

    return param


if __name__ == "__main__":
    print(bubbleSort([1, 3, 7, 2, 4, 6]))
