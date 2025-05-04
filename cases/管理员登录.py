from time import sleep
from lib.webui import *


def suite_teardown():
    # 清除方法
    # 登录需要输入用户名、密码，为不影响其他用例测试，需要清空值
    wd = GSTORE['wd']
    wd.find_element(By.ID, 'username').clear()
    wd.find_element(By.ID, 'password').clear()


class UI_000x:
    tags = ['登录功能', '冒烟测试', 'UI测试']

    ddt_cases = [
        {
            'name': '登录-0001',
            'para': [None, '88888888', '请输入用户名']
        },
        {
            'name': '登录-0002',
            'para': ['byhy', None, '请输入密码']
        },
        {
            'name': '登录-0003',
            'para': ['byh', '88888888', '登录失败 : 用户名或者密码错误']
        },
        {
            'name': '登录-0004',
            'para': ['byhy', '8888888', '登录失败 : 用户名或者密码错误']
        },
        {
            'name': '登录-0005',
            'para': ['byhy', '888888888', '登录失败 : 用户名或者密码错误']
        }
    ]

    def teststeps(self):
        wd = GSTORE['wd']
        wd.get('http://127.0.0.1/mgr/sign.html')
        # 取出参数
        username, password, info = self.para
        if username is not None:
            wd.find_element(By.ID, 'username').send_keys(username)
        if password is not None:
            wd.find_element(By.ID, 'password').send_keys(password)
        wd.find_element(By.TAG_NAME, 'button').click()
        sleep(1)
        notify = wd.switch_to.alert.text
        CHECK_POINT('弹出提示', notify == info)
        # 点击确定按钮
        wd.switch_to.alert.accept()

