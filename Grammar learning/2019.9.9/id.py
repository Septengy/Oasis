"""
用户身份验证

Version: 0.1
源程序作者: 骆昊
拷贝:Sep
"""

username = input('请输入用户名：')
password = input('请输入口令: ')
if username == 'admin' and password == '123456':
    print('身份验证成功')
else:
    print('身份验证失败！')