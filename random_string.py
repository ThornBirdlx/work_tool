# -*- coding: utf-8 -*-
# @Time: 2022/12/5 12:23
# @Author: LiuXiu
# @File : random_string.py


"""
1、随机数字
2、随机字母
"""
import random
import string


def get_random_string():
    r_len = 30
    token = "".join(random.sample(string.ascii_letters + string.digits, r_len))
    return token
    # print(token)


for i in range(1, 10):
    print("{}_{}".format(get_random_string(), i))

