from template.ORM.Connect import Connect
from template.ORM.UpStatus import UpStatus, Base
from template.ORM.UpMapAccnt import UpMapAccnt, Base
import pandas as pd

db_host = '192.168.63.240'
db_port = 3306
db_user = 'gc_spt'
db_pwd  = 'gc_spt20220509'
db_name = 'portal_pms'
is_ssh  = True
db_ssh_host = '122.224.119.138'
db_ssh_port = 13305
db_ssh_user = 'root'
db_ssh_pwd  = '240.deviskaifa'

if __name__ == '__main__':
    try:
        conn = Connect(db_host = db_host, db_port = db_port, db_user = db_user, db_pwd = db_pwd, db_name = db_name, is_ssh = is_ssh, db_ssh_host = db_ssh_host, db_ssh_port = db_ssh_port, db_ssh_user = db_ssh_user, db_ssh_pwd = db_ssh_pwd)
        
        session = conn.connect()
        Base.metadata.create_all(conn.engine)
        if session is not None:
            print('Connect success')    
            # new_status = UpStatus(hotel_id = 9, up_step = 'test', time_begin = '2022-05-09 00:00:00', time_end = '2022-05-09 00:00:00', time_long = 1, remark = 'test')
            # new_map_accnt = UpMapAccnt(hotel_id = 9, hotel_group_id = 2, accnt_type = 'test', accnt_class = 'F', accnt_old = '', accnt_new = 1)
            # session.add_all([new_status, new_map_accnt])
            # session.flush()
            # session.refresh(new_status)
            # session.refresh(new_map_accnt)
            # print(new_status.id, new_map_accnt.id)
            # session.commit()
            
            data1 = session.query(UpStatus).all()
            data2 = session.query(UpMapAccnt).filter(UpMapAccnt.hotel_id == 9).all()
            print(pd.DataFrame(data1))
            print(pd.DataFrame(data2))
    except Exception as e:
        print(e)
    finally:
        print('Connect Closing')
        session.close()
        conn.close()
