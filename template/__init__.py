import FileProcessor
from DBConnect import DBConnect
from DBtestconnect import DBtestconnect


# data = FileProcessor.ExcelFileProcessor('C:\\Users\\wzw\\AppData\\Roaming\\SQLyog\\Favorites\\02、协议单位迁移\\协议单位迁移模板.xlsx')
# for i in data.get_data():
#     print(i)

# conn = DBConnect(db_host='192.168.63.240',db_port=3306,db_user='gc_project',db_pwd='gc_project0120',db_name='portal_pms',db_ssh_host='122.224.119.138',db_ssh_port=13305,db_ssh_user='root',db_ssh_pwd='240.deviskaifa',db_charset='utf8')
# conn.connect()
# data = conn.query('select * from hotel')
# conn.close()
# for item in data:
#     print(item)

# DBtest = DBtestconnect('E:\Project\pythonProject\pythonProject\static\database_info.ini')
# DBtest.get_conn_info()
# DBtest.print_conn_info()

# hotel_group_id = [['1']]
# hotel_group_id[0][0] = '2'
# print(f'INSERT INTO up_status(hotel_id,up_step,time_begin,time_end,time_long,remark) VALUES({hotel_group_id[0][0]},\'COMPANY\',NOW(),NULL,0,\'\')')


dict = [
    {'a':'1','b':'2','c':'3','d':'4'},
    {'a':'5','b':'6','c':'7','d':'8'},
    {'a':'9','b':'10','c':'11','d':'12'}
]
#
# for item in dict:
#     for