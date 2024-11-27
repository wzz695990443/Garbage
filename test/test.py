import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame
from template.FileProcessor import ExcelFileProcessor


# conn = DBConnect(db_host='192.168.63.240',db_port=3306,db_user='gc_project',db_pwd='gc_project0120',db_name='portal_pms',db_ssh_host='122.224.119.138',db_ssh_port=13305,db_ssh_user='root',db_ssh_pwd='240.deviskaifa',db_charset='utf8')
# conn.connect()
# data = conn.query('select * from sync_ip')
# conn.close()
# print(type(data))
# print(data)
# for item in data:
#     print(item)


if __name__ == '__main__':
    data = ((1, '服务器组A', 'ipms', 'http://localhost:8104/ipms', 'T'), (2, '服务器组A', 'group', 'http://127.0.0.1:8101/ipmsgroup', 'T'), (3, '服务器组A', 'member', 'http://localhost:8102/ipmsmember', 'T'), (8, '服务器组A', 'pos', 'http://localhost:8106/pos', 'T'), (9, 'default', 'rocketmq', 'http://124.221.194.237:9876', 'T'))
    df = pd.DataFrame(data, columns=['id', 'group_name', 'service_name', 'service_url', 'is_enable'])
    print(df)

    excel_file = ExcelFileProcessor('..\\static\\test.xlsx')
    excel_file.read_file()
    exfile = excel_file.get_data('DataFrame')
    print(exfile)






