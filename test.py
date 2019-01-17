import requests
import threading
import csv
import json

# total = 0
# diff = 0
# k = 5
#
#
# def sum(arg1, arg2):
#     global diff
#     total = arg1 + arg2 + k
#     diff = arg1 - arg2 + k
#     print('total in', total)
#     print('diff in', diff)
#     print('k in', k)
#     return total
#
#
# print(sum(20, 10))
# print('total out', total)
# print('diff out', diff)
# print('k out', k)

aaa='''
"error": {
"message": "该帐号已停用，主页无法访问",
"code": 310001,
"name": "AccountHangError"
}
'''
aaa = json.dumps(aaa)
print(type(aaa))
