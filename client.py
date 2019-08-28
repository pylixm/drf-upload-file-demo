# -*- coding:utf-8 -*-
import requests
import json


# # multipart/form-data
# ret = requests.post('http://localhost:8001/api/v1/airticle/', data={
#         'title': '标题测试2',
#         'content': '正文测试2'
#     }, files={
#         'image': open('./image.jpeg', 'rb')
#     })
# print(json.loads(ret.content))
#

# 只上传图片
# ret = requests.put('http://localhost:8001/api/v1/airticle/upload/image.jpeg',
#                    files={
#                        'file': open('./image.jpeg', 'rb'),
#                    })
# print(ret.status_code)

# 自定义route
ret = requests.put('http://localhost:8001/api/v1/airticle/9/upload/',
                   files={
                       'file': open('./image.jpeg', 'rb'),
                   })
print(ret.status_code)