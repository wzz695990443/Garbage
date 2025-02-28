from sqlalchemy import create_engine,Column, Integer, String, ForeignKey,DateTime,Boolean,Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship,joinedload
from sshtunnel import SSHTunnelForwarder

from template.ORM.CompanyBase import Base
from template.tool import is_meaningful

Base = declarative_base()

class Connect:
    def __init__(self, db_host = None, db_port: int= None, db_user= None, db_pwd= None, db_name=None,is_ssh=False, db_ssh_host=None, db_ssh_port: int=None, db_ssh_user=None, db_ssh_pwd=None, db_charset='utf8', ** kwargs):
        self.server = None
        self.DBSession = None
        self.is_ssh = is_ssh
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
        self.engine = None
        
    def connect(self):
        try:
            if self.is_ssh:
                self.server = SSHTunnelForwarder(
                    (self.db_ssh_host, self.db_ssh_port),
                    ssh_username=self.db_ssh_user,
                    ssh_password=self.db_ssh_pwd,
                    remote_bind_address=(self.db_host, self.db_port)
                )
                self.server.start()
                print('SSH is Connected')
                self.engine = create_engine(f"""mysql+pymysql://{self.db_user}:{self.db_pwd}@127.0.0.1:{self.server.local_bind_port}/{self.db_name}?charset={self.db_charset}""") 
                self.DBSession = sessionmaker(bind= self.engine)
                self.session = self.DBSession()
            else:
                self.engine = create_engine(f"""mysql+pymysql://{self.db_user}:{self.db_pwd}@{self.db_host}:{self.db_port}/{self.db_name}?charset={self.db_charset}""") 
                self.DBSession = sessionmaker(bind= self.engine)
                self.session = self.DBSession()
        except Exception as e:
            print(e)
        finally:
            if self.session is not None:
                return self.session
            
    def close(self):
        if self.is_ssh:
            self.server.stop()
            print('SSH is Closed')
            
            
            
            
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
            

