import pandas as pd
import numpy as np
import template.Table
from template.Table import CompanyBase

if __name__ == '__main__':
    company_base = CompanyBase()
    company_base.append([9, 2, 0, '绿云', 'Lu Yun', 'Lu Yun', '绿云LuYunLuYunLY', 'F', 'C', 'CN', '1465328798', '', '', '', '', '',
           '', '', '', '', 'NULL', 'NULL', '', '', 'CN', '', '', '', '杭州市天苑大厦', '', '', 'NULL', '', '', '', '', '', '',
           'T', 'GCPM', 'ADMIN', '2022-01-12 16:40:02', 'GCPM', 'ADMIN', '2022-08-14 21:42:03', '*'])
    company_base.hotel_group_id = 2
    company_base.hotel_id = 9
    a = company_base.get()
    for index, row in a.iterrows():
        print(row)
        print(type(row))
        print(int(index))
    # for item in a.loc[0]:
    #     print(item)
    # print(", ".join(row for index,row in a.iterrows()))
    # for index, row in a.iterrows():
    #     sql = f'INSERT INTO company_base({", ".join(item for item in company_base.table_columns)}) VALUES ({company_base.hotel_group_id},{company_base.hotel_id},NULL,{", ".join(item for item in row[3:].astype(str))})'
    #     print(sql)
    # print(a)
    # company_base.init_type()
    # b = company_base.get()
    # print(b.dtypes)
    # print(b)
    # test = pd.DataFrame(['2024-02-01', '2024-02-02','2024-02-03'])
    # print(test)
    # test.astype('datetime64[ns]')
    # print(test)
