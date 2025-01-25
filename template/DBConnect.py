"""
DBConnect:用于连接数据库
"""

import pymysql
from sshtunnel import SSHTunnelForwarder

from template.tool import is_meaningful


class DBConnect:
    def __init__(self, db_host = None, db_port: int= None, db_user= None, db_pwd= None, db_name=None, db_ssh_host=None, db_ssh_port: int=None, db_ssh_user=None, db_ssh_pwd=None, db_charset='utf8',** kwargs):
        self.conn = None
        self.server = None
        self.db_host = db_host
        self.db_port = db_port
        self.db_user = db_user
        self.db_pwd = db_pwd
        self.db_name = db_name
        self.db_ssh_host = db_ssh_host
        self.db_ssh_port = db_ssh_port
        self.db_ssh_user = db_ssh_user
        self.db_ssh_pwd  = db_ssh_pwd
        self.db_charset = db_charset
        self.connection_timeout = 10

    def connect(self):
        if is_meaningful(self.db_ssh_host) and is_meaningful(self.db_ssh_port) and is_meaningful(self.db_ssh_user) and is_meaningful(self.db_ssh_pwd):
            self.server = SSHTunnelForwarder(
                (self.db_ssh_host, self.db_ssh_port),
                ssh_username=self.db_ssh_user,
                ssh_password=self.db_ssh_pwd,
                remote_bind_address=(self.db_host, self.db_port)
            )
            self.server.start()
            self.conn = pymysql.connect(
                host='127.0.0.1',
                port=self.server.local_bind_port,
                user=self.db_user,
                password=self.db_pwd,
                db=self.db_name,
                charset=self.db_charset,
                connect_timeout=self.connection_timeout
            )
        else:
            self.conn = pymysql.connect(
                host=self.db_host,
                port=self.db_port,
                user=self.db_user,
                password=self.db_pwd,
                db=self.db_name,
                charset=self.db_charset,
                connect_timeout=self.connection_timeout
            )

    def close(self):
        if self.conn is not None:
            self.conn.close()
        if self.db_ssh_host is not None and self.db_ssh_port is not None and self.db_ssh_user is not None and self.db_ssh_pwd is not None:
            self.server.stop()

    def execute(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        self.conn.commit()
        cursor.close()

    def query(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result


    def form_connect(self,dict :dict):
        for key,value in dict.items():
            if key == 'db_host':
                self.db_host = value
            elif key == 'db_port':
                self.db_port = int(value)
            elif key == 'db_user':
                self.db_user = value
            elif key == 'db_pwd':
                self.db_pwd = value
            elif key == 'db_name':
                self.db_name = value
            elif key == 'db_ssh_host':
                self.db_ssh_host = value
            elif key == 'db_ssh_port':
                self.db_ssh_port = value
            elif key == 'db_ssh_user':
                self.db_ssh_user = value
            elif key == 'db_ssh_pwd':
                self.db_ssh_pwd = value
            elif key == 'db_charset':
                self.db_charset = value
            else:
                raise ValueError('Invalid key: {}'.format(key))





