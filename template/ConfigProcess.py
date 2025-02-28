import tomllib

from sqlalchemy import false


class ConfigProcess:
    def __init__(self):
        self.conn_name = None
        self.db_type = None
        self.db_ssh_pwd = None
        self.db_ssh_user = None
        self.db_ssh_port = None
        self.db_ssh_host = None
        self.db_name = None
        self.db_pwd = None
        self.db_user = None
        self.db_port = None
        self.db_host = None
        self.connectinfo = None

        with open("../config.toml", "rb") as fp:
            self.connectinfo = tomllib.load(fp)

    def get_conn_info(self, connect_name):
        self.conn_name = self.connectinfo[connect_name]["conn_name"]
        self.db_type = self.connectinfo[connect_name]["db_type"]
        self.db_host = self.connectinfo[connect_name]["db_host"]
        self.db_port = self.connectinfo[connect_name]["db_port"]
        self.db_user = self.connectinfo[connect_name]["db_user"]
        self.db_pwd  = self.connectinfo[connect_name]["db_pwd"]
        self.is_ssh = self.connectinfo[connect_name]["is_ssh"]
        if self.connectinfo[connect_name]["db_name"]:
            self.db_name = self.connectinfo[connect_name]["db_name"]
        if self.is_ssh:
            self.db_ssh_host = self.connectinfo[connect_name]["db_ssh_host"]
            self.db_ssh_port = self.connectinfo[connect_name]["db_ssh_port"]
            self.db_ssh_user = self.connectinfo[connect_name]["db_ssh_user"]
            self.db_ssh_pwd  = self.connectinfo[connect_name]["db_ssh_pwd"]
        return {
            "conn_name": self.conn_name,
            "db_type": self.db_type,
            "db_host": self.db_host,
            "db_port": self.db_port,
            "db_user": self.db_user,
            "db_pwd" : self.db_pwd,
            "db_name": self.db_name,
            "is_ssh": self.is_ssh,
            "db_ssh_host": self.db_ssh_host,
            "db_ssh_port": self.db_ssh_port,
            "db_ssh_user": self.db_ssh_user,
            "db_ssh_pwd" : self.db_ssh_pwd
        }

    def get_conn_name(self,db_type = None):
        if db_type is None:
            return [i for i in self.connectinfo.keys()]
        elif db_type == "group":
            return [i for i in self.connectinfo.keys() if self.connectinfo[i]["db_type"] == "group"]
        elif db_type == "member":
            return [i for i in self.connectinfo.keys() if self.connectinfo[i]["db_type"] == "member"]
        elif db_type == "pms":
            return [i for i in self.connectinfo.keys() if self.connectinfo[i]["db_type"] == "pms"]

if __name__ == "__main__":
    cp = ConfigProcess()
    print(cp.get_conn_name())
    print(cp.get_conn_info("gcschool"))
