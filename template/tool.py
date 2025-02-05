"""

"""
import base64
import datetime
import json
import os
import configparser
import pandas as pd

def decode(base64str):
    tmp = base64.b64decode(base64str)
    return bytearray([(b << 1 & 255) | (b >> 7) for b in tmp]).decode("utf8")


def is_meaningful(strs):
    """
    判断字符串有无实际意义
    """

    if strs == True or strs == False:
        return True
    elif isinstance(strs, list):
        for item in strs:
            if is_meaningful(item):
                return True
    elif isinstance(strs, int) or isinstance(strs, float):
        return True
    elif isinstance(strs, str) and strs.strip() == '':
        return False
    elif strs == None:
        return False
    return True


def convert_dict_valuestype(convert_dict: dict, type_dict: dict, is_mysql: bool):
    """
    用于批量转换字典的值的类型。

    :param convert_dict :被转换value类型的字典
    :param type_dict :转换时用于类型对照的字典，与convert_dict的key一样，value为对应的数据类型
    :param is_mysql :判断是否是MySQL字段类型
    """

    # 定义类型转换函数
    python_type = {
        "str": str,
        "int": int,
        "float": float,
        "bool": bool
    }

    mysql_to_python_type = {
        "VARCHAR": str,
        "CHAR": str,
        "TEXT": str,
        "MEDIUMTEXT": str,
        "LONGTEXT": str,
        "INT": int,
        "TINYINT": int,
        "SMALLINT": int,
        "MEDIUMINT": int,
        "BIGINT": int,
        "FLOAT": float,
        "DOUBLE": float,
        "DECIMAL": float,
        "DATE": str,
        "DATETIME": str,
        "TIMESTAMP": str,
        "TIME": str,
        "YEAR": int,
        "BLOB": bytes,
        "LONGBLOB": bytes
    }

    # 遍历列表 convert_dict 中的每个字典
    if is_mysql:
        for item in convert_dict:
            for key, type_str in type_dict.items():
                if key in item:
                    # 检查类型字符串是否有效
                    if type_str.upper() in mysql_to_python_type:
                        # 转换值的类型
                        item[key] = mysql_to_python_type[type_str.upper()](item[key])
                    else:
                        raise ValueError(f"未知类型: {type_str}")
    else:
        for item in convert_dict:
            for key, type_str in type_dict.items():
                if key in item:
                    # 检查类型字符串是否有效
                    if type_str.upper() in python_type:
                        # 转换值的类型
                        item[key] = python_type[type_str.upper()](item[key])
                    else:
                        raise ValueError(f"未知类型: {type_str}")

    return convert_dict

import json
import os

def save_data_to_json(data, file_path, mode='update'):
    """
    将数据保存到JSON文件中。

    :param data: 需要保存的数据
    :param file_path: JSON文件的地址
    :param mode: 操作模式，'update' 表示更新现有内容，'append' 表示在文件末尾添加新内容
    """

    # 检测路径是文件还是文件夹
    if os.path.isdir(file_path):
        raise ValueError(f"{file_path} 是一个文件夹，而不是文件")
    else:
        # 确保文件夹存在
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # 检测文件是否存在
    file_exists = os.path.exists(file_path)

    if mode == 'update':
        if file_exists:
            # 如果文件存在，重置内容，写入文件
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        else:
            with open(file_path,'x', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

    elif mode == 'append':
        if file_exists:
            with open(file_path,'a', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

        else:
            # 如果文件不存在，创建新文件并初始化为空列表
            with open(file_path, 'x', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

    else:
        raise ValueError("无效的模式，只能是 'update' 或 'append'")

    print(f"数据已成功保存到 {file_path}")


def save_data_to_ini(data, file_path, section='default', mode = 'update'):
    """
    将数据保存到ini文件中

    :param data: 需要保存的数据
    :param file_path: ini文件路径
    :param section: ini文件的section
    :param mode: 操作模式，'update' 表示更新现有内容，'append' 表示在文件末尾添加新内容
    :return:
    """

    # 检测路径是文件还是文件夹
    if os.path.isdir(file_path):
        raise ValueError(f"{file_path} 是一个文件夹，而不是文件")
    else:
        # 确保文件夹存在
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # 检测文件是否存在
    file_exists = os.path.exists(file_path)

    if mode == 'update':
        if file_exists:
            # 如果文件存在，重置内容，写入文件
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        else:
            with open(file_path,'x', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

    elif mode == 'append':
        if file_exists:
            with open(file_path,'a', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

        else:
            # 如果文件不存在，创建新文件并初始化为空列表
            with open(file_path, 'x', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

    else:
        raise ValueError("无效的模式，只能是 'update' 或 'append'")

    print(f"数据已成功保存到 {file_path}")



def insert_row_at_index(df, row_data, index):
    """
    在指定索引位置插入一行或多行数据到 DataFrame 中。

    :param df: 原始 DataFrame
    :param row_data: 要插入的行数据，可以是字典、Series 或 DataFrame
    :param index: 插入位置的索引
    :return: 插入新行或多行后的 DataFrame
    """
    if not isinstance(row_data, (dict, pd.Series, pd.DataFrame)):
        raise ValueError("row_data 必须是字典、pandas Series 或 pandas DataFrame")
    
    if index < 0 or index > df.shape[0]:
        raise IndexError("索引超出范围")
    
    # 将 row_data 转换为 DataFrame
    if isinstance(row_data, dict):
        row_data = pd.DataFrame([row_data])
    elif isinstance(row_data, pd.Series):
        row_data = row_data.to_frame().T
    
    # 分割 DataFrame
    df_before = df.iloc[:index]
    df_after = df.iloc[index:]
    
    # 合并 DataFrame 和新行或多行
    new_df = pd.concat([df_before, row_data, df_after], ignore_index=True)
    
    return new_df