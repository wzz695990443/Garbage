import time

import numpy as np
from template.ORM.Connect import Connect
from template.ORM.UpStatus import UpStatus, Base
from template.ORM.UpMapAccnt import UpMapAccnt, Base
import pandas as pd
from template.DataPipeline import DataPipeline, DataProcessor

db_host = '192.168.63.240'
db_port = 3306
db_user = 'gc_spt'
db_pwd  = 'gc_spt20220509'
db_name = 'portal_pms'
is_ssh  = True
db_ssh_host = '122.224.119.138'
db_ssh_port = 13305
db_ssh_user = 'root'
db_ssh_pwd  = '240.deviskaifa'

def generate_random_dataframe(rows=5, cols=3):
    # 生成一个包含随机数据的DataFrame
    df = pd.DataFrame(np.random.randn(rows, cols), columns=[f'Column_{i+1}' for i in range(cols)])
    return df


def validate(data: pd.DataFrame, column: str, round: int):
    if column in data.columns:
        if data[column].values[round] is not None:
            return data[column].values[round]
    return "Flag"


if __name__ == '__main__':
    # helloworld = DataProcessor("字符串",hello())
    # clean_data = DataProcessor("数据清洗", lambda x: x.strip())
    # normalize = DataProcessor("数据归一化", lambda x: x.lower())
    # validate = DataProcessor("数据验证", lambda x: x if len(x) > 0 else"无效数据")

    # pipeline = DataPipeline()
    # pipeline.add_processor(clean_data).add_processor(normalize).add_processor(validate)

    # result = pipeline("  Hello World  ")
    # print(result)  # 输出: hello world
    # random_df = generate_random_dataframe(5, 3)
    # print(random_df)
    # print(validate(random_df, "Column_4", 0))
    # print(validate(random_df, "Column_3", 0))
    print(str(1) + str(2))
