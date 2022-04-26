#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:xiaohe
# datetime:2022/2/28 18:15
import time
import pytest
from test.func.calculator import Calculator

# - 测试整体执行开始/结束阶段，打印：测试开始/结束--作用域默认function，自动执行
@pytest.fixture(scope='session', autouse=True)
def begin():
    print("测试开始")
    yield
    print("测试结束")

# - 每条用例执行开始/结束阶段，打印：计算开始/结束--作用域设置为session级别，自动执行
@pytest.fixture(autouse=True)
def start():
    print("计算开始")
    yield
    print("计算结束")


# fixture提供calc实例
@pytest.fixture(autouse=True)
def get_calc():
    calc = Calculator()
    return calc


# 修改编码格式，测试用例收集完成后，将收集到的item的name和nodeid中文显示
def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


# log文件名时间显示
@pytest.fixture(scope="session", autouse=True)
def manage_logs(request):
    """Set log file name same as test name"""
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    log_name = './logs/' + now + '.logs'
    request.config.pluginmanager.get_plugin("logging-plugin").set_log_path(log_name)
