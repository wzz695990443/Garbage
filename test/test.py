

array = list(range(901610,901860,10))
print(array)

update_sql = """"""
for i in array:
    update_sql += f"""SELECT `day` FROM rep_jour WHERE 1=1 AND code = '{i}';+"""
print(update_sql)
