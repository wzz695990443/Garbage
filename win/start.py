from template.DBConnect import DBConnect
from template.ConfigProcess import ConfigProcess
from template.DBtestconnect import DBtestconnect

if __name__ == '__main__':
    db = DBtestconnect()
    print(db.test_connect('gc_project'))
    
    
    # cp = ConfigProcess()
    # conn_info = cp.get_conn_info('gc_project')
    # print(conn_info)
    # print(type(conn_info))
    
    
    # cp = ConfigProcess()
    # conn_info = cp.get_conn_info('gc_project')
    # conn = DBConnect()
    # conn.form_connect(conn_info)
    # print(type(conn.db_port))
    # conn.connect()
    # conn.close()
    
    # conn = DBConnect(db_host = '192.168.63.240',
    #                     db_port = 3306,
    #                     db_user = 'gc_spt',
    #                     db_pwd  = 'gc_spt20220509',
    #                     db_ssh_host = '122.224.119.138',
    #                     db_ssh_port = 13305,
    #                     db_ssh_user = 'root',
    #                     db_ssh_pwd  = '240.deviskaifa')
    # conn.connect()
    # conn.close()
    
    # a = '1'
    # print(type(int(a)))