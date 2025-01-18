"""
DBupdateinfo:用于从SQLyog数据库连接配置的ini文件中批量获取能够连接到数据库的配置信息
"""

import configparser
import os

import DBConnect
from tool import decode
import ConfigProcess


class DBtestconnect():
    def __init__(self,path = '../config.toml'):
        self.conninfo = []
        if not isinstance(path,str):
            raise TypeError('请输入正确参数类型！')
        elif os.path.isfile(path):
            self.path = path
        else:
            raise NameError('请输入正确的文件路径！')

    def get_conn_info(self):
        global testconn
        ini = configparser.ConfigParser(allow_no_value=True)
        ini.read(self.path, encoding='utf8')
        connections = [r for r in ini.sections() if r.startswith('Connection')]
        for c in connections:
            try:
                name = ini.get(c, 'Name')
                host = ini.get(c, 'Host')
                port = ini.getint(c, 'Port')
                user = ini.get(c, 'User')
                password = decode(ini.get(c, 'Password'))
                sshhost = ini.get(c, 'SshHost')
                sshport = ini.getint(c, 'SshPort')
                sshuser = ini.get(c, 'SshUser')
                sshpwd = decode(ini.get(c, 'SshPwd'))
                testconn = DBConnect.DBConnect(host, port, user, password, '', sshhost, sshport, sshuser, sshpwd)
                testconn.connection_timeout = 5
                testconn.connect()
                self.conninfo.append({'name': name, 'db_host': host, 'db_port': port, 'db_user': user, 'db_pwd': password, 'db_ssh_host': sshhost, 'db_ssh_port': sshport, 'db_ssh_user': sshuser, 'db_ssh_pwd': sshpwd})
            except Exception as e:
                print(e)
            finally:
                testconn.close()
        return self.conninfo

    def print_conn_info(self):
        for conn in self.conninfo:
            for key, value in conn.items():
                print(key, ':', value)
            print('----------------------------------------------------------------------------------')



