"""
DBupdateinfo:用于从SQLyog数据库连接配置的ini文件中批量获取能够连接到数据库的配置信息
"""

import configparser
import os

from template.DBConnect import DBConnect
from template.tool import decode
from template.ConfigProcess import ConfigProcess


class DBtestconnect():
    def __init__(self,path = '../config.toml'):
        self.conninfo = []
        if not isinstance(path,str):
            raise TypeError('请输入正确参数类型！')
        elif os.path.isfile(path):
            self.path = path
        else:
            raise NameError('请输入正确的文件路径！')

    def test_connect(self,conn_name):
        global conn
        cp = ConfigProcess()
        conn_info = cp.get_conn_info(conn_name)
        conn = DBConnect()
        conn.form_connect(conn_info)
        
        try:       
            conn.connect()            
        except Exception as e:
            return(False)
        finally:
            conn.close()
            
        return(True)

    def print_conn_info(self):
        for conn in self.conninfo:
            for key, value in conn.items():
                print(key, ':', value)
            print('----------------------------------------------------------------------------------')



