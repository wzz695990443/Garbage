import tomllib

from sqlalchemy import false


class ConfigProcess:
    def __init__(self):
        self.db_ssh_pwd = None
        self.db_ssh_user = None
        self.db_ssh_port = None
        self.db_ssh_host = None
        self.db_pwd = None
        self.db_user = None
        self.db_port = None
        self.db_host = None
        self.connectinfo = None

        with open("../config.toml", "rb") as fp:
            self.connectinfo = tomllib.load(fp)

    def get_conn_info(self, connect_name):
        self.db_host = self.connectinfo[connect_name]["db_host"]
        self.db_port = self.connectinfo[connect_name]["db_port"]
        self.db_user = self.connectinfo[connect_name]["db_user"]
        self.db_pwd  = self.connectinfo[connect_name]["db_pwd"]
        if self.connectinfo[connect_name]["is_ssh"]:
            self.db_ssh_host = self.connectinfo[connect_name]["db_ssh_host"]
            self.db_ssh_port = self.connectinfo[connect_name]["db_ssh_port"]
            self.db_ssh_user = self.connectinfo[connect_name]["db_ssh_user"]
            self.db_ssh_pwd  = self.connectinfo[connect_name]["db_ssh_pwd"]
        return {
            "db_host": self.db_host,
            "db_port": self.db_port,
            "db_user": self.db_user,
            "db_pwd" : self.db_pwd,
            "db_ssh_host": self.db_ssh_host,
            "db_ssh_port": self.db_ssh_port,
            "db_ssh_user": self.db_ssh_user,
            "db_ssh_pwd" : self.db_ssh_pwd
        }

    def get_conn_name(self):
        return [i for i in self.connectinfo.keys()]

if __name__ == "__main__":
    cp = ConfigProcess()
    print(cp.get_conn_name())
    print(cp.get_conn_info("gcschool"))
