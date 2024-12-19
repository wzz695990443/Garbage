from datetime import datetime
import numpy as np
table_name = 'company_base'
table_columns = (
    'id', 'hotel_group_id', 'hotel_id', 'company_id', 'sta', 'manual_no', 'sys_cat', 'flag_cat', 'grade',
    'latency', 'class1', 'class2', 'class3', 'class4', 'src', 'channel', 'market', 'vip',
    'belong_app_code', 'membership_type', 'membership_no', 'membership_level', 'over_rsvsrc',
    'valid_begin', 'valid_end', 'code1', 'code2', 'code3', 'code4', 'code5', 'flag', 'saleman', 'ar_no1',
    'ar_no2', 'extra_flag', 'extra_info', 'comments', 'create_user', 'create_datetime',
    'modify_user', 'modify_datetime', 'is_verified'
)
table_types = (
    'bigint', 'bigint', 'bigint', 'bigint', 'varchar', 'varchar', 'varchar', 'varchar', 'varchar', 'varchar',
    'varchar', 'varchar', 'varchar', 'varchar', 'varchar', 'varchar', 'varchar', 'varchar', 'varchar',
    'varchar', 'varchar', 'varchar', 'varchar', 'datetime', 'datetime', 'varchar', 'varchar', 'varchar',
    'varchar', 'varchar', 'varchar', 'varchar', 'bigint', 'bigint', 'varchar', 'varchar', 'varchar', 'varchar',
    'datetime', 'varchar','datetime', 'varchar'
)
A =  f'INSERT INTO {table_name}({", ".join(item for item in table_columns[1:])}) VALUES '
print(A)
