# -*- coding: utf-8 -*-
# @Time: 2023/1/9 23:29
# @Author: LiuXiu
# @File : data_for_test.py


from faker import Faker

fake= Faker(locale="zh_CN")
print(fake.phone_number())