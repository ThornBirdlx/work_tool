# -*- coding: utf-8 -*-
# @Time: 2023/2/14 22:19
# @Author: LiuXiu
# @File : handle_json.py

from jsonpath import jsonpath
import time

data ={
  "data": {
    "auditorder": [
      {
        "auditorderid": "au20211027171351429",
        "createtime": 1635326031,
        "ww_corpid": "1970324986089526",
        "vid": "1688850879438971",
        "suiteid": 1006769,
        "status": 5,
        "audittime": 1635326036,
        "suitename": "第一象限小助手",
        "corpname": "杭州一知智能科技有限公司",
        "logo": "https://p.qlogo.cn/bizmail/Otsttsx5SNdW1Hj5mKB86UiadA9RiaQ9NILC2CEAFBibaOVwadjM4SdLg/0",
        "app_name": "第一象限小助手",
        "corpappid": "5629501665483137",
        "authcorp_name": "北京智德瑞奇网络科技有限公司",
        "audit_order_type": 3
      },
      {
        "auditorderid": "au20211027170708128",
        "createtime": 1635325628,
        "ww_corpid": "1970324986089526",
        "vid": "1688850879438971",
        "suiteid": 1006769,
        "status": 5,
        "audittime": 1635325634,
        "suitename": "第一象限小助手",
        "corpname": "杭州一知智能科技有限公司",
        "logo": "https://p.qlogo.cn/bizmail/Otsttsx5SNdW1Hj5mKB86UiadA9RiaQ9NILC2CEAFBibaOVwadjM4SdLg/0",
        "app_name": "第一象限小助手",
        "corpappid": "5629503711523606",
        "authcorp_name": "上海亿朵网络科技有限公司",
        "audit_order_type": 3
      },
      {
        "auditorderid": "au20211027151923479",
        "createtime": 1635319163,
        "ww_corpid": "1970324986089526",
        "vid": "1688850879438971",
        "suiteid": 1006769,
        "status": 5,
        "audittime": 1635319169,
        "suitename": "第一象限小助手",
        "corpname": "杭州一知智能科技有限公司",
        "logo": "https://p.qlogo.cn/bizmail/Otsttsx5SNdW1Hj5mKB86UiadA9RiaQ9NILC2CEAFBibaOVwadjM4SdLg/0",
        "app_name": "第一象限小助手",
        "corpappid": "5629501161552801",
        "authcorp_name": "深圳市富安娜家居用品股份有限公司",
        "audit_order_type": 3
      },
      {
        "auditorderid": "au20211027111117749",
        "createtime": 1635304277,
        "ww_corpid": "1970324986089526",
        "vid": "1688850879438971",
        "suiteid": 1006769,
        "status": 5,
        "audittime": 1635304296,
        "suitename": "第一象限小助手",
        "corpname": "杭州一知智能科技有限公司",
        "logo": "https://p.qlogo.cn/bizmail/Otsttsx5SNdW1Hj5mKB86UiadA9RiaQ9NILC2CEAFBibaOVwadjM4SdLg/0",
        "app_name": "第一象限小助手",
        "corpappid": "5629502102558277",
        "authcorp_name": "英氏控股集团股份有限公司",
        "audit_order_type": 3
      },
      {
        "auditorderid": "au2021102710174818",
        "createtime": 1635301068,
        "ww_corpid": "1970324986089526",
        "vid": "1688850879438971",
        "suiteid": 1006769,
        "status": 5,
        "audittime": 1635301084,
        "suitename": "第一象限小助手",
        "corpname": "杭州一知智能科技有限公司",
        "logo": "https://p.qlogo.cn/bizmail/Otsttsx5SNdW1Hj5mKB86UiadA9RiaQ9NILC2CEAFBibaOVwadjM4SdLg/0",
        "app_name": "第一象限小助手",
        "corpappid": "5629503178570648",
        "authcorp_name": "北京厚大轩成教育科技股份公司",
        "audit_order_type": 3
      },
      {
        "auditorderid": "au2021102619095862",
        "createtime": 1635246598,
        "ww_corpid": "1970324986089526",
        "vid": "1688850879438971",
        "suiteid": 1006769,
        "status": 5,
        "audittime": 1635246603,
        "suitename": "第一象限小助手",
        "corpname": "杭州一知智能科技有限公司",
        "logo": "https://p.qlogo.cn/bizmail/Otsttsx5SNdW1Hj5mKB86UiadA9RiaQ9NILC2CEAFBibaOVwadjM4SdLg/0",
        "app_name": "第一象限小助手",
        "corpappid": "5629499986576689",
        "authcorp_name": "测试二哈-修改",
        "audit_order_type": 3
      },

      {
        "auditorderid": "au20211026170244333",
        "createtime": 1635238964,
        "ww_corpid": "1970324986089526",
        "vid": "1688850879438971",
        "suiteid": 1006769,
        "status": 5,
        "audittime": 1635238969,
        "suitename": "第一象限小助手",
        "corpname": "杭州一知智能科技有限公司",
        "logo": "https://p.qlogo.cn/bizmail/Otsttsx5SNdW1Hj5mKB86UiadA9RiaQ9NILC2CEAFBibaOVwadjM4SdLg/0",
        "app_name": "第一象限小助手",
        "corpappid": "5629502490576628",
        "authcorp_name": "中国联通scrm演示账号",
        "audit_order_type": 3
      },

      {
        "auditorderid": "au20211012133603142",
        "createtime": 1634016963,
        "ww_corpid": "1970324986089526",
        "vid": "1688850879438968",
        "suiteid": 1006769,
        "status": 5,
        "audittime": 1634016969,
        "suitename": "第一象限小助手",
        "corpname": "杭州一知智能科技有限公司",
        "logo": "https://p.qlogo.cn/bizmail/Otsttsx5SNdW1Hj5mKB86UiadA9RiaQ9NILC2CEAFBibaOVwadjM4SdLg/0",
        "app_name": "第一象限小助手",
        "corpappid": "5629500868575799",
        "authcorp_name": "杭州探意智能科技有限公司",
        "audit_order_type": 3
      }
    ],
    "total": 373
  }
}
authcorp_name = jsonpath(data, "$..authcorp_name")
audittime = jsonpath(data, "$..audittime")
status = jsonpath(data, "$..status")
print(status)

def get_name():
  for n in authcorp_name:
      print(n)

def temp_time():
   for i in audittime:
      timeStamp = i
      timeArray = time.localtime(timeStamp)
      otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
      print(otherStyleTime)


get_name()
temp_time()