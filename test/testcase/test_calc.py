#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:xiaohe
# datetime:2022/4/25 12:32
import logging
import allure
import pytest
import yaml


# 从yaml文件中获取add数据，根据入参level返回对应级别的datas和ids
# 获取yaml文件中的add数据
def get_data_add(level):
    with open("../data/data.yml", encoding='utf-8') as f:
        data = yaml.safe_load(f)
        add_data = data.get("add")
        # 返回一个元组：格式([[data1],[data2],[data3]],[ids])
        return (add_data.get(level).get("datas"),add_data.get(level).get("ids"))

# 获取yaml文件中的div数据
def get_data_div(level):
    with open("../data/data.yml", encoding='utf-8') as f:
        data = yaml.safe_load(f)
        div_data = data.get("div")
        return (div_data.get(level).get("datas"),div_data.get(level).get("ids"))


@allure.feature("计算器测试用例")
class TestCalc():

    # add-P0
    @pytest.mark.parametrize("a,b,excepted", get_data_add("P0")[0], ids=get_data_add("P0")[1])
    @pytest.mark.P0
    @allure.story("加法")
    @allure.title("加法-P0级别")
    def test_add_p0(self, a, b, excepted, get_calc): # 在conftest中实例的calc，在测试用例中使用需要传参get_calc
        result = get_calc.add(a, b)
        logging.info(f"输入数据:{a},{b},输出数据:{excepted}")
        assert result == excepted

    # add-P1_1
    @pytest.mark.parametrize("a,b,excepted", get_data_add("P1_1")[0], ids=get_data_add("P1_1")[1])
    @pytest.mark.P1_1
    @allure.story("加法")
    @allure.title("加法-P1_1级别")
    def test_add_p1_1(self, a, b, excepted, get_calc):
        result = get_calc.add(a, b)
        logging.info(f"输入数据:{a},{b},输出数据:{excepted}")
        assert result == excepted

    # add-P1_2
    @pytest.mark.parametrize("a,b,errortype", get_data_add("P1_2")[0], ids=get_data_add("P1_2")[1])
    @pytest.mark.P1_2
    @allure.story("加法")
    @allure.title("加法-P1_2级别")
    def test_add_p1_2(self, a, b, errortype, get_calc):
        # 捕获异常，eval将传入的字符串转换为类型
        with pytest.raises(eval(errortype)) as e:
            result = get_calc.add(a, b)
        assert e.typename == errortype

    # add-P2
    @pytest.mark.parametrize("a,b,errortype", get_data_add("P2")[0], ids=get_data_add("P2")[1])
    @pytest.mark.P2
    @allure.story("加法")
    @allure.title("加法-P2级别")
    def test_add_p2(self, a, b, errortype, get_calc):
        with pytest.raises(eval(errortype)) as e:
            result = get_calc.add(a, b)
        assert e.typename == errortype

    # div-P0
    @pytest.mark.parametrize("a,b,excepted", get_data_div("P0")[0], ids=get_data_div("P0")[1])
    @pytest.mark.P0
    @allure.story("除法")
    @allure.title("除法-P0级别")
    def test_div_p0(self, a, b, excepted, get_calc):
        result = get_calc.div(a, b)
        logging.info(f"输入数据:{a},{b},输出数据:{excepted}")
        assert result == excepted

    # div-P1_1
    @pytest.mark.parametrize("a,b,errortype", get_data_div("P1_1")[0], ids=get_data_div("P1_1")[1])
    @pytest.mark.P1_1
    @allure.story("除法")
    @allure.title("除法-P1_1级别")
    def test_div_p1_2(self, a, b, errortype, get_calc):
        with pytest.raises(eval(errortype)) as e:
            result = get_calc.div(a, b)
        assert e.typename == errortype

    # div-P1_2
    @pytest.mark.parametrize("a,b,errortype", get_data_div("P1_2")[0], ids=get_data_div("P1_2")[1])
    @pytest.mark.P1_2
    @allure.story("除法")
    @allure.title("除法-P1_2级别")
    def test_div_p1_2(self, a, b, errortype, get_calc):
        with pytest.raises(eval(errortype)) as e:
            result = get_calc.div(a, b)
        assert e.typename == errortype

    # div-P2
    @pytest.mark.parametrize("a,b,errortype", get_data_div("P2")[0], ids=get_data_div("P2")[1])
    @pytest.mark.P2
    @allure.story("除法")
    @allure.title("除法-P2级别")
    def test_div_p2(self, a, b, errortype, get_calc):
        with pytest.raises(eval(errortype)) as e:
            result = get_calc.div(a, b)
        assert e.typename == errortype
