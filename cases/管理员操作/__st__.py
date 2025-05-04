# cases/管理员操作/__st__.py
from cases.__st__ import suite_setup as root_suite_setup
from cases.__st__ import suite_teardown as root_suite_teardown
from lib.webui import *

force_tags = ['登录功能', '冒烟测试', 'UI测试']


def suite_setup():
    root_suite_setup()


def suite_teardown():
    root_suite_teardown()
